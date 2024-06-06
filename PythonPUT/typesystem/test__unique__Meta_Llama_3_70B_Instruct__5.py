import unique as module_0
import pytest
import typing
def test_example_wdwrb6ft():
    uniqueness = module_0.Uniqueness([1, 2, 3, True, False, [1, 2], [3, 4]])
    assert True in uniqueness


def test_example_07kyxznq():
    uniqueness = module_0.Uniqueness([1, 2, 3, {'a': 1}, {'b': 2}, {'a': 1}])
    assert {'a': 1} in uniqueness


def test_example_v3oykukn():
    uniqueness = module_0.Uniqueness([1, 2, 3, [1, 2], [1, 2], [3, 4]])
    assert [1, 2] in uniqueness


def test_example_47f95lri():
    uniqueness = module_0.Uniqueness([1, 2, 3, False, 0, 'hello', 'hello'])
    assert 'hello' in uniqueness


def test_example_p6h5ugp3():
    uniqueness = module_0.Uniqueness([1, 2, 3, {'a': 1, 'b': 2}, {'a': 1, 'b': 2}, {'a': 1, 'c': 2}])
    assert {'a': 1, 'b': 2} in uniqueness


def test_example_dkmd4k3i():
    uniqueness = module_0.Uniqueness([1, 2, 3, None, None])
    assert None in uniqueness


def test_example_19ifj6ap():
    uniqueness = module_0.Uniqueness([1, 2, 3, [4, 5], [4, 5], [6, 7]])
    assert [4, 5] in uniqueness


def test_example_75hj3wlf():
    uniqueness = module_0.Uniqueness([1, 2, 3, {'a': 1, 'b': 2, 'c': 3}, {'a': 1, 'b': 2, 'c': 3}, {'a': 1, 'b': 2, 'd': 3}])
    assert {'a': 1, 'b': 2, 'c': 3} in uniqueness


