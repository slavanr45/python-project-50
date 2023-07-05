from gendiff.engine import generate_diff
from gendiff.parsing import read_data


path = 'tests/fixtures/'


def test_diff_nested():
    expected = read_data(path + 'result_nested.txt')
    assert generate_diff(path + 'file3.json', path + 'file4.json') == expected
    assert generate_diff(path + 'file3.yaml', path + 'file4.yaml') == expected
    assert generate_diff(path + 'file3.json', path + 'file4.yaml') == expected


def test_diff_nested_with_empty():
    expected = read_data(path + 'result_nested_empty.txt')
    assert generate_diff(path + 'file3.json', path + 'empty.json') == expected


def test_diff_nested_with_copy():
    expected = read_data(path + 'result_nested_copy.txt')
    assert generate_diff(path + 'file3.json', path + 'file3.json') == expected
