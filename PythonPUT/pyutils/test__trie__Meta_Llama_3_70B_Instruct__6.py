import doctest
from typing import Any
import pytest
from typing import Generator
import trie as module_0
from typing import Sequence
from typing import Dict
import logging
def test_example_qs0ao39o():
    t = module_0.Trie()
    t.insert('test')
    assert 'test' in t


def test_example_ml2kt39o():
    t = module_0.Trie()
    t.insert('what')
    t.insert('who')
    t.insert('when')
    assert t.successors('wh') == ['a', 'o', 'e']


def test_example_5r7pj4cq():
    t = module_0.Trie()
    t.insert('test')
    t.insert('tess')
    t.insert('tessel')
    assert len(t) == 3


def test_example_cb8dy25b():
    t = module_0.Trie()
    t.insert('this')
    t.insert('that')
    assert 'that' in t


def test_example_anrf6jbr():
    t = module_0.Trie()
    t.insert('test')
    t.insert('tess')
    t.insert('tessel')
    t.__delitem__('test')
    assert len(t) == 2


def test_example_z823u68y():
    t = module_0.Trie()
    t.insert('test')
    t.insert('tess')
    t.insert('tessel')
    for item in t:
        assert item in ['test', 'tess', 'tessel']


def test_example_w0rmtfx1():
    t = module_0.Trie()
    t.insert(['this', 'is', 'a', 'test'])
    t.insert(['this', 'is', 'a', 'robbery'])
    t.insert(['this', 'is', 'a', 'walrus'])
    assert t.successors(['this', 'is', 'a']) == ['test', 'robbery', 'walrus']


def test_example_iyaqaon5():
    t = module_0.Trie()
    t.insert('what')
    t.insert('who')
    t.insert('when')
    assert t.contains_prefix('wh')


