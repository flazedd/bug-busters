from typing import Dict
import pytest
from typing import Any
import logging
import doctest
import trie as module_0
from typing import Generator
from typing import Sequence
def test_example_iyqojqhk():
    t = module_0.Trie()
    t.insert('test')
    assert 'test' in t





def test_example_epapwu26():
    t = module_0.Trie()
    t.insert('test')
    t.insert('testing')
    assert t.contains_prefix('test')





def test_example_s34ihd4z():
    t = module_0.Trie()
    t.insert('test')
    t.insert('testing')
    t.__delitem__('test')
    assert 'test' not in t





def test_example_jp1lnejp():
    t = module_0.Trie()
    t.insert('what')
    t.insert('who')
    t.insert('when')
    assert t.successors('wh') == ['a', 'o', 'e']





def test_example_qghiquhc():
    t = module_0.Trie()
    t.insert('what')
    t.insert('who')
    t.insert('when')
    assert t.repr_brief(t.root, '.') == 'w.h.[a.t,o,e.n]'





def test_example_8503xs7z():
    t = module_0.Trie()
    t.insert('abc')
    t.insert('abcd')
    t.insert('abe')
    assert t.contains_prefix('ab') == True





def test_example_qvjb13xa():
    t = module_0.Trie()
    t.insert('abc')
    t.insert('abcd')
    t.insert('abe')
    assert t.contains_prefix('abcde') == False





def test_example_wgyw99hs():
    t = module_0.Trie()
    t.insert('test')
    assert 'test' in t


