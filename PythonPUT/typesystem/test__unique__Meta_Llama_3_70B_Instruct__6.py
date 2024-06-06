import typing
import unique as module_0
import pytest
def test_example_poccuaxt():
    unique = module_0.Uniqueness([True, 1, False, 0, [1, 2], [1, 2]])
    assert True in unique and 1 in unique and (False in unique) and (0 in unique) and ([1, 2] in unique)


def test_example_0hs9id3q():
    unique = module_0.Uniqueness([{'a': 1}, {'a': 1}, {'b': 2}])
    assert {'a': 1} in unique and {'b': 2} in unique


def test_example_q385k959():
    unique = module_0.Uniqueness([True, False, True, False])
    assert unique.__contains__(True) and unique.__contains__(False)


def test_example_0sajig6d():
    unique = module_0.Uniqueness([1, 2, 3, 2, 1])
    assert 1 in unique and 2 in unique and (3 in unique)


def test_example_i5jkgp94():
    unique = module_0.Uniqueness([{1: 'a'}, {1: 'a'}, {2: 'b'}])
    assert {1: 'a'} in unique and {2: 'b'} in unique


def test_example_t24z9fdn():
    unique = module_0.Uniqueness([None, None, 1, 1])
    assert None in unique and 1 in unique


def test_example_e4q7e2aj():
    unique = module_0.Uniqueness([[1, 2], [1, 2], [3, 4]])
    assert [1, 2] in unique and [3, 4] in unique


def test_example_zeivwj7v():
    unique = module_0.Uniqueness(['a', 'b', 'a', 'c'])
    assert 'a' in unique and 'b' in unique and ('c' in unique)


