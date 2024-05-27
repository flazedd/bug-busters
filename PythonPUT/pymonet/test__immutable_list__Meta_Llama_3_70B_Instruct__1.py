from typing import Callable
import pytest
from typing import TypeVar
import immutable_list as module_0
from typing import Optional
from typing import Generic
def test_immutable_list_append_86bqf9vw():
    assert module_0.ImmutableList.of(1, 2, 3).append(4).to_list() == [1, 2, 3, 4]


def test_immutable_list_map_eogjhwrx():
    assert module_0.ImmutableList.of(1, 2, 3).map(lambda x: x * 2).to_list() == [2, 4, 6]


def test_immutable_list_find_dum907of():
    assert module_0.ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x % 2 == 0) == 2


def test_immutable_list_reduce_sy70rtxm():
    assert module_0.ImmutableList.of(1, 2, 3, 4, 5).reduce(lambda x, y: x + y, 0) == 15


def test_immutable_list_unshift_iddfgowt():
    assert module_0.ImmutableList.of(1, 2, 3).unshift(0).to_list() == [0, 1, 2, 3]


def test_immutable_list_eq_jfmknhsm():
    assert module_0.ImmutableList.of(1, 2, 3) == module_0.ImmutableList.of(1, 2, 3)


def test_immutable_list_len_pz47oa6n():
    assert len(module_0.ImmutableList.of(1, 2, 3, 4, 5)) == 5


def test_immutable_list_str_cp8z438p():
    assert str(module_0.ImmutableList.of(1, 2, 3)) == 'ImmutableList[1, 2, 3]'


