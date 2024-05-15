# test_difficult.py
from difficult import Difficult

def test_calculate():
    difficult = Difficult()

    # Test case 1: Normal calculation
    assert difficult.calculate(5, [1, 2, 3, 4, 5]) == 18

    # Test case 2: With reverse=True
    assert difficult.calculate(5, [1, 2, 3, 4, 5], reverse=True) == 18

    # Test case 3: With square=True
    assert difficult.calculate(5, [1, 2, 3, 4, 5], square=True) == 70

    # Test case 4: With multiply=3
    assert difficult.calculate(5, [1, 2, 3, 4, 5], multiply=3) == 54

    # Test case 5: With all parameters
    assert difficult.calculate(5, [1, 2, 3, 4, 5], reverse=True, square=True, multiply=3) == 210
