from typing import Callable
import pytest
from typing import Optional
from typing import TypeVar
from typing import Generic
import immutable_list as module_0
def test_example_nrrslxbb():
    assert module_0.ImmutableList.of(1, 2, 3).to_list() == [1, 2, 3]


def test_example_zo86ee46():
    immutable_list = module_0.ImmutableList.of(1, 2, 3)
    new_list = immutable_list.append(4)
    assert new_list.to_list() == [1, 2, 3, 4]


def test_example_da271qa2():
    immutable_list = module_0.ImmutableList.of(1, 2, 3)
    mapped_list = immutable_list.map(lambda x: x * 2)
    assert mapped_list.to_list() == [2, 4, 6]


def test_example_b8yjm3jf():
    immutable_list = module_0.ImmutableList.of(1, 2, 3)
    reduced_value = immutable_list.reduce(lambda acc, x: acc + x, 0)
    assert reduced_value == 6


def test_example_lhxbl1fv():
    immutable_list = module_0.ImmutableList.of(1, 2, 3)
    unshifted_list = immutable_list.unshift(0)
    assert unshifted_list.to_list() == [0, 1, 2, 3]


def test_example_o1p4fuqf():
    immutable_list = module_0.ImmutableList.of(1, 2, 3)
    found_element = immutable_list.find(lambda x: x > 2)
    assert found_element == 3


def test_example_muct0hiv():
    immutable_list = module_0.ImmutableList.empty()
    assert len(immutable_list) == 0


def test_example_11z2g56a():
    immutable_list1 = module_0.ImmutableList.of(1, 2, 3)
    immutable_list2 = module_0.ImmutableList.of(1, 2, 3)
    assert immutable_list1 == immutable_list2


