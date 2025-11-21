import json
import os

from importlib.resources import files

def load_config():
    config_path = files("cobit").joinpath("config.json")
    return json.loads(config_path.read_text())

config = load_config()

def get_kraken_keys():
    """Safely attempt to retrieve Kraken API keys."""
    try:
        return os.environ["API_KEY_KRAKEN"], os.environ["API_SEC_KRAKEN"]
    except KeyError:
        raise RuntimeError("Kraken API keys not set in environment.")
