import pytest
import unique as module_0
import typing
def test_example_j625c8lu():
    uniqueness_instance = module_0.Uniqueness()
    uniqueness_instance.add(True)
    uniqueness_instance.add(1)
    uniqueness_instance.add(False)
    uniqueness_instance.add(0)
    assert len(uniqueness_instance._set) == 4


def test_example_3h8p47lb():
    uniqueness_instance = module_0.Uniqueness()
    uniqueness_instance.add([1, 2, 3])
    uniqueness_instance.add([1, 2, 3])
    uniqueness_instance.add([4, 5, 6])
    assert len(uniqueness_instance._set) == 2


def test_example_gw2lbelm():
    uniqueness_instance = module_0.Uniqueness()
    uniqueness_instance.add({'a': 1, 'b': 2})
    uniqueness_instance.add({'a': 1, 'b': 2})
    uniqueness_instance.add({'c': 3, 'd': 4})
    assert len(uniqueness_instance._set) == 2


def test_example_u95c4m7e():
    uniqueness_instance = module_0.Uniqueness([True, False, 1, 0])
    assert len(uniqueness_instance._set) == 4


def test_example_7j80rpa3():
    uniqueness_instance = module_0.Uniqueness()
    uniqueness_instance.add(None)
    uniqueness_instance.add(None)
    assert len(uniqueness_instance._set) == 1


def test_example_5jmgv8w8():
    uniqueness_instance = module_0.Uniqueness()
    uniqueness_instance.add([1, 2, 3])
    uniqueness_instance.add([3, 2, 1])
    assert len(uniqueness_instance._set) == 2


def test_example_e9t3bdor():
    uniqueness_instance = module_0.Uniqueness()
    uniqueness_instance.add({'a': 1, 'b': 2})
    uniqueness_instance.add({'b': 2, 'a': 1})
    assert uniqueness_instance.make_hashable({'a': 1, 'b': 2}) in uniqueness_instance._set


def test_example_5ehtkzqb():
    uniqueness_instance = module_0.Uniqueness([1, 2, 3, 2, 1])
    assert len(uniqueness_instance._set) == 3


