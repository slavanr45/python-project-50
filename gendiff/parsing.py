import json
import yaml


def read_data(name: str) -> dict:
    with open(name, encoding='utf8') as file:
        if name.endswith('.json'):
            return json.load(file)
        elif name.endswith(('.yaml', '.yml')):
            return yaml.load(file, Loader=yaml.loader.SafeLoader)


# def check_diff(data1: dict, data2: dict) -> str:
#     result = '{\n'
#     for key in sorted(data1 | data2):
#         a = data1.get(key, None)
#         b = data2.get(key, None)
#         if a == b:
#             result += f'    {key}: {data1[key]}\n'
#         else:
#             if a is not None:
#                 result += f'  - {key}: {data1[key]}\n'
#             if b is not None:
#                 result += f'  + {key}: {data2[key]}\n'
#     return result + '}'


def check_diff(data1: dict, data2: dict) -> dict:
    result = {}
    for key in sorted(data1 | data2):
        a = data1.get(key, 9999)
        b = data2.get(key, 9999)
        if isinstance(a, dict) and isinstance(b, dict):
            result[key] = check_diff(a, b)
        else:
            if a == b:
                result[key] = a
            else:
                if a != 9999:
                    result[key+'-1'] = a
                if b != 9999:
                    result[key+'-2'] = b
    return result


def stylish(value, n=1, sep='    '):
    if not isinstance(value, dict):
        match value:
            case False:
                return 'false'
            case True:
                return 'true'
            case None:
                return 'null'
        return str(value)
    result = '{\n'
    for key, val in value.items():
        if key.endswith('-1'):
            result += (f'{sep * (n - 1) + "  - "}{key[:-2]}: {stylish(val, n+1)}\n')
        elif key.endswith('-2'):
            result += (f'{sep * (n - 1) + "  + "}{key[:-2]}: {stylish(val, n+1)}\n')
        else:
            result += (f'{sep * n}{key}: {stylish(val, n+1)}\n')
    result += (sep * (n-1) + '}')
    return result
