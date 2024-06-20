from __type_hints import Comparable
from typing import List
import doctest
from typing import Optional
import bst as module_0
import pytest
from typing import Generator
def test_example_4rd3fzga():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    assert bst.get_root().value == 5


def test_example_ijmeoyvw():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    assert list(bst.iterate_inorder()) == [2, 3, 4, 5, 6, 7, 8]


def test_example_n5hpy9gm():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    assert list(bst.iterate_leaves()) == [2, 4, 6, 8]


def test_example_5mieaqkk():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    assert bst.get_next_node(bst.get_root().left).value == 4


def test_example_6dzvu72t():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    assert bst.depth() == 3


def test_example_9mjcjf2o():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    assert bst.__contains__(5) == True


def test_example_r4n1rxi4():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    bst.__delitem__(5)
    assert bst.__contains__(5) == False


def test_example_67h074t0():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    assert bst.get_root().left.value == 3


