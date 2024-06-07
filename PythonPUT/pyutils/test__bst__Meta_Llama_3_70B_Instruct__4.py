from typing import Generator
from typing import Optional
from __type_hints import Comparable
import bst as module_0
import doctest
import pytest
from typing import List
def test_example_e6vzzk4f():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    assert list(bst.iterate_inorder()) == [2, 3, 4, 5, 6, 7, 8]


def test_example_nmuv7a0j():
    bst = module_0.BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    bst.insert(12)
    bst.insert(20)
    assert bst.depth() == 3


def test_example_al6fflbp():
    bst = module_0.BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    bst.insert(12)
    bst.insert(20)
    assert list(bst.iterate_leaves()) == [3, 7, 12, 20]


def test_example_zsf6uzsz():
    bst = module_0.BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    bst.insert(12)
    bst.insert(20)
    assert bst.get_next_node(bst.get_root().left).value == 7


def test_example_u10bu27d():
    bst = module_0.BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    bst.insert(12)
    bst.insert(20)
    assert list(bst.iterate_preorder()) == [10, 5, 3, 7, 15, 12, 20]


def test_example_tuqeyawx():
    bst = module_0.BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    bst.insert(12)
    bst.insert(20)
    assert list(bst.iterate_postorder()) == [3, 7, 5, 12, 20, 15, 10]


def test_example_qqglzwi3():
    bst = module_0.BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    bst.insert(12)
    bst.insert(20)
    assert bst.get_nodes_in_range_inclusive(5, 15) is not None


def test_example_zfs3gx98():
    bst = module_0.BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    bst.insert(12)
    bst.insert(20)
    assert bst.__contains__(12) == True


