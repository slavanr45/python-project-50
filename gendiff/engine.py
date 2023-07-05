from gendiff.parsing import read_data, check_diff, stylish, plain


def generate_diff(file_path1: str, file_path2: str, format_name='stylish') -> str:
    data1 = read_data(file_path1)
    data2 = read_data(file_path2)
    data_prepared = check_diff(data1, data2)
    # print(data_prepared)
    # print(list(stylish(data_prepared)))
    # print()
    # path = 'tests/fixtures/'
    # with open(path + 'result_nested.txt', encoding='utf8') as file:
    #     print(list(file.read()))
    if format_name == 'stylish':
        return stylish(data_prepared)
    elif format_name == 'plain':
        return plain(data_prepared)
