import json

from cobit.kraken.kraken_auth import request, get_kraken_keys
from cobit.utils.config import CONFIG
from cobit.utils.logger import logger_setup, ERROR

# Initialize logger
logger = logger_setup(
    __name__,
    CONFIG['logging']['kraken_client_filepath'],
    ERROR,
)

def make_request(path: str, body: dict = None, query: dict | None = None, method: str = 'GET'):
    """A wrapper for making API requests."""
    public_key, private_key = get_kraken_keys()

    try:
        response = request(
            method=method,
            path=path,
            query=query,
            body=body,
            public_key=public_key,
            private_key=private_key,
            environment=CONFIG['environment']
        )
        data = json.loads(response.read().decode('utf-8'))

        # Handle Kraken internal error response
        if data['error']:
            logger.error(f'Kraken API returned error(s): {data["error"]}')
            return None

        return data

    except Exception as e:
        logger.exception(f'Request to Kraken failed for path {path}: {e}')
        raise
