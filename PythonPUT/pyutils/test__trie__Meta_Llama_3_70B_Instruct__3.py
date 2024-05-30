import trie as module_0
import logging
import doctest
import pytest
from typing import Any
from typing import Sequence
from typing import Dict
from typing import Generator
def test_example_e3q2v0zn():
    t = module_0.Trie()
    t.insert('test')
    assert 'test' in t


def test_example_1c4cgxh2():
    t = module_0.Trie()
    t.insert('test')
    t.insert('testing')
    assert t.contains_prefix('test')


def test_example_iv5g8pfn():
    t = module_0.Trie()
    t.insert('test')
    t.insert('testing')
    assert len(t) == 2


def test_example_f2yihwvj():
    t = module_0.Trie()
    t.insert('test')
    t.insert('testing')
    del t['test']
    assert len(t) == 1


def test_example_89akhuap():
    t = module_0.Trie()
    t.insert('what')
    t.insert('who')
    t.insert('when')
    assert t.successors('wh') == ['a', 'o', 'e']


def test_example_xxv24kz8():
    t = module_0.Trie()
    t.insert('this')
    t.insert('that')
    t.insert('them')
    assert 'this' in t


def test_example_pdlq53e4():
    t = module_0.Trie()
    t.insert('this')
    t.insert('that')
    t.insert('them')
    for item in t:
        assert item in ['this', 'that', 'them']


def test_example_fyc5btxo():
    t = module_0.Trie()
    t.insert('test')
    t.insert('tess')
    t.insert('tessel')
    assert t.repr_brief(t.root, '.') == 't.e.s.[t,s.e.l]'


