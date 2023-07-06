import json
from gendiff.formaters.stylish import to_stylish


def to_json(data: dict) -> str:
    return json.dumps(to_stylish(data).split('\n'), indent=0)
