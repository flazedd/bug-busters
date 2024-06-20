from typing import Callable
import pytest
from typing import Optional
from typing import TypeVar
from typing import Generic
import immutable_list as module_0
def test_immutable_list_t7txjggj():
    lst = module_0.ImmutableList.of(1, 2, 3)
    assert lst.to_list() == [1, 2, 3]


def test_immutable_list_map_fedbpdlj():
    lst = module_0.ImmutableList.of(1, 2, 3)
    double_lst = lst.map(lambda x: x * 2)
    assert double_lst.to_list() == [2, 4, 6]


def test_immutable_list_filter_dygv7yd9():
    lst = module_0.ImmutableList.of(1, 2, 3, 4, 5, 6)
    even_lst = lst.filter(lambda x: x % 2 == 0)
    assert even_lst.to_list() == [2, 4, 6]


def test_immutable_list_append_xmwnul9v():
    lst = module_0.ImmutableList.of(1, 2, 3)
    new_lst = lst.append(4)
    assert new_lst.to_list() == [1, 2, 3, 4]


def test_immutable_list_unshift_hiw5vooi():
    lst = module_0.ImmutableList.of(1, 2, 3)
    new_lst = lst.unshift(0)
    assert new_lst.to_list() == [0, 1, 2, 3]


def test_immutable_list_reduce_q088ppbr():
    lst = module_0.ImmutableList.of(1, 2, 3, 4, 5)
    sum_result = lst.reduce(lambda acc, x: acc + x, 0)
    assert sum_result == 15


def test_immutable_list_find_mpxef9my():
    lst = module_0.ImmutableList.of(1, 2, 3, 4, 5)
    found_element = lst.find(lambda x: x > 3)
    assert found_element == 4


def test_immutable_list_eq_y13gsrsy():
    lst1 = module_0.ImmutableList.of(1, 2, 3)
    lst2 = module_0.ImmutableList.of(1, 2, 3)
    assert lst1 == lst2


