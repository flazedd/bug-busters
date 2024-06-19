import pytest
import typing
import unique as module_0
def test_example_hmzufwn1():
    uniqueness = module_0.Uniqueness([1, 2, 3, True, False, 'a', 'b', [1, 2], [3, 4], {'a': 1}, {'b': 2}])
    assert True in uniqueness


def test_example_16wy5sa8():
    uniqueness = module_0.Uniqueness([1, 2, 3, 'a', 'b', [1, 2], [3, 4], {'a': 1}, {'b': 2}])
    uniqueness.add(False)
    assert False in uniqueness


def test_example_0qnd1trj():
    uniqueness = module_0.Uniqueness([1, 2, 3, 'a', 'b', [1, 2], [3, 4], {'a': 1}, {'b': 2}])
    uniqueness.add({'c': 3})
    assert {'c': 3} in uniqueness


def test_example_dklgq86h():
    uniqueness = module_0.Uniqueness([1, 2, 3, 'a', 'b', [1, 2], [3, 4], {'a': 1}, {'b': 2}])
    uniqueness.add([4, 5])
    assert [4, 5] in uniqueness


def test_example_o8r48ivj():
    uniqueness = module_0.Uniqueness([1, 2, 3, 'a', 'b', [1, 2], [3, 4], {'a': 1}, {'b': 2}])
    uniqueness.add(1)
    assert 1 in uniqueness


def test_example_waysu2pi():
    uniqueness = module_0.Uniqueness()
    uniqueness.add(1)
    uniqueness.add(True)
    uniqueness.add([1, 2])
    uniqueness.add({'a': 1})
    assert len(uniqueness._set) == 4


def test_example_lm7upm6j():
    uniqueness = module_0.Uniqueness([1, 2, 3, 'a', 'b', [1, 2], [3, 4], {'a': 1}, {'b': 2}])
    assert [1, 2] in uniqueness


def test_example_l31wzrgh():
    uniqueness = module_0.Uniqueness([1, 2, 3, 'a', 'b', [1, 2], [3, 4], {'a': 1}, {'b': 2}])
    assert not [4, 5] in uniqueness


