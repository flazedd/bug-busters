from typing import Callable
import immutable_list as module_0
from typing import Optional
from typing import Generic
from typing import TypeVar
import pytest
def test_example_w21v5iwl():
    il = module_0.ImmutableList.of(1, 2, 3, 4, 5)
    double_elements = il.map(lambda x: x * 2)
    assert double_elements.to_list() == [2, 4, 6, 8, 10]


def test_example_m7vn2gdi():
    il = module_0.ImmutableList.of('a', 'b', 'c')
    filtered_elements = il.filter(lambda x: x != 'b')
    assert filtered_elements.to_list() == ['a', 'c']


def test_example_yqx853vh():
    il = module_0.ImmutableList.of(1, 2, 3, 4, 5)
    reduced_elements = il.reduce(lambda x, y: x + y, 0)
    assert reduced_elements == 15


def test_example_6j2b2xl5():
    il = module_0.ImmutableList.of(1, 2, 3, 4, 5)
    found_element = il.find(lambda x: x > 3)
    assert found_element == 4


def test_example_pglnmllf():
    il = module_0.ImmutableList.of(1, 2, 3, 4, 5)
    appended_list = il.append(6)
    assert appended_list.to_list() == [1, 2, 3, 4, 5, 6]


def test_example_tlk0iq30():
    il = module_0.ImmutableList.of(1, 2, 3, 4, 5)
    unshifted_list = il.unshift(0)
    assert unshifted_list.to_list() == [0, 1, 2, 3, 4, 5]


def test_example_p4wyvux5():
    il1 = module_0.ImmutableList.of(1, 2, 3)
    il2 = module_0.ImmutableList.of(4, 5, 6)
    added_list = il1 + il2
    assert added_list.to_list() == [1, 2, 3, 4, 5, 6]


def test_example_ou3386i9():
    il = module_0.ImmutableList.empty()
    assert il.is_empty == True


