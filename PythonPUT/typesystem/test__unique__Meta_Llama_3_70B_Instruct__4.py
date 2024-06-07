import unique as module_0
import typing
import pytest
def test_example_5c4iht54():
    uniqueness = module_0.Uniqueness()
    uniqueness.add(True)
    uniqueness.add(1)
    uniqueness.add(False)
    uniqueness.add(0)
    assert len(uniqueness._set) == 4


def test_example_qihz7bu4():
    uniqueness = module_0.Uniqueness()
    uniqueness.add([1, 2, 3])
    uniqueness.add([1, 2, 3])
    uniqueness.add([1, 2, 4])
    assert len(uniqueness._set) == 2


def test_example_9mimst4v():
    uniqueness = module_0.Uniqueness()
    uniqueness.add({'a': 1, 'b': 2})
    uniqueness.add({'a': 1, 'b': 2})
    uniqueness.add({'a': 1, 'c': 2})
    assert len(uniqueness._set) == 2


def test_example_f643o6c4():
    uniqueness = module_0.Uniqueness()
    uniqueness.add(None)
    uniqueness.add(None)
    assert len(uniqueness._set) == 1


def test_example_klgb0pa1():
    uniqueness = module_0.Uniqueness()
    uniqueness.add(1)
    uniqueness.add(1.0)
    assert len(uniqueness._set) == 1


def test_example_z6wvpkmo():
    uniqueness = module_0.Uniqueness()
    uniqueness.add('hello')
    uniqueness.add('hello')
    assert len(uniqueness._set) == 1


def test_example_78wrb9u5():
    uniqueness = module_0.Uniqueness([1, 2, 3, 2, 1])
    assert len(uniqueness._set) == 3


def test_example_b5ed156n():
    uniqueness = module_0.Uniqueness()
    uniqueness.add([1, 2, 3])
    assert [1, 2, 3] in uniqueness


