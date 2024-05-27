import pytest
import trie as module_0
from typing import Any
from typing import Generator
from typing import Dict
import doctest
from typing import Sequence
import logging
def test_example_32knq32k():
    t = module_0.Trie()
    t.insert('test')
    assert 'test' in t


def test_example_f4kssjaj():
    t = module_0.Trie()
    t.insert('test')
    t.insert('testing')
    assert t.contains_prefix('test')


def test_example_e6pmorgi():
    t = module_0.Trie()
    t.insert('test')
    t.insert('testing')
    t.insert('tess')
    assert len(t) == 3


def test_example_ml47yj20():
    t = module_0.Trie()
    t.insert('test')
    t.insert('testing')
    t.insert('tess')
    t.__delitem__('testing')
    assert len(t) == 2


def test_example_vffl28wc():
    t = module_0.Trie()
    t.insert('what')
    t.insert('who')
    t.insert('when')
    assert t.successors('wh') == ['a', 'o', 'e']


def test_example_kv3vqv6g():
    t = module_0.Trie()
    t.insert(['this', 'is', 'a', 'test'])
    t.insert(['this', 'is', 'a', 'robbery'])
    t.insert(['this', 'is', 'a', 'walrus'])
    assert t.successors(['this', 'is', 'a']) == ['test', 'robbery', 'walrus']


def test_example_rw8zivgc():
    t = module_0.Trie()
    t.insert('test')
    t.insert('testing')
    t.insert('tess')
    assert list(t) == ['test', 'testing', 'tess']


def test_example_zh5yvzxu():
    t = module_0.Trie()
    t.insert([10, 0, 0, 1])
    t.insert([10, 0, 0, 2])
    t.insert([10, 10, 10, 1])
    t.insert([10, 10, 10, 2])
    assert t.repr_brief(t.root, '.') == '10.[0.0.[1,2],10.10.[1,2]]'


