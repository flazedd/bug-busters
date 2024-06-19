from typing import Generator
import pytest
from __type_hints import Comparable
import bst as module_0
import doctest
from typing import List
from typing import Optional
def test_example_e8tgu3ua():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    assert bst.get_root().value == 5


def test_example_8qtjtp65():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    assert 3 in bst


def test_example_nu9vvhd6():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    assert len(bst) == 3


def test_example_w7r0yj2f():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    assert list(bst.iterate_preorder()) == [5, 3, 7]


def test_example_gg4v0m3v():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    assert list(bst.iterate_inorder()) == [2, 3, 4, 5, 6, 7, 8]


def test_example_jklivvld():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    assert list(bst.iterate_leaves()) == [2, 4, 6, 8]


def test_example_4baxqp0y():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    assert bst.depth() == 3


def test_example_dtsslyyg():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    assert list(bst.get_nodes_in_range_inclusive(4, 6)) == [bst[4], bst[5], bst[6]]


