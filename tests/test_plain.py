import pytest
from gendiff.engine import generate_diff


# def test_load_data():
#     with pytest.raises(FileNotFoundError):
#         data1, data2 = load_data('fil1.json', 'fil2.json')
path = 'tests/fixtures/'


@pytest.fixture
def txt():  # имя фикстуры выбирается произвольно
    with open(path + 'result_plain.txt', encoding='utf8') as file:
        return file.read()


def test_diff_plain(txt):
    assert generate_diff(path + 'file1.json', path + 'file2.json') == txt
    assert generate_diff(path + 'file1.yaml', path + 'file2.yaml') == txt
    assert generate_diff(path + 'file1.json', path + 'file2.yaml') == txt


def test_diff_plain_with_empty():
    with open(path + 'result_plain_empty.txt', encoding='utf8') as file:
        expected = file.read()
    assert generate_diff(path + 'file1.json', path + 'empty.json') == expected


def test_diff_plain_with_copy():
    with open(path + 'result_plain_copy.txt', encoding='utf8') as file:
        expected = file.read()
    assert generate_diff(path + 'file1.json', path + 'file1.json') == expected
