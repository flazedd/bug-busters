import pytest
import unique as module_0
import typing
def test_example_ccmr9m8j():
    uniqueness = module_0.Uniqueness([1, True, 'hello', [1, 2, 3], {'a': 1, 'b': 2}])
    uniqueness.add(True)
    assert True in uniqueness


def test_example_g9v3hv13():
    uniqueness = module_0.Uniqueness([1, 'hello', [1, 2, 3], {'a': 1, 'b': 2}])
    assert False not in uniqueness


def test_example_409dk3jb():
    uniqueness = module_0.Uniqueness([1, 2, 3, 4, 5])
    uniqueness.add(1)
    assert 1 in uniqueness


def test_example_wpxqi7ss():
    uniqueness = module_0.Uniqueness([{'a': 1, 'b': 2}, {'c': 3, 'd': 4}])
    uniqueness.add({'a': 1, 'b': 2})
    assert {'a': 1, 'b': 2} in uniqueness


def test_example_emqqoa6q():
    uniqueness = module_0.Uniqueness([1, 2, 3])
    assert [1, 2, 3] not in uniqueness


def test_example_dn6e0l77():
    uniqueness = module_0.Uniqueness([1, 2, 3])
    uniqueness.add([1, 2, 3])
    assert [1, 2, 3] in uniqueness and 1 in uniqueness


def test_example_ciyhtnb1():
    uniqueness = module_0.Uniqueness([{'a': 1, 'b': 2}, {'c': 3, 'd': 4}])
    uniqueness.add({'e': 5, 'f': 6})
    assert len(uniqueness._set) == 3


def test_example_q9fvxo5l():
    uniqueness = module_0.Uniqueness([1, 2, 3])
    uniqueness.add(None)
    assert None in uniqueness


