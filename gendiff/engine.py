import json


def generate_diff(first, second):
    with open(first, encoding='utf8') as file1:
        data1 = json.load(file1)
    with open(second, encoding='utf8') as file2:
        data2 = json.load(file2)
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
