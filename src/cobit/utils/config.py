import json
import os

from importlib.resources import files

def load_config():
    config_path = files("cobit").joinpath("config.json")
    return json.loads(config_path.read_text())

CONFIG = load_config()
ENDPOINTS = CONFIG['endpoints']
