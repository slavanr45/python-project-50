import json
import yaml


def parse_data(name: str) -> dict:
    with open(name, encoding='utf8') as file:
        if name.endswith('.json'):
            return json.load(file)
        if name.endswith(('.yaml', '.yml')):
            return yaml.load(file, Loader=yaml.loader.SafeLoader)
        return None
