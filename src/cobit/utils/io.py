import json

from pathlib import Path

from cobit.utils.utils import generate_filename_timestamp

def save_raw_api_response_json(response: dict, directory: str, filename: str, indent: int = 0):
    """Save Kraken API response dict as JSON."""
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)

    if not filename.endswith('.json'):
        filename += '.json'

    timestamped_name = generate_filename_timestamp() + filename
    filepath = directory / timestamped_name
    
    with open(filepath, 'w') as f:
        json.dump(response, f, indent=indent)
