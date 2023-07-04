import pytest
from gendiff.engine import generate_diff


# def test_load_data():
#     with pytest.raises(FileNotFoundError):
#         data1, data2 = load_data('fil1.json', 'fil2.json')
path = 'tests/fixtures/'


@pytest.fixture
def txt():  # имя фикстуры выбирается произвольно
    with open(path + 'result_nested.txt', encoding='utf8') as file:
        return file.read()


def test_diff_nested(txt):
    assert generate_diff(path + 'file3.json', path + 'file4.json') == txt
    assert generate_diff(path + 'file3.yaml', path + 'file4.yaml') == txt
    assert generate_diff(path + 'file3.json', path + 'file4.yaml') == txt


def test_diff_nested_with_empty():
    with open(path + 'result_nested_empty.txt', encoding='utf8') as file:
        expected = file.read()
    assert generate_diff(path + 'file3.json', path + 'empty.json') == expected


def test_diff_nested_with_copy():
    with open(path + 'result_nested_copy.txt', encoding='utf8') as file:
        expected = file.read()
    assert generate_diff(path + 'file3.json', path + 'file3.json') == expected
