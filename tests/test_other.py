from gendiff.engine import generate_diff
from gendiff.parsing import read_data


path = 'tests/fixtures/'


def test_diff_plain():
    expected = read_data(path + 'result_plain.txt')
    assert generate_diff(path + 'file3.json', path + 'file4.json', 'plain') == expected
    assert generate_diff(path + 'file3.yaml', path + 'file4.yaml', 'plain') == expected
    assert generate_diff(path + 'file3.json', path + 'file4.yaml', 'plain') == expected
