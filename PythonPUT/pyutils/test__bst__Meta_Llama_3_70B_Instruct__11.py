from typing import List
import pytest
import bst as module_0
from typing import Optional
from __type_hints import Comparable
import doctest
from typing import Generator
def test_example_b4ynnyt7():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    assert 3 in bst


def test_example_488xm3y2():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    assert list(bst.iterate_inorder()) == [2, 3, 4, 5, 6, 7, 8]


def test_example_vy5g566v():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    assert bst.height() == 3


def test_example_js420lji():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    assert bst.depth() == 3


def test_example_guo2nu3y():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    del bst[7]
    assert 7 not in bst


def test_example_b7dbwkss():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    assert list(bst.iterate_leaves()) == [2, 4, 6, 8]


def test_example_kec0w05j():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    assert list(bst.iterate_preorder()) == [5, 3, 2, 4, 7, 6, 8]


def test_example_vk8new9j():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    assert list(bst.iterate_postorder()) == [2, 4, 3, 6, 8, 7, 5]


