import pytest
import typing
import unique as module_0
def test_example_so99dzx2():
    uniqueness = module_0.Uniqueness([1, 2, 3, True, False, 'hello', [1, 2], {'a': 1, 'b': 2}])
    assert True in uniqueness


def test_example_xk3gitv4():
    uniqueness = module_0.Uniqueness([1, 2, 3, True, False, 'hello', [1, 2], {'a': 1, 'b': 2}])
    uniqueness.add([4, 5])
    assert [4, 5] in uniqueness


def test_example_6x7g23we():
    uniqueness = module_0.Uniqueness([1, 2, 3, True, False, 'hello', {'a': 1, 'b': 2}])
    uniqueness.add({'c': 3, 'd': 4})
    assert {'c': 3, 'd': 4} in uniqueness


def test_example_w0mpdra6():
    uniqueness = module_0.Uniqueness([1, 2, 3, True, False, 'hello'])
    uniqueness.add(1)
    assert len(uniqueness._set) == 6


def test_example_l4oi9rvn():
    uniqueness = module_0.Uniqueness([1, 2, 3, True, False, 'hello'])
    uniqueness.add(None)
    assert None in uniqueness


def test_example_btb2o1yy():
    uniqueness = module_0.Uniqueness([1, 2, 3, True, False, 'hello'])
    uniqueness.add([1, 2, 3])
    uniqueness.add([1, 2, 3])
    assert len(uniqueness._set) == 7


def test_example_649ftkl7():
    uniqueness = module_0.Uniqueness([1, 2, 3, True, False, 'hello'])
    uniqueness.add({'a': 1, 'b': 2})
    uniqueness.add({'a': 1, 'b': 2})
    assert len(uniqueness._set) == 7


def test_example_phm52pkz():
    uniqueness = module_0.Uniqueness([1, 2, 3, True, False, 'hello'])
    uniqueness.add([4, 5, 6])
    uniqueness.add([4, 5, 6, 7])
    assert [4, 5, 6, 7] in uniqueness


