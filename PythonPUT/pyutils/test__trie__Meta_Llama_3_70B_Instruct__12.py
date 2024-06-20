import pytest
from typing import Any
import doctest
import trie as module_0
from typing import Sequence
import logging
from typing import Dict
from typing import Generator
def test_example_ecijy94l():
    trie = module_0.Trie()
    trie.insert('test')
    assert 'test' in trie





def test_example_eehkim1j():
    trie = module_0.Trie()
    trie.insert('testing')
    trie.insert('tests')
    assert trie.contains_prefix('test')





def test_example_49yt3prg():
    trie = module_0.Trie()
    trie.insert('test')
    trie.insert('testing')
    trie.insert('tessera')
    assert len(trie) == 3





def test_example_ri8j5cp5():
    trie = module_0.Trie()
    trie.insert('test')
    trie.insert('testing')
    trie.insert('tessera')
    trie.__delitem__('test')
    assert len(trie) == 2





def test_example_vpl90idc():
    trie = module_0.Trie()
    trie.insert('test')
    trie.insert('testing')
    trie.insert('tessera')
    assert 'tessera' in trie





def test_example_2obgyt66():
    trie = module_0.Trie()
    trie.insert('test')
    trie.insert('testing')
    trie.insert('tessera')
    trie.insert('tessera')
    for item in trie:
        assert item in ['test', 'testing', 'tessera']





def test_example_s5515r9y():
    trie = module_0.Trie()
    trie.insert('test')
    trie.insert('testing')
    trie.insert('tessera')
    trie.insert('tessera')
    trie.__delitem__('testing')
    assert 'testing' not in trie





def test_example_ta89n8gg():
    t = module_0.Trie()
    t.insert('test')
    assert 'test' in t


