import immutable_list as module_0
from typing import Callable
from typing import Generic
from typing import Optional
import pytest
from typing import TypeVar
def test_example_ex0fw8xm():
    lst = module_0.ImmutableList.of(1, 2, 3)
    assert lst.to_list() == [1, 2, 3]


def test_example_0ll3fs4a():
    lst = module_0.ImmutableList.of(1, 2, 3)
    new_lst = lst.append(4)
    assert new_lst.to_list() == [1, 2, 3, 4]


def test_example_4s4ed1qr():
    lst = module_0.ImmutableList.of(1, 2, 3)
    new_lst = lst.map(lambda x: x * 2)
    assert new_lst.to_list() == [2, 4, 6]


def test_example_ftdg2xwv():
    lst = module_0.ImmutableList.of(1, 2, 3)
    result = lst.reduce(lambda acc, x: acc + x, 0)
    assert result == 6


def test_example_gxrojp4h():
    lst = module_0.ImmutableList.of(1, 2, 3)
    new_lst = lst.unshift(0)
    assert new_lst.to_list() == [0, 1, 2, 3]


def test_example_apgf1iwp():
    lst = module_0.ImmutableList.of(1, 2, 3)
    assert len(lst) == 3


def test_example_bqbbxq0i():
    lst = module_0.ImmutableList.of(1, 2, 3)
    new_lst = lst + module_0.ImmutableList.of(4, 5)
    assert new_lst.to_list() == [1, 2, 3, 4, 5]


def test_example_jfiar9iw():
    lst = module_0.ImmutableList.of(1, 2, 3)
    assert lst == module_0.ImmutableList.of(1, 2, 3)


