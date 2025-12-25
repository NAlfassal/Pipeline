from __future__ import annotations
import logging
import sys
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "src") not in sys.path:
    sys.path.insert(0, str(ROOT / "src"))

from data_workflow.config import make_paths
from data_workflow.io import read_parquet, write_parquet
from data_workflow.quality import require_columns, assert_non_empty, assert_unique_key, assert_in_range
from data_workflow.transformers import parse_datetime, add_time_parts, winsorize, add_outlier_flag
from data_workflow.joins import safe_left_join

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
log = logging.getLogger(__name__)

def main() -> None:
    p = make_paths(ROOT)
    
    log.info("Loading cleaned datasets...")
    orders = read_parquet(p.processed / "orders_clean.parquet")
    users = read_parquet(p.processed / "users.parquet")

   
    require_columns(orders, ["order_id", "user_id", "amount", "created_at"])
    require_columns(users, ["user_id", "country"])

    assert_non_empty(orders, name="Cleaned Orders")
    assert_non_empty(users, name="Users Table")
    
    assert_unique_key(users, "user_id")
    log.info("Initial checks passed. Data is ready for processing.")

    orders_t = parse_datetime(orders, "created_at", utc=True)
    orders_t = add_time_parts(orders_t, "created_at")

    log.info("Joining tables...")
    analytics_df = safe_left_join(
        orders_t, users, on="user_id", validate="many_to_one", suffixes=("", "_user")
    )

    if len(analytics_df) != len(orders_t):
        raise AssertionError(f"Join explosion detected! Rows changed from {len(orders_t)} to {len(analytics_df)}")

    log.info("Handling outliers...")
    analytics_df = add_outlier_flag(analytics_df, "amount", k=1.5)
    analytics_df = analytics_df.assign(
        amount_winsor=winsorize(analytics_df["amount"])
    )

    assert_in_range(analytics_df["amount_winsor"], lo=0, name="amount_winsor")

    out_path = p.processed / "analytics_table.parquet"
    write_parquet(analytics_df, out_path)
    log.info("Wrote final analytics table with %s rows.", len(analytics_df))

if __name__ == "__main__":
    main()