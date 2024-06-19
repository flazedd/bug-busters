import pytest
import unique as module_0
import typing
def test_example_b80g267f():
    u = module_0.Uniqueness([1, 2, 3, True, False, 'hello', [1, 2], {'a': 1, 'b': 2}])
    assert len(u._set) == 8


def test_example_aeqflqwg():
    u = module_0.Uniqueness([1, 2, 2, True, True, 'hello', 'hello', [1, 2], [1, 2], {'a': 1, 'b': 2}, {'a': 1, 'b': 2}])
    assert len(u._set) == 6


def test_example_zaf1pgm6():
    u = module_0.Uniqueness([None, None, [1, 2, 3], [1, 2, 3], {'a': 1, 'b': 2}, {'a': 1, 'b': 2}])
    assert len(u._set) == 3


def test_example_n6i70exr():
    u = module_0.Uniqueness([1, 2, 3, True, False, 'hello', [1, 2], {'a': 1, 'b': 2}, 1, 2, 3, True, False, 'hello', [1, 2], {'a': 1, 'b': 2}])
    assert len(u._set) == 8


def test_example_vfk950gd():
    u = module_0.Uniqueness([1.0, 1, '1', [1], {'a': 1}, 2.0, 2, '2', [2], {'a': 2}, 1.0, 1, '1', [1], {'a': 1}])
    assert len(u._set) == 8


def test_example_1h0yeio1():
    u = module_0.Uniqueness([{'a': 1, 'b': 2}, {'b': 2, 'a': 1}, {'a': 1, 'c': 2}, {'c': 2, 'a': 1}, {'a': 1, 'b': 2}, {'b': 2, 'a': 1}, {'a': 2, 'b': 1}, {'b': 1, 'a': 2}, {'a': 1, 'b': 2}, {'b': 2, 'a': 1}])
    assert len(u._set) == 6


def test_example_c1w0nnc8():
    u = module_0.Uniqueness([1, 1.0, '1', [1], {'a': 1}, 2, 2.0, '2', [2], {'a': 2}, 1, 1.0, '1', [1], {'a': 1}, 3, 3.0, '3', [3], {'a': 3}])
    assert len(u._set) == 12


def test_example_ylzukhnd():
    u = module_0.Uniqueness([{'a': 1, 'b': 2}, {'a': 2, 'b': 1}, {'a': 1, 'b': 2, 'c': 3}, {'a': 2, 'b': 1, 'c': 3}, {'a': 1, 'b': 2}, {'a': 2, 'b': 1}])
    assert len(u._set) == 4


