from typing import List
import pytest
import bst as module_0
from typing import Optional
from __type_hints import Comparable
import doctest
from typing import Generator
def test_example_rzeomnzt():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    assert 3 in [x.value for x in bst.get_nodes_in_range_inclusive(2, 4)]


def test_example_1f8s32x2():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    assert bst.depth() == 3


def test_example_9bk5lgd0():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    assert list(bst.iterate_inorder()) == [3, 5, 7]


def test_example_ml8x47h4():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    assert list(bst.iterate_leaves()) == [2, 4, 7]


def test_example_x50m47yb():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    assert bst.get_root().value == 5


def test_example_cqarydec():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    del bst[3]
    assert bst.get_root().left.value == 4


def test_example_gzy2f0gh():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    assert bst.get_next_node(bst.get_root().left).value == 5


def test_example_u9kl6y1y():
    bst = module_0.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    assert list(bst.iterate_postorder()) == [2, 4, 3, 7, 5]


