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


def make_diff(data1: dict, data2: dict) -> dict:
    result = {}
    for key in sorted(data1 | data2):
        a = data1.get(key, 9999)
        b = data2.get(key, 9999)
        if isinstance(a, dict) and isinstance(b, dict):
            result[key] = make_diff(a, b)
        else:
            if a == b:
                result[key] = a
            else:
                if a != 9999:
                    result[key+'-1'] = a
                if b != 9999:
                    result[key+'-2'] = b
    return result
