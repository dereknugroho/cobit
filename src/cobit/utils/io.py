import json

from pathlib import Path

from cobit.utils.config import CONFIG
from cobit.utils.logger import logger_setup, INFO
from cobit.utils.utils import generate_filename_timestamp

logger = logger_setup(
    __name__,
    CONFIG['logging']['ingestion_log'],
    INFO
)

def save_raw_api_response_json(response: dict, directory: str, filename: str):
    """Save Kraken API response dict as JSON."""
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)

    if not filename.endswith('.json'):
        filename += '.json'

    timestamped_name = generate_filename_timestamp() + filename
    filepath = directory / timestamped_name
    
    with open(filepath, 'w') as f:
        json.dump(response, f)

    logger.info(f'Successfully saved raw Kraken response to {filepath}')
