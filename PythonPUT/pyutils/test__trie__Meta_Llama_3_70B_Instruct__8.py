from typing import Generator
from typing import Any
import trie as module_0
import doctest
from typing import Dict
import logging
import pytest
from typing import Sequence
def test_example_w06btm3s():
    t = module_0.Trie()
    t.insert('test')
    assert 'test' in t


def test_example_mihmhbkk():
    t = module_0.Trie()
    t.insert('test')
    t.insert('testing')
    assert t.contains_prefix('test')


def test_example_ybukq4gi():
    t = module_0.Trie()
    t.insert('test')
    t.insert('testing')
    assert len(t) == 2


def test_example_6dwti373():
    t = module_0.Trie()
    t.insert('test')
    t.insert('testing')
    t.__delitem__('test')
    assert len(t) == 1


def test_example_gk4l35q1():
    t = module_0.Trie()
    t.insert('what')
    t.insert('who')
    t.insert('when')
    assert t.successors('wh') == ['a', 'o', 'e']


def test_example_q3elk070():
    t = module_0.Trie()
    t.insert(['this', 'is', 'a', 'test'])
    t.insert(['this', 'is', 'a', 'robbery'])
    t.insert(['this', 'is', 'a', 'walrus'])
    assert t.successors(['this', 'is', 'a']) == ['test', 'robbery', 'walrus']


def test_example_4oji2925():
    t = module_0.Trie()
    t.insert('test')
    t.insert('tickle')
    for item in t:
        assert item in ['test', 'tickle']


def test_example_fny6u0q4():
    t = module_0.Trie()
    t.insert('test')
    t.insert('tess')
    t.insert('tessel')
    assert t.repr_brief(t.root, '.') == 't.e.s.[t,s.e.l]'


