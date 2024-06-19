from typing import Generator
from typing import Any
import trie as module_0
import doctest
from typing import Dict
import logging
import pytest
from typing import Sequence
def test_example_ryrelxnq():
    t = module_0.Trie()
    t.insert('test')
    assert 'test' in t


def test_example_h3rultl2():
    t = module_0.Trie()
    t.insert('test')
    t.insert('testing')
    assert t.contains_prefix('test')


def test_example_3x2x8zzf():
    t = module_0.Trie()
    t.insert('test')
    t.insert('testing')
    t.__delitem__('test')
    assert 'test' not in t


def test_example_dyv4njzx():
    t = module_0.Trie()
    t.insert('what')
    t.insert('who')
    t.insert('when')
    assert t.successors('wh') == ['a', 'o', 'e']


def test_example_5e7y9naz():
    t = module_0.Trie()
    t.insert('this')
    t.insert('that')
    assert len(t) == 2


def test_example_muk0die9():
    t = module_0.Trie()
    t.insert('test')
    t.insert('testing')
    assert list(t) == ['test', 'testing']


def test_example_ydco93dj():
    t = module_0.Trie()
    t.insert([10, 0, 0, 1])
    t.insert([10, 0, 0, 2])
    t.insert([10, 10, 10, 1])
    t.insert([10, 10, 10, 2])
    assert t.repr_brief(t.root, '.') == '10.[0.0.[1,2],10.10.[1,2]]'


def test_example_8xq0on6m():
    t = module_0.Trie()
    t.insert('test')
    t.insert('testing')
    assert t.contains_prefix('testing') == True


