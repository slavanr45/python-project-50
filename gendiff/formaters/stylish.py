def to_stylish(data: dict, level=1) -> str:
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
        result += (f'{make_indent(key, level)}: {to_stylish(val, level+1)}\n')
    return result + ('    ' * (level - 1) + '}')  # add tail


def make_indent(word, n, sep='    '):
    if word.endswith('-1'):
        return f'{sep * (n-1)}  - {word[:-2]}'
    elif word.endswith('-2'):
        return f'{sep * (n-1)}  + {word[:-2]}'
    else:
        return f'{sep * (n-1)}    {word[:]}'
