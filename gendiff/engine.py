from gendiff.diff import make_diff
from gendiff.formaters import to_stylish, to_plain
import json
import yaml


def read_data(name: str) -> dict:
    with open(name, encoding='utf8') as file:
        if name.endswith('.json'):
            return json.load(file)
        elif name.endswith(('.yaml', '.yml')):
            return yaml.load(file, Loader=yaml.loader.SafeLoader)
        return file.read().strip()


def generate_diff(file_path1: str, file_path2: str, format_name='stylish') -> str:
    data1 = read_data(file_path1)
    data2 = read_data(file_path2)
    data_prepared = make_diff(data1, data2)
    # print(data_prepared)
    # print(list(stylish(data_prepared)))
    # print()
    # path = 'tests/fixtures/'
    # with open(path + 'result_nested.txt', encoding='utf8') as file:
    #     print(list(file.read()))
    if format_name == 'stylish':
        return to_stylish(data_prepared)
    elif format_name == 'plain':
        return to_plain(data_prepared)
