from gendiff.parsing import read_data, check_diff, stylish


def generate_diff(filename1: str, filename2: str):
    data1 = read_data(filename1)
    data2 = read_data(filename2)
    data_prepared = check_diff(data1, data2)
    # print(data_prepared)
    # print(list(stylish(data_prepared)))
    # print()
    # path = 'tests/fixtures/'
    # with open(path + 'result_nested.txt', encoding='utf8') as file:
    #     print(list(file.read()))
    return stylish(data_prepared)
