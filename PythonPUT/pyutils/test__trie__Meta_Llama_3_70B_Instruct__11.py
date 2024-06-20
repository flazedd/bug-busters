import pytest
from typing import Any
import doctest
import trie as module_0
from typing import Sequence
import logging
from typing import Dict
from typing import Generator
def test_example_sn16epco():
    t = module_0.Trie()
    t.insert('test')
    assert 'test' in t


def test_example_wqlzdpkq():
    t = module_0.Trie()
    t.insert('test')
    t.insert('testing')
    assert t.contains_prefix('test')


def test_example_h65m5tn5():
    t = module_0.Trie()
    t.insert('test')
    t.insert('testing')
    t.__delitem__('test')
    assert 'test' not in t


def test_example_en9w6gmh():
    t = module_0.Trie()
    t.insert('what')
    t.insert('who')
    t.insert('when')
    assert t.successors('wh') == ['a', 'o', 'e']


def test_example_z4i7coff():
    t = module_0.Trie()
    t.insert('test')
    t.insert('tess')
    t.insert('tessel')
    assert list(t) == ['test', 'tess', 'tessel']


def test_example_2pr39zka():
    t = module_0.Trie()
    t.insert([10, 0, 0, 1])
    t.insert([10, 0, 0, 2])
    t.insert([10, 10, 10, 1])
    t.insert([10, 10, 10, 2])
    assert t.repr_brief(t.root, '.') == '10.[0.0.[1,2],10.10.[1,2]]'


def test_example_yybc1m6a():
    t = module_0.Trie()
    t.insert('test')
    assert t.length == 1


def test_example_p613k9x2():
    t = module_0.Trie()
    t.insert('test')
    t.insert('testing')
    assert len(t) == 2


