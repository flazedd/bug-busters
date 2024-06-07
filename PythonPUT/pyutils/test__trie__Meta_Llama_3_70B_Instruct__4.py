import logging
from typing import Any
import pytest
import trie as module_0
import doctest
from typing import Generator
from typing import Dict
from typing import Sequence
def test_example_n53al6wb():
    t = module_0.Trie()
    t.insert('test')
    assert 'test' in t


def test_example_pjehi0k3():
    t = module_0.Trie()
    t.insert('test')
    t.insert('testing')
    assert t.contains_prefix('test')


def test_example_w4jk7nk3():
    t = module_0.Trie()
    t.insert('test')
    t.insert('testing')
    t.insert('tess')
    assert len(t) == 3


def test_example_fyqk6eki():
    t = module_0.Trie()
    t.insert('test')
    t.insert('testing')
    t.insert('tess')
    assert list(t) == ['test', 'testing', 'tess']


def test_example_98o7dgug():
    t = module_0.Trie()
    t.insert('what')
    t.insert('who')
    t.insert('when')
    assert t.successors('wh') == ['a', 'o', 'e']


def test_example_9y73r121():
    t = module_0.Trie()
    t.insert(['this', 'is', 'a', 'test'])
    t.insert(['this', 'is', 'a', 'robbery'])
    t.insert(['this', 'is', 'a', 'walrus'])
    assert t.successors(['this', 'is', 'a']) == ['test', 'robbery', 'walrus']


def test_example_23l9871n():
    t = module_0.Trie()
    t.insert('test')
    t.insert('testing')
    t.insert('tess')
    t.__delitem__('test')
    assert len(t) == 2


def test_example_a4lp7tih():
    t = module_0.Trie()
    t.insert('test')
    t.insert('testing')
    t.insert('tess')
    t.__delitem__('testing')
    assert 'testing' not in t


