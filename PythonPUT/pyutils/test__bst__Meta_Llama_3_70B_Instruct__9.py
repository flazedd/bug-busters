import doctest
from typing import List
from typing import Generator
from typing import Optional
import pytest
import bst as module_0
from __type_hints import Comparable
def test_example_t9l1kpxl():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    assert bst.get_nodes_in_range_inclusive(3, 7).__next__().value == 3


def test_example_j16ttrfl():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    assert bst.height() == 2


def test_example_559qx61d():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    assert list(bst.iterate_inorder()) == [3, 5, 7]


def test_example_pq0vckf4():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    assert bst.depth() == 2


def test_example_jw0eh97b():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    assert bst.get_next_node(bst.get_root()).value == 7


def test_example_n9nuppo0():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    assert list(bst.iterate_leaves()) == [3, 7]


def test_example_e03tto46():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    assert bst.get_nodes_in_range_inclusive(3, 7).__next__().value == 3
    assert list(bst.get_nodes_in_range_inclusive(3, 7))[1].value == 5
    assert list(bst.get_nodes_in_range_inclusive(3, 7))[2].value == 7


def test_example_uwx4u7r4():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    assert bst.parent_path(bst.get_root().right).index(bst.get_root()) == 0


