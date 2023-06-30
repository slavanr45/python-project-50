import json
# import json_diff


def json_load(name: str) -> dict:
    with open(name, encoding='utf8') as file:
        return json.load(file)


def generate_diff(first: str, second: str):
    data1 = json_load(first)
    data2 = json_load(second)
    result = json_diff(data1, data2)
    return result


def json_diff(data1: dict, data2: dict) -> str:
    result = '{\n'
    for key in sorted(data1 | data2):
        a = data1.get(key, None)
        b = data2.get(key, None)
        if a == b:
            result += f'    {key}: {data1[key]}\n'
        elif b is None:
            result += f'  - {key}: {data1[key]}\n'
        elif a is None:
            result += f'  + {key}: {data2[key]}\n'
        else:
            result += f'  - {key}: {data1[key]}\n'
            result += f'  + {key}: {data2[key]}\n'
    return result + '}'
