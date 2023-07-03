import pytest
from gendiff.engine import generate_diff, check_diff
from gendiff.parsing import parse_data

# def test_load_data():
#     with pytest.raises(FileNotFoundError):
#         data1, data2 = load_data('fil1.json', 'fil2.json')
path = 'tests/fixtures/'


@pytest.fixture
def txt():  # имя фикстуры выбирается произвольно
    with open(path + 'result.txt', encoding='utf8') as file:
        return file.read()


# unit test
def test_json_parse(txt):
    data1 = parse_data(path + 'file1.json')
    data2 = parse_data(path + 'file2.json')
    assert data1
    assert data2
    assert check_diff(data1, data2) == txt


def test_yaml_parse(txt):
    data1 = parse_data(path + 'file1.yaml')
    data2 = parse_data(path + 'file2.yaml')
    assert data1
    assert data2
    assert check_diff(data1, data2) == txt


# integrity test
def test_diff(txt):
    assert generate_diff(path + 'file1.json', path + 'file2.json') == txt
    assert generate_diff(path + 'file1.yaml', path + 'file2.yaml') == txt
    assert generate_diff(path + 'file1.json', path + 'file2.yaml') == txt


def test_diff_with_empty():
    with open(path + 'result_empty.txt', encoding='utf8') as file:
        expected = file.read()
    assert generate_diff(path + 'file1.json', path + 'file3.json') == expected


def test_diff_with_copy():
    with open(path + 'result_copy.txt', encoding='utf8') as file:
        expected = file.read()
    assert generate_diff(path + 'file1.json', path + 'file1.json') == expected
