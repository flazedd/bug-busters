import immutable_list as module_0
import pytest
from typing import Optional
from typing import TypeVar
from typing import Generic
from typing import Callable
def test_example_yovamfbj():
    ilist = module_0.ImmutableList.of(1, 2, 3)
    assert ilist.to_list() == [1, 2, 3]


def test_example_q6gbexjw():
    ilist = module_0.ImmutableList.of(1, 2, 3)
    new_ilist = ilist.append(4)
    assert new_ilist.to_list() == [1, 2, 3, 4]


def test_example_64ktjc9a():
    ilist = module_0.ImmutableList.of(1, 2, 3)
    new_ilist = ilist.unshift(0)
    assert new_ilist.to_list() == [0, 1, 2, 3]


def test_example_imw73ggh():
    ilist = module_0.ImmutableList.of(1, 2, 3)
    mapped_ilist = ilist.map(lambda x: x * 2)
    assert mapped_ilist.to_list() == [2, 4, 6]


def test_example_lbltr8xj():
    ilist = module_0.ImmutableList.of(1, 2, 3)
    reduced_ilist = ilist.reduce(lambda acc, x: acc + x, 0)
    assert reduced_ilist == 6


def test_example_vfucrtt7():
    ilist = module_0.ImmutableList.of(1, 2, 3)
    found_element = ilist.find(lambda x: x > 2)
    assert found_element == 3


def test_example_o7ra5y0y():
    ilist = module_0.ImmutableList.of(1, 2, 3)
    assert len(ilist) == 3


def test_example_4f8t1ofl():
    ilist1 = module_0.ImmutableList.of(1, 2, 3)
    ilist2 = module_0.ImmutableList.of(4, 5, 6)
    ilist3 = ilist1 + ilist2
    assert ilist3.to_list() == [1, 2, 3, 4, 5, 6]


