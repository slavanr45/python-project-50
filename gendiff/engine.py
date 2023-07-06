from gendiff.diff import make_diff
from gendiff.formaters.stylish import to_stylish
from gendiff.formaters.plain import to_plain
from gendiff.formaters.json import to_json
import json
import yaml


def read_data(name: str) -> dict:
    with open(name, encoding='utf8') as file:
        if name.endswith('.json'):
            return json.load(file)
        elif name.endswith(('.yaml', '.yml')):
            return yaml.load(file, Loader=yaml.loader.SafeLoader)
        else:
            return file.read()


def generate_diff(file_path1: str, file_path2: str, format_name='stylish') -> str:
    data1 = read_data(file_path1)
    data2 = read_data(file_path2)
    data_prepared = make_diff(data1, data2)
    # pprint(data_prepared)
    # print()
    # # print(to_stylish(data_prepared))
    if format_name == 'stylish':
        return to_stylish(data_prepared)
    elif format_name == 'plain':
        return to_plain(data_prepared)
    elif format_name == 'json':
        return to_json(data_prepared)
