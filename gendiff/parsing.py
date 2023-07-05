import json
import yaml


def read_data(name: str) -> dict:
    with open(name, encoding='utf8') as file:
        if name.endswith('.json'):
            return json.load(file)
        elif name.endswith(('.yaml', '.yml')):
            return yaml.load(file, Loader=yaml.loader.SafeLoader)
        return file.read().strip()


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


def stylish(data: dict, level=1) -> str:
    if not isinstance(data, dict):
        match data:  # correcting formating for keywords
            case False:
                return 'false'
            case True:
                return 'true'
            case None:
                return 'null'
        return str(data)
    result = '{\n'
    for key, val in data.items():
        result += (f'{make_indent(key, level)}: {stylish(val, level+1)}\n')
    return result + ('    ' * (level-1) + '}')  # add tail


def make_indent(word, n, sep='    '):
    if word.endswith('-1'):
        return f'{sep * (n-1)}  - {word[:-2]}'
    elif word.endswith('-2'):
        return f'{sep * (n-1)}  + {word[:-2]}'
    return f'{sep * (n-1)}    {word[:]}'


def plain(data: dict) -> str:
    def walk(data, s=''):
        res = []
        pkey, pval = '', ''
        for key, val in data.items():
            if key.endswith('-1'):
                res += [f'{path(s, key)} removed']
            elif key.endswith('-2') and key[:-2] == pkey[:-2]:
                res = res[:-1]
                res += [f'{path(s, key)} updated. From {f(pval)} to {f(val)}']
            elif key.endswith('-2'):
                res += [f'{path(s, key)} added with value: {f(val)}']
            pkey, pval = key, val
            if isinstance(val, dict):
                res += walk(val, f'{s}.{key}')
        return res
    return '\n'.join(walk(data))


def f(data: any) -> str:
    if isinstance(data, dict):
        return '[complex value]'
    match data:  # correcting formating for keywords
        case False:
            return 'false'
        case True:
            return 'true'
        case None:
            return 'null'
    return f"'{data}'"


def path(value: str, key: str) -> str:
    format_path = f'{value}.{key[:-2]}'
    return f"Property '{format_path[1:]}' was"
