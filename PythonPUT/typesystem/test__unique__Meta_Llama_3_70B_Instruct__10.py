import pytest
import unique as module_0
import typing
def test_example_04w90910():
    uniqueness = module_0.Uniqueness([True, 1, False, 0, [1, 2], [1, 2], {'a': 1}, {'a': 1}])
    assert len(uniqueness._set) == 6


def test_example_k7hq6xqh():
    uniqueness = module_0.Uniqueness([1, 2, 3, 1, 2, 3, 'a', 'b', 'a'])
    assert len(uniqueness._set) == 5


def test_example_8y512vpz():
    uniqueness = module_0.Uniqueness([None, None, [1, 2, 3], [1, 2, 3], {'a': 1, 'b': 2}, {'a': 1, 'b': 2}])
    assert len(uniqueness._set) == 3


def test_example_vflifs7a():
    uniqueness = module_0.Uniqueness([True, False, 1, 0, 'True', 'False'])
    assert len(uniqueness._set) == 6


def test_example_pb4r1hyv():
    uniqueness = module_0.Uniqueness([{'a': 1, 'b': 2}, {'b': 2, 'a': 1}, {'a': 1, 'c': 2}, {'a': 1, 'c': 2}])
    assert len(uniqueness._set) == 3


def test_example_56xmih2c():
    uniqueness = module_0.Uniqueness([[1, 2], [2, 1], [1, 2, 3], [1, 2, 3]])
    assert len(uniqueness._set) == 3


def test_example_wdja25uu():
    uniqueness = module_0.Uniqueness([1, '1', 2, '2', 1, '1'])
    assert len(uniqueness._set) == 4


def test_example_0a0p7lq5():
    uniqueness = module_0.Uniqueness([1, 2, 3, 1, 2, 3, {'a': 1, 'b': 2}, {'a': 1, 'b': 2}, {'b': 2, 'a': 1}])
    assert len(uniqueness._set) == 5


