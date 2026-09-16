import pytest

def func(x):
    return x + 1

def test_func(x = 10):
    assert func(x) == x + 1

def test_sum():
    assert (0.1 + 0.2) == pytest.approx(0.3)

test_func()
