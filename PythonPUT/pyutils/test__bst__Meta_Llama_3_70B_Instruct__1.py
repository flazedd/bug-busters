import doctest
import pytest
from __type_hints import Comparable
from typing import Optional
import bst as module_0
from typing import List
from typing import Generator
def test_example_e78g0i0q():
    t = module_0.BinarySearchTree()
    t.insert(50)
    assert t.depth() == 1


def test_example_1fgnsp03():
    t = module_0.BinarySearchTree()
    t.insert(50)
    t.insert(25)
    t.insert(75)
    assert t.get_next_node(t[50]).value == 75


def test_example_3d7maa72():
    t = module_0.BinarySearchTree()
    t.insert(50)
    t.insert(25)
    t.insert(75)
    t.insert(66)
    t.insert(22)
    t.insert(13)
    t.insert(23)
    assert list(t.iterate_inorder()) == [13, 22, 23, 25, 50, 66, 75]


def test_example_bsocfsgf():
    t = module_0.BinarySearchTree()
    t.insert(50)
    t.insert(25)
    t.insert(75)
    t.insert(66)
    t.insert(22)
    t.insert(13)
    t.insert(23)
    assert list(t.get_nodes_in_range_inclusive(21, 74)) == [t[22], t[23], t[25], t[50], t[66]]


def test_example_h60srvve():
    t = module_0.BinarySearchTree()
    t.insert(50)
    t.insert(25)
    t.insert(75)
    t.insert(66)
    t.insert(22)
    t.insert(13)
    t.insert(23)
    assert list(t.iterate_leaves()) == [13, 23, 66]


def test_example_pu2us7xr():
    t = module_0.BinarySearchTree()
    t.insert(50)
    t.insert(25)
    t.insert(75)
    t.insert(66)
    t.insert(22)
    t.insert(13)
    t.insert(23)
    assert t.height() == 4


def test_example_uds5ukp4():
    t = module_0.BinarySearchTree()
    t.insert(50)
    t.insert(25)
    t.insert(75)
    t.insert(66)
    t.insert(22)
    t.insert(13)
    t.insert(23)
    assert list(t.iterate_preorder()) == [50, 25, 22, 13, 23, 75, 66]


def test_example_wg9relly():
    t = module_0.BinarySearchTree()
    t.insert(50)
    t.insert(25)
    t.insert(75)
    t.insert(66)
    t.insert(22)
    t.insert(13)
    t.insert(23)
    assert t.get_next_node(t[25]).value == 50


