import pytest
from typing import TypeVar
from typing import Callable
from typing import Optional
from typing import Generic
import immutable_list as module_0
def test_example_qcxx8lds():
    lst = module_0.ImmutableList.of(1, 2, 3)
    assert lst.to_list() == [1, 2, 3]





def test_example_sckkt6hh():
    lst = module_0.ImmutableList.of(1, 2, 3)
    new_lst = lst.append(4)
    assert new_lst.to_list() == [1, 2, 3, 4]





def test_example_h9w79yx0():
    lst = module_0.ImmutableList.of(1, 2, 3)
    new_lst = lst.unshift(0)
    assert new_lst.to_list() == [0, 1, 2, 3]





def test_example_4ucvau87():
    lst = module_0.ImmutableList.of(1, 2, 3)
    new_lst = lst.map(lambda x: x * 2)
    assert new_lst.to_list() == [2, 4, 6]





def test_example_5z1fa2xa():
    assert module_0.ImmutableList.of(1, 2, 3).to_list() == [1, 2, 3]


def test_example_6pj2hecm():
    assert module_0.ImmutableList.of(1, 2, 3).map(lambda x: x * 2).to_list() == [2, 4, 6]


def test_example_b6lyxrfw():
    assert module_0.ImmutableList.of(1, 2, 3).append(4).to_list() == [1, 2, 3, 4]


def test_example_wey8lq9m():
    assert module_0.ImmutableList.of(1, 2, 3).unshift(0).to_list() == [0, 1, 2, 3]


