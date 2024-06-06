from typing import TypeVar
import immutable_list as module_0
from typing import Generic
from typing import Optional
from typing import Callable
import pytest
def test_immutable_list_append_5hytcd0x():
    assert module_0.ImmutableList.of(1, 2, 3).append(4).to_list() == [1, 2, 3, 4]


def test_immutable_list_unshift_fyi0xttv():
    assert module_0.ImmutableList.of(1, 2, 3).unshift(0).to_list() == [0, 1, 2, 3]


def test_immutable_list_map_scsuvwrq():
    assert module_0.ImmutableList.of(1, 2, 3).map(lambda x: x * 2).to_list() == [2, 4, 6]


def test_immutable_list_find_4e8wbbnn():
    assert module_0.ImmutableList.of(1, 2, 3, 4, 5).find(lambda x: x > 3) == 4


def test_immutable_list_reduce_unr33pdl():
    assert module_0.ImmutableList.of(1, 2, 3).reduce(lambda acc, x: acc + x, 0) == 6


def test_immutable_list_eq_evssnmwe():
    assert module_0.ImmutableList.of(1, 2, 3) == module_0.ImmutableList.of(1, 2, 3)


def test_immutable_list_len_jdncs3n5():
    assert len(module_0.ImmutableList.of(1, 2, 3)) == 3


def test_immutable_list_add_0o57m2md():
    assert (module_0.ImmutableList.of(1, 2, 3) + module_0.ImmutableList.of(4, 5, 6)).to_list() == [1, 2, 3, 4, 5, 6]


