from gendiff.parsing import parse_data


def generate_diff(filename1: str, filename2: str):
    data1 = parse_data(filename1)
    data2 = parse_data(filename2)
    return check_diff(data1, data2)


def check_diff(data1: dict, data2: dict) -> str:
    result = '{\n'
    for key in sorted(data1 | data2):
        a = data1.get(key, None)
        b = data2.get(key, None)
        if a == b:
            result += f'    {key}: {data1[key]}\n'
        else:
            if a is not None:
                result += f'  - {key}: {data1[key]}\n'
            if b is not None:
                result += f'  + {key}: {data2[key]}\n'
    return result + '}'
