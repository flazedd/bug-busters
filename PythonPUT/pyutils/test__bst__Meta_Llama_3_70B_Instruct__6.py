from __type_hints import Comparable
import doctest
from typing import Generator
import bst as module_0
from typing import List
from typing import Optional
import pytest
def test_example_qhdgvsig():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    assert 3 in bst


def test_example_dpeyn9cm():
    bst = module_0.BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    assert list(bst.iterate_inorder()) == [3, 5, 7, 10, 15]


def test_example_8hwf8ten():
    bst = module_0.BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    assert bst.depth() == 3


def test_example_466gukcy():
    bst = module_0.BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    assert list(bst.iterate_leaves()) == [3, 7, 15]


def test_example_21ms4wte():
    bst = module_0.BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    nodes = list(bst.get_nodes_in_range_inclusive(3, 7))
    assert [node.value for node in nodes] == [3, 5, 7]


def test_example_hfgxaehw():
    bst = module_0.BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    del bst[5]
    assert 5 not in bst


def test_example_vdcvy7nj():
    bst = module_0.BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    assert bst.height() == 3


def test_example_ev31seif():
    bst = module_0.BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    assert len(bst) == 5


