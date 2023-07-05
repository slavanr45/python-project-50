from gendiff.engine import generate_diff, read_data


path = 'tests/fixtures/'


def test_diff():
    expected = read_data(path + 'result.txt')
    assert generate_diff(path + 'file1.json', path + 'file2.json') == expected
    assert generate_diff(path + 'file1.yaml', path + 'file2.yaml') == expected
    assert generate_diff(path + 'file1.json', path + 'file2.yaml') == expected


def test_diff_with_empty():
    expected = read_data(path + 'result_empty.txt')
    assert generate_diff(path + 'file1.json', path + 'empty.json') == expected


def test_diff_with_copy():
    expected = read_data(path + 'result_copy.txt')
    assert generate_diff(path + 'file1.json', path + 'file1.json') == expected
