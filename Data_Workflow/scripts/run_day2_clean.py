import sys
from pathlib import Path
from datetime import datetime, timezone
import logging
import json

ROOT = Path(__file__).parent.parent
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from data_workflow.config import make_paths
from data_workflow.io import read_orders_csv, read_users_csv, write_parquet
from data_workflow.transformers import enforce_schema, missingness_report, add_missing_flags, normalize_text, apply_mapping, dedupe_keep_latest
from data_workflow.quality import require_columns, assert_non_empty, assert_unique_key, assert_in_range

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger("DataCleaner")

def main():
    paths = make_paths(ROOT)
    logger.info("Loading data..")
    raw_orders = read_orders_csv(paths.raw / "orders.csv")
    raw_users = read_users_csv(paths.raw / "users.csv")

    logger.info("Running quality checks on columns..")
    require_columns(raw_orders, ["order_id","user_id","amount","quantity","created_at","status"])
    require_columns(raw_users, ["user_id", "country"])
    assert_non_empty(raw_orders, name="Orders")
    assert_non_empty(raw_users, name="Users")
    orders = enforce_schema(raw_orders)
    orders = dedupe_keep_latest(orders, key_cols=["order_id"], ts_col="created_at")
    logger.info("Checks on Deduplication completed")

    m_report = missingness_report(orders)
    report_path = ROOT / "reports" / "missingness_orders.csv"
    report_path.parent.mkdir(exist_ok=True)
    m_report.to_csv(report_path)
    logger.info(f"Missingness Report saved to {report_path}")

    status_norm = normalize_text(orders["status"])
    s_map = {"refunded": "refund", "payment_complete": "paid"}
    orders = orders.assign(
        status_clean=apply_mapping(status_norm, s_map)
    )
    
    orders = add_missing_flags(orders, cols=["amount", "quantity"])
    assert_unique_key(orders, key="order_id")
    assert_in_range(orders["amount"], lo=0, name="amount")
    assert_in_range(orders["quantity"], lo=0, name="quantity")

    logger.info("Writing final Parquet files...")
    write_parquet(orders, paths.processed / "orders_clean.parquet")
    write_parquet(raw_users, paths.processed / "users.parquet")

    summary = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "orders_count": len(orders),
        "users_count": len(raw_users)
    }
    (paths.processed / "run_meta.json").write_text(json.dumps(summary, indent=4))
    
    logger.info("Data processing completed successfully.")

if __name__ == "__main__":
     main()
