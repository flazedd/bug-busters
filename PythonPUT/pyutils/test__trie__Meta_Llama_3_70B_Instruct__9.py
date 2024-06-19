import logging
import doctest
from typing import Dict
from typing import Sequence
from typing import Any
from typing import Generator
import trie as module_0
import pytest
def test_example_67983gb5():
    t = module_0.Trie()
    t.insert('test')
    assert 'test' in t


def test_example_mpwmygr5():
    t = module_0.Trie()
    t.insert('what')
    t.insert('who')
    t.insert('when')
    assert t.successors('wh') == ['a', 'o', 'e']


def test_example_49g8mege():
    t = module_0.Trie()
    t.insert(['this', 'is', 'a', 'test'])
    t.insert(['this', 'is', 'a', 'robbery'])
    t.insert(['this', 'is', 'a', 'walrus'])
    assert t.successors(['this', 'is', 'a']) == ['test', 'robbery', 'walrus']


def test_example_3zt6k9qj():
    t = module_0.Trie()
    t.insert('test')
    t.insert('tess')
    t.insert('tessel')
    assert len(t) == 3


def test_example_wlh6qkvh():
    t = module_0.Trie()
    t.insert('test')
    t.insert('tess')
    t.insert('tessel')
    del t['test']
    assert len(t) == 2


def test_example_geffne6x():
    t = module_0.Trie()
    t.insert('test')
    t.insert('tess')
    t.insert('tessel')
    for item in t:
        assert item in ['test', 'tess', 'tessel']


def test_example_skclox64():
    t = module_0.Trie()
    t.insert('test')
    t.insert('tess')
    t.insert('tessel')
    assert t.contains_prefix('tes') == True


def test_example_m3rtbkpx():
    t = module_0.Trie()
    t.insert('test')
    t.insert('tess')
    t.insert('tessel')
    assert t.contains_prefix('te') == True


