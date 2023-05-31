from os.path import join

from yaml import safe_load

from src import RESOURCE_PATH


def get_config_key(key: str) -> str:
    return safe_load(open(join(RESOURCE_PATH, 'config.yml')))[key]
