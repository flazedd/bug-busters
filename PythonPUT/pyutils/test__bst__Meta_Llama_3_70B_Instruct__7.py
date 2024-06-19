from typing import Generator
import pytest
from __type_hints import Comparable
import bst as module_0
import doctest
from typing import List
from typing import Optional
def test_example_n0ipbz5p():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    assert bst.get_root().value == 5


def test_example_b7gw0yrc():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    assert len(list(bst.iterate_inorder())) == 3


def test_example_li860dg5():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    assert bst.get_next_node(bst.get_root().left).value == 5


def test_example_xkhzxlwu():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    assert bst.depth() == 2


def test_example_engtuwsh():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    assert bst.get_nodes_in_range_inclusive(3, 7).__next__().value == 3


def test_example_1px8gudl():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    assert list(bst.iterate_leaves()) == [2, 4, 7]


def test_example_w3xcigto():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    assert bst.__contains__(4) == True


def test_example_t14tvrwx():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.__delitem__(3)
    assert bst.__len__() == 4


