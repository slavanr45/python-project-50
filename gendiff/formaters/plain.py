def to_plain(data: dict) -> str:
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
