import pytest

from calculator import AdvancedCalculator

calc = AdvancedCalculator()

def test_factorial_zero():
    assert calc.factorial(0) == 1

def test_factorial_positive():
    assert calc.factorial(5) == 120

def test_factorial_negative():
    with pytest.raises(ValueError):
        calc.factorial(-1)

def test_exponential():
    assert calc.exponential(2, 3) == 8
    assert calc.exponential(9, 0.5) == 3

def test_sums_various():
    assert calc.sums(1, 2, 3, 4) == 10
    assert calc.sums([10, 20]) == 30
