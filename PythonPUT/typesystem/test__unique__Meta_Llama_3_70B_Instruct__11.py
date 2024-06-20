import pytest
import unique as module_0
import typing
def test_example_sliz4rig():
    uniqueness = module_0.Uniqueness([True, 1, False, 0])
    assert True in uniqueness and 1 in uniqueness and (False in uniqueness) and (0 in uniqueness)


def test_example_lmd8h612():
    uniqueness = module_0.Uniqueness([1, 2, 3, 2, 1])
    assert len(uniqueness._set) == 3


def test_example_uj47gg6d():
    uniqueness = module_0.Uniqueness([{'a': 1}, {'b': 2}, {'a': 1}])
    assert len(uniqueness._set) == 2


def test_example_4akofq5c():
    uniqueness = module_0.Uniqueness([[1, 2], [2, 3], [1, 2]])
    assert len(uniqueness._set) == 2


def test_example_waexmtok():
    uniqueness = module_0.Uniqueness([None, None, 'a', 'a'])
    assert len(uniqueness._set) == 2


def test_example_3s0z56uq():
    uniqueness = module_0.Uniqueness([{'a': 1}, {'a': 1, 'b': 2}, {'a': 1}])
    assert len(uniqueness._set) == 2


def test_example_py8am31v():
    uniqueness = module_0.Uniqueness([])
    assert len(uniqueness._set) == 0


def test_example_6nt6vu05():
    uniqueness = module_0.Uniqueness([1, 2, 3])
    uniqueness.add(4)
    assert len(uniqueness._set) == 4


