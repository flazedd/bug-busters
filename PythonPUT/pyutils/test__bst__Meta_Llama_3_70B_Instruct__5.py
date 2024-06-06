from __type_hints import Comparable
import bst as module_0
import pytest
import doctest
from typing import Optional
from typing import List
from typing import Generator
def test_example_tsq7amup():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    assert 3 in bst


def test_example_3j5textg():
    bst = module_0.BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    assert list(bst.iterate_inorder()) == [3, 5, 7, 10, 15]


def test_example_7zo9lfx0():
    bst = module_0.BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    assert bst.height() == 3


def test_example_dmvh9kfs():
    bst = module_0.BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    assert list(bst.iterate_leaves()) == [3, 7, 15]


def test_example_uoo1b9qv():
    bst = module_0.BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    del bst[5]
    assert 5 not in bst


def test_example_beldqs3i():
    bst = module_0.BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    assert bst.depth() == 3


def test_example_imluyx9v():
    bst = module_0.BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    assert list(bst.iterate_preorder()) == [10, 5, 3, 7, 15]


def test_example_fkre37uk():
    bst = module_0.BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    assert bst.get_root().value == 10


