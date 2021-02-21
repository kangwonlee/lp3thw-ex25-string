import random
import urllib.request as ur
from typing import List

import pytest

import main

random.seed()


@pytest.fixture
def url():
    return 'https://www.mit.edu/~ecprice/wordlist.10000'


@pytest.fixture
def words(url, scope='session') -> List[bytes]:
    # https://docs/python.org/3/library/urllib.request.html
    with ur.urlopen(url) as req:
        txt_lines = req.readlines()
    return txt_lines


@pytest.fixture
def sample_string(words:List[str]) -> str:
    # https://docs/python.org/3/library/random.html
    min_words = 5
    max_words = 10
    assert len(words) >= min_words
    n = random.randint(min_words, min(max_words, len(words)))
    word_list = list(map(lambda w:w.decode().strip(), random.choices(words, k=n)))
    random.shuffle(word_list)
    return ' '.join(word_list)


def test_first_word_type(sample_string:str):
    result = main.first_word(sample_string)
    assert isinstance(result, str)


def test_first_word_result(sample_string:str):
    result = main.first_word(sample_string)
    assert sample_string.startswith(result)


def test_last_word_type(sample_string:str):
    result = main.last_word(sample_string)
    assert isinstance(result, str)


def test_last_word_result(sample_string:str):
    result = main.last_word(sample_string)
    assert sample_string.endswith(result)


if "__main__" == __name__:
    pytest.main()
