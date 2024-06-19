from __future__ import annotations
from typing import Any
from typing import Union
from typing import Tuple
from typing import Optional
import logical_search as module_0
import logging
import enum
from typing import List
from __exceptions import PyUtilsParseError
import doctest
from typing import Dict
from collections import defaultdict
import pytest
from dataclasses import dataclass
from dataclasses import field
from typing import Sequence
from typing import Set
def test_example_n95twhcv():
    corpus = module_0.Corpus()
    doc = module_0.Document('doc1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    corpus.add_doc(doc)
    assert corpus.query('tag1') == {'doc1'}


def test_example_oa4zg0os():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('doc1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('doc2', {'tag2', 'tag3'}, [('key2', 'value2'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('tag1 or tag3') == {'doc1', 'doc2'}


def test_example_lntswxln():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('doc1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('doc2', {'tag2', 'tag3'}, [('key2', 'value2'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('not tag3') == {'doc1'}


def test_example_ga2olbko():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('doc1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('doc2', {'tag2', 'tag3'}, [('key2', 'value2'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('key1:value1') == {'doc1'}


def test_example_5j1fxt2q():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('doc1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('doc2', {'tag2', 'tag3'}, [('key2', 'value2'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('tag2 and key2:value2') == {'doc1', 'doc2'}


def test_example_1lnndo9x():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('doc1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('doc2', {'tag2', 'tag3'}, [('key2', 'value2'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('tag2 or key3:value3') == {'doc1', 'doc2'}


def test_example_jbn1r6ra():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('doc1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('doc2', {'tag2', 'tag3'}, [('key2', 'value2'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('not (tag1 and key1:value1)') == {'doc2'}


def test_example_i108cb3j():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('doc1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('doc2', {'tag2', 'tag3'}, [('key2', 'value2'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('tag2 and (key1:value1 or key3:value3)') == {'doc1', 'doc2'}


