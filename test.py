import pytest
from app import add, subtract, multiply, divide

def test_add(a, b):
    assert add(1,2) == 3
    assert add(-1,1) == 0
    assert add(0,0) == 0
def test_subtract():
    assert subtract(5,3) == 2
    assert subtract(0,0) == 0
    assert subtract(-1,-1) == 0


@pytest.fixture
def sample_numbers():
    return (10, 5)

def test_divide_with_fixture(sample_numbers):
    num1, num2 = sample_numbers
    assert divide(num1, num2) == 2.0
    assert divide(num2, num1) == 0.5

@pytest.mark.parametrize("num1, num2, expected", [
    (10, 2, 5.0),
    (100, 10, 10.0),
    (1, 1, 1.0),
    (-6, 3, -2.0)
])
def test_divide_parametrized(num1, num2, expected):
    assert divide(num1, num2) == expected


def test_divide_by_zero_raises_error():
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(10, 0)