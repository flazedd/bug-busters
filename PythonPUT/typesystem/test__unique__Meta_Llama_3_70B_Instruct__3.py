import pytest
import typing
import unique as module_0
def test_uniqueness_1ayybtv6():
    uniqueness = module_0.Uniqueness([1, True, 'a', 1, True, 'a'])
    assert len(uniqueness._set) == 3


def test_uniqueness_dicts_otfk69ip():
    uniqueness = module_0.Uniqueness([1, {'a': 1}, {'a': 1}, {'b': 1}])
    assert len(uniqueness._set) == 3


def test_uniqueness_mixed_zj78exv7():
    uniqueness = module_0.Uniqueness([1, True, 'a', 1, True, 'a', {'b': 1}, {'b': 1}, [1, 2], [1, 2]])
    assert len(uniqueness._set) == 5


def test_uniqueness_nested_lists_agctmujr():
    uniqueness = module_0.Uniqueness([1, [1, 2], [1, [2, 3]], [1, [2, 3]]])
    assert len(uniqueness._set) == 3


def test_uniqueness_nested_dicts_e4d3izfb():
    uniqueness = module_0.Uniqueness([1, {'a': 1}, {'a': {'b': 1}}, {'a': {'b': 1}}])
    assert len(uniqueness._set) == 3


def test_uniqueness_none_mjkqjjs9():
    uniqueness = module_0.Uniqueness([1, None, 1, None, 'a', 'a'])
    assert len(uniqueness._set) == 3


def test_uniqueness_bools_kzbkev3b():
    uniqueness = module_0.Uniqueness([True, False, True, False, 1, 0])
    assert len(uniqueness._set) == 4


def test_uniqueness_mixed_empty_hmih25dw():
    uniqueness = module_0.Uniqueness([1, [], {}, True, False, None, 'a', 'a'])
    assert len(uniqueness._set) == 7


