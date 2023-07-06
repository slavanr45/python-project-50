from gendiff.engine import generate_diff, read_data
import os


def get_path(file_name):
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, 'fixtures', file_name)


def test_diff():
    expected = read_data(get_path('result.txt'))
    assert generate_diff(get_path('file1.json'),
                         get_path('file2.json')) == expected
    assert generate_diff(get_path('file1.yaml'),
                         get_path('file2.yaml')) == expected
    assert generate_diff(get_path('file1.json'),
                         get_path('file2.yaml')) == expected


def test_diff_with_empty():
    expected = read_data(get_path('result_empty.txt'))
    assert generate_diff(get_path('file1.json'),
                         get_path('empty.json')) == expected


def test_diff_with_copy():
    expected = read_data(get_path('result_copy.txt'))
    assert generate_diff(get_path('file1.json'),
                         get_path('file1.json')) == expected


def test_diff_nested():
    expected = read_data(get_path('result_nested.txt'))
    assert generate_diff(get_path('file3.json'),
                         get_path('file4.json')) == expected
    assert generate_diff(get_path('file3.yaml'),
                         get_path('file4.yaml')) == expected
    assert generate_diff(get_path('file3.json'),
                         get_path('file4.yaml')) == expected


def test_diff_nested_with_empty():
    expected = read_data(get_path('result_nested_empty.txt'))
    assert generate_diff(get_path('file3.json'),
                         get_path('empty.json')) == expected


def test_diff_nested_with_copy():
    expected = read_data(get_path('result_nested_copy.txt'))
    assert generate_diff(get_path('file3.json'),
                         get_path('file3.json')) == expected


def test_diff_plain():
    expected = read_data(get_path('result_plain.txt'))
    assert generate_diff(get_path('file3.json'),
                         get_path('file4.json'), 'plain') == expected
    assert generate_diff(get_path('file3.yaml'),
                         get_path('file4.yaml'), 'plain') == expected
    assert generate_diff(get_path('file3.json'),
                         get_path('file4.yaml'), 'plain') == expected


def test_diff_json():
    expected = read_data(get_path('result_json.txt'))
    assert generate_diff(get_path('file1.json'),
                         get_path('file2.json'), 'json') == expected
