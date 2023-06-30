import pytest
from gendiff.engine import generate_diff, json_diff, json_load


# def test_load_data():
#     with pytest.raises(FileNotFoundError):
#         data1, data2 = load_data('fil1.json', 'fil2.json')
path = 'tests/fixtures/'


@pytest.fixture
def txt():  # имя фикстуры выбирается произвольно
    with open(path + 'result.txt', encoding='utf8') as file:
        data = file.read()
    return data


# unit test
def test_json_load(txt):
    data1 = json_load(path + 'file1.json')
    data2 = json_load(path + 'file2.json')
    assert data1
    assert data2
    assert json_diff(data1, data2) == txt


# integrity test
def test_json_diff(txt):
    assert generate_diff(path + 'file1.json', path + 'file2.json') == txt
