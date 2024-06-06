import pytest
from typing import Callable
from typing import Optional
from typing import Generic
import immutable_list as module_0
from typing import TypeVar
def test_immutable_list_append_u36ai6tt():
    il = module_0.ImmutableList.of(1, 2, 3)
    new_il = il.append(4)
    assert new_il.to_list() == [1, 2, 3, 4]


def test_immutable_list_unshift_7rlc0u78():
    il = module_0.ImmutableList.of(1, 2, 3)
    new_il = il.unshift(0)
    assert new_il.to_list() == [0, 1, 2, 3]


def test_immutable_list_map_cbop6koe():
    il = module_0.ImmutableList.of(1, 2, 3)
    new_il = il.map(lambda x: x * 2)
    assert new_il.to_list() == [2, 4, 6]


def test_immutable_list_find_zi4tdx1r():
    il = module_0.ImmutableList.of(1, 2, 3, 4, 5)
    found = il.find(lambda x: x > 3)
    assert found == 4


def test_immutable_list_reduce_wpg4naqp():
    il = module_0.ImmutableList.of(1, 2, 3, 4, 5)
    result = il.reduce(lambda acc, x: acc + x, 0)
    assert result == 15


def test_immutable_list_eq_bqcxhl16():
    il1 = module_0.ImmutableList.of(1, 2, 3)
    il2 = module_0.ImmutableList.of(1, 2, 3)
    assert il1 == il2


def test_immutable_list_len_43vgejmi():
    il = module_0.ImmutableList.of(1, 2, 3, 4, 5)
    assert len(il) == 5


def test_immutable_list_str_tzpsk6xf():
    il = module_0.ImmutableList.of(1, 2, 3)
    assert str(il) == 'ImmutableList[1, 2, 3]'


