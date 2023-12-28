import os
import yaml

SETTINGS = None


def load_config(config_path: str) -> None:
    global SETTINGS

    if not os.path.isfile(config_path):
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(config_path) as file:
        SETTINGS = yaml.safe_load(file)
