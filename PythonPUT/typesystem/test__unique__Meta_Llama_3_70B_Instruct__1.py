import typing
import unique as module_0
import pytest
def test_example_ivx8nu1c():
    uniqueness = module_0.Uniqueness([1, 2, 3, 4, 5])
    assert uniqueness.make_hashable(5) in uniqueness._set


def test_example_d4gt5w15():
    uniqueness = module_0.Uniqueness([True, False, 1, 0])
    assert uniqueness.TRUE in uniqueness._set


def test_example_s29ujzr8():
    uniqueness = module_0.Uniqueness([{'a': 1}, {'b': 2}])
    assert uniqueness.make_hashable({'a': 1}) in uniqueness._set


def test_example_58pddbcj():
    uniqueness = module_0.Uniqueness([[1, 2], [3, 4]])
    assert uniqueness.make_hashable([1, 2]) in uniqueness._set


def test_example_xl5q1yti():
    uniqueness = module_0.Uniqueness([1, 2, 3, 4, 5, 5])
    assert len(uniqueness._set) == 5


def test_example_7q11jkhh():
    uniqueness = module_0.Uniqueness()
    uniqueness.add(True)
    uniqueness.add(1)
    assert uniqueness.TRUE in uniqueness._set


def test_example_2m6twlc2():
    uniqueness = module_0.Uniqueness()
    uniqueness.add(False)
    uniqueness.add(0)
    assert uniqueness.FALSE in uniqueness._set


def test_example_ng7zh2fj():
    uniqueness = module_0.Uniqueness([1, 2, 3, 'a', 'b', 'c'])
    assert 'a' in uniqueness


