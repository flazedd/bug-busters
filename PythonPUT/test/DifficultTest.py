# DifficultTest.py
from PythonPUT.src.Difficult import Difficult

def test_calculate_positive():
    difficult = Difficult()
    assert difficult.calculate(5, [3, 2, 1, 5, 4]) == 15

def test_calculate_positive_reverse():
    difficult = Difficult()
    assert difficult.calculate(5, [3, 2, 1, 5, 4], reverse=True) == 15

def test_calculate_positive_square():
    difficult = Difficult()
    assert difficult.calculate(5, [3, 2, 1, 5, 4], square=True) == 55

def test_calculate_positive_reverse_square():
    difficult = Difficult()
    assert difficult.calculate(5, [3, 2, 1, 5, 4], reverse=True, square=True) == 55

def test_calculate_positive_multiply():
    difficult = Difficult()
    assert difficult.calculate(5, [3, 2, 1, 5, 4], multiply=3) == 90

def test_calculate_positive_reverse_square_multiply():
    difficult = Difficult()
    assert difficult.calculate(5, [3, 2, 1, 5, 4], reverse=True, square=True, multiply=3) == 165
