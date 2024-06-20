from typing import Dict
import doctest
from typing import Sequence
from typing import Generator
import trie as module_0
from typing import Any
import logging
import pytest
def test_example_erdrufhv():
    t = module_0.Trie()
    t.insert('test')
    assert 'test' in t


def test_example_fuhxmkf4():
    t = module_0.Trie()
    t.insert('testing')
    t.insert('test')
    assert t.contains_prefix('te')


def test_example_g2mdinn3():
    t = module_0.Trie()
    t.insert('testing')
    t.insert('test')
    assert len(t) == 2


def test_example_oo6oemno():
    t = module_0.Trie()
    t.insert('testing')
    t.insert('test')
    t.__delitem__('test')
    assert len(t) == 1


def test_example_yq4rbosp():
    t = module_0.Trie()
    t.insert('testing')
    t.insert('test')
    for item in t:
        assert item in ['testing', 'test']


def test_example_tk7t9s7s():
    t = module_0.Trie()
    t.insert('testing')
    t.insert('test')
    assert 'testing' in t
    assert 'test' in t


def test_example_m6fax3k6():
    t = module_0.Trie()
    t.insert('testing')
    t.insert('test')
    t.insert('tess')
    assert t.repr_brief(t.root, '.') == 't.e.s.[t.i.n.g,s]'


def test_example_lgal375y():
    t = module_0.Trie()
    t.insert('testing')
    t.insert('test')
    t.insert('tess')
    assert t.contains_prefix('tes')


