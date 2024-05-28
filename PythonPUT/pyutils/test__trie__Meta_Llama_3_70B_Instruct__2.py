import doctest
import pytest
from typing import Generator
import logging
from typing import Sequence
from typing import Any
from typing import Dict
import trie as module_0
def test_example_p6xwmiaz():
    t = module_0.Trie()
    t.insert('test')
    assert 'test' in t


def test_example_76bplzh9():
    t = module_0.Trie()
    t.insert('test')
    t.insert('testing')
    assert t.contains_prefix('test')


def test_example_2u4nli87():
    t = module_0.Trie()
    t.insert('test')
    t.insert('testing')
    del t['test']
    assert 'test' not in t


def test_example_qfnlsph5():
    t = module_0.Trie()
    t.insert('test')
    t.insert('testing')
    assert len(t) == 2


def test_example_ghwo8vsl():
    t = module_0.Trie()
    t.insert('test')
    t.insert('testing')
    for item in t:
        assert item in ['test', 'testing']


def test_example_791ka96h():
    t = module_0.Trie()
    t.insert('what')
    t.insert('who')
    t.insert('when')
    assert t.successors('wh') == ['a', 'o', 'e']


def test_example_pxqi7qdn():
    t = module_0.Trie()
    t.insert('this')
    t.insert('that')
    assert t.contains_prefix('th')


def test_example_m8z9qj8y():
    t = module_0.Trie()
    t.insert('test')
    assert t.repr_brief(t.root, '.') == 't.e.s.t'


