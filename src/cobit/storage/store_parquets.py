from pathlib import Path

import pyarrow as pa
import pyarrow.parquet as pq

from cobit.ingestion.ingestion_pipeline import ingest_market_trades, ingest_order_book
from cobit.utils.config import CONFIG
from cobit.utils.logger import logger_setup, INFO
from cobit.utils.utils import generate_filename_timestamp

logger = logger_setup(
    __name__,
    CONFIG['logging']['storage_log'],
    INFO,
)

def save_table_to_parquet(table: pa.Table, directory: str, filename: str) -> None:
    """Save a PyArrow table to parquet."""
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)

    if not filename.endswith('.parquet'):
        filename += '.parquet'

    timestamped_name = f'{generate_filename_timestamp()}_{filename}'
    filepath = directory / timestamped_name

    pq.write_table(table, filepath)

    logger.info(f'Successfully saved table to {filepath}')

    return filepath
