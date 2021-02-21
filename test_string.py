import main
import random
import pytest


random.seed()


@pytest.fixture
def sample_string():
    return random.randint(-100, 100), random.randint(-100, 100)


@pytest.fixture
def str_a_b():
    return chr(random.randint(ord('!'), ord('~'))), chr(random.randint(ord('!'), ord('~')))


def test_a_plus_twice_b_int_type(int_a_b):
    a, b = int_a_b

    result = main.a_plus_twice_b(a, b)

    assert isinstance(result, int), "반환된 결과값의 자료형을 확인하시오 Check the type of the return value"
    assert not ((result - a) // 2 - b), "함수의 반환값이 예상결과와 같은지 확인하시오 Verify the return value"


def test_a_plus_twice_b_str_type(str_a_b):
    a, b = str_a_b

    result = main.a_plus_twice_b(a, b)

    assert isinstance(result, str), "반환된 결과값의 자료형을 확인하시오 Check the type of the return value"
    assert not ((len(result) - len(a))//2 - len(b)), "함수의 반환값이 예상결과와 같은지 확인하시오 Verify the return value"
    assert a == result[0], "함수의 반환값이 예상결과와 같은지 확인하시오 Verify the return value"
    assert b == result[-1], "함수의 반환값이 예상결과와 같은지 확인하시오 Verify the return value"
    assert b == result[-2], "함수의 반환값이 예상결과와 같은지 확인하시오 Verify the return value"
