from typing import TypeVar
from typing import Generic
from typing import Callable
from typing import Optional
import pytest
import immutable_list as module_0
def test_example_1kmk4ecy():
    il = module_0.ImmutableList.of(1, 2, 3)
    assert il.to_list() == [1, 2, 3]


def test_example_2kroydoh():
    il = module_0.ImmutableList.of(1, 2, 3)
    il2 = il.append(4)
    assert il2.to_list() == [1, 2, 3, 4]


def test_example_d73rp3di():
    il = module_0.ImmutableList.of(1, 2, 3)
    il2 = il.map(lambda x: x * 2)
    assert il2.to_list() == [2, 4, 6]


def test_example_3j1nanyv():
    il = module_0.ImmutableList.of(1, 2, 3)
    il2 = il.unshift(0)
    assert il2.to_list() == [0, 1, 2, 3]


def test_example_92j9gy0c():
    il = module_0.ImmutableList.of(1, 2, 3)
    assert il.find(lambda x: x % 2 == 0) == 2


def test_example_k8jflpfz():
    il = module_0.ImmutableList.of(1, 2, 3)
    assert il.reduce(lambda acc, x: acc + x, 0) == 6


def test_example_zyh451ug():
    il = module_0.ImmutableList.of(1, 2, 3)
    il2 = il + module_0.ImmutableList.of(4, 5, 6)
    assert il2.to_list() == [1, 2, 3, 4, 5, 6]


def test_example_zuja1k5j():
    il = module_0.ImmutableList.of(1, 2, 3)
    il2 = il.filter(lambda x: x != 2)
    assert il2.to_list() == [1, 3]


