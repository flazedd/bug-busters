from typing import Callable
import pytest
from typing import TypeVar
from typing import Generic
import immutable_list as module_0
from typing import Optional
def test_example_lg7sqsf1():
    lst = module_0.ImmutableList.of(1, 2, 3)
    mapped_lst = lst.map(lambda x: x * 2)
    assert mapped_lst.to_list() == [2, 4, 6]


def test_example_4900pgkr():
    lst = module_0.ImmutableList.of(1, 2, 3, 4, 5)
    reduced_value = lst.reduce(lambda acc, x: acc + x, 0)
    assert reduced_value == 15


def test_example_rmlj69su():
    lst = module_0.ImmutableList.of(1, 2, 3, 4, 5)
    found_element = lst.find(lambda x: x > 3)
    assert found_element == 4


def test_example_wl1avmup():
    lst = module_0.ImmutableList.of(1, 2, 3)
    appended_lst = lst.append(4)
    assert appended_lst.to_list() == [1, 2, 3, 4]


def test_example_fm937t2s():
    lst = module_0.ImmutableList.of(1, 2, 3)
    unshifted_lst = lst.unshift(0)
    assert unshifted_lst.to_list() == [0, 1, 2, 3]


def test_example_j6hej7g4():
    lst = module_0.ImmutableList.of(1, 2, 3)
    len_lst = len(lst)
    assert len_lst == 3


def test_example_at0v3i8k():
    lst1 = module_0.ImmutableList.of(1, 2, 3)
    lst2 = module_0.ImmutableList.of(1, 2, 3)
    assert lst1 == lst2


def test_example_978jli8f():
    lst = module_0.ImmutableList.of(1, 2, 3)
    added_lst = lst + module_0.ImmutableList.of(4, 5)
    assert added_lst.to_list() == [1, 2, 3, 4, 5]


