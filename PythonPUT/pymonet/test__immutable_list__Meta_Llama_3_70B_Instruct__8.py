import immutable_list as module_0
import pytest
from typing import Optional
from typing import TypeVar
from typing import Generic
from typing import Callable
def test_example_nxy3e66s():
    il = module_0.ImmutableList.of(1, 2, 3)
    assert il.to_list() == [1, 2, 3]


def test_example_vaiwkm7y():
    il = module_0.ImmutableList.of(1, 2, 3)
    il_mapped = il.map(lambda x: x * 2)
    assert il_mapped.to_list() == [2, 4, 6]


def test_example_unbwm7vg():
    il = module_0.ImmutableList.of(1, 2, 3)
    il_appended = il.append(4)
    assert il_appended.to_list() == [1, 2, 3, 4]


def test_example_c1s2scxw():
    il = module_0.ImmutableList.of(1, 2, 3)
    il_unshifted = il.unshift(0)
    assert il_unshifted.to_list() == [0, 1, 2, 3]


def test_example_js9ymfa8():
    il = module_0.ImmutableList.of(1, 2, 3)
    assert il.find(lambda x: x > 2) == 3


def test_example_shk078z4():
    il = module_0.ImmutableList.of(1, 2, 3)
    assert il.reduce(lambda acc, x: acc + x, 0) == 6


def test_example_1sadtb1s():
    il1 = module_0.ImmutableList.of(1, 2, 3)
    il2 = module_0.ImmutableList.of(4, 5, 6)
    il_added = il1 + il2
    assert il_added.to_list() == [1, 2, 3, 4, 5, 6]


def test_example_cgumtuap():
    il = module_0.ImmutableList.of(1, 2, 3)
    assert len(il) == 3


