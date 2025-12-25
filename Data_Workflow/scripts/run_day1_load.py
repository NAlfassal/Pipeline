import sys
from pathlib import Path
import logging
import json 
from datetime import datetime, timezone

ROOT = Path(__file__).parent.parent
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from data_workflow.config import make_paths
from data_workflow.io import read_orders_csv, read_users_csv, write_parquet
from data_workflow.transformers import enforce_schema

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger("Day1Loader")

def main():

    paths = make_paths(ROOT)
    logger.info(" Starting Data Processing Pipeline")
    logger.info("Loading raw data")
    orders_input = read_orders_csv(paths.raw / "orders.csv")
    users_input = read_users_csv(paths.raw / "users.csv")
    processed_orders = enforce_schema(orders_input)
    orders_output = paths.processed / "orders.parquet"
    users_output = paths.processed / "users.parquet"

    write_parquet(processed_orders, orders_output)
    logger.info(f"Orders saved to {orders_output}")
    
    write_parquet(users_input, users_output)
    logger.info(f"Users saved to {users_output}")
    
    
    Metadata_description = {
        "total_orders": len(processed_orders),
        "total_users": len(users_input),
        "processed_at": datetime.now(timezone.utc).isoformat(),
    }
    metadata_output = paths.processed / "metadata.json"
    with open(metadata_output, "w") as f:
        json.dump(Metadata_description, f, indent=4)
    logger.info(f" Metadata saved to {metadata_output}")

    logger.info("Processing completed successfully")

    logger.info("Run metadata: %s", metadata_output)
    logger.info("Wrote: %s", paths.processed)

if __name__ == "__main__":
    main()
