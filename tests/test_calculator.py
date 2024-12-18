import pytest
from calculator import add, subtract, divide, multiply

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(2, 1) == 1
    assert subtract(2, 2) == 0
    assert subtract(2, 3) == -1

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(-2, -3) == 6

def test_divide():
    assert divide(6, 3) == 2
    assert divide(-6, 2) == -3
    assert divide(-6, -2) == 3
    with pytest.raises(ValueError):
        divide(6, 0)