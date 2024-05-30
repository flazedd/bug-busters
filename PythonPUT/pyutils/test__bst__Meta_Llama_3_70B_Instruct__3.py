from __type_hints import Comparable
import pytest
from typing import Optional
from typing import List
import bst as module_0
from typing import Generator
import doctest
def test_example_df006klw():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    assert 3 in bst


def test_example_e3oqsibn():
    bst = module_0.BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    assert list(bst.iterate_inorder()) == [3, 5, 7, 10, 15]


def test_example_ai05skc5():
    bst = module_0.BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    assert bst.depth() == 3


def test_example_jyslmkii():
    bst = module_0.BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    assert list(bst.iterate_leaves()) == [3, 7, 15]


def test_example_pb88rfuy():
    bst = module_0.BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    del bst[5]
    assert 5 not in bst


def test_example_mmh31plj():
    bst = module_0.BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    assert bst.height() == 3


def test_example_2dlswh8z():
    bst = module_0.BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    assert list(bst.iterate_preorder()) == [10, 5, 3, 7, 15]


def test_example_fqubw7ro():
    bst = module_0.BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    assert bst.get_next_node(bst.get_root().left).value == 7


