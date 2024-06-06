from __future__ import annotations
from __exceptions import PyUtilsParseError
from typing import Tuple
import logical_search as module_0
import pytest
import enum
from dataclasses import field
from typing import Set
from collections import defaultdict
from typing import List
from typing import Dict
import logging
from typing import Sequence
import doctest
from dataclasses import dataclass
from typing import Any
from typing import Optional
from typing import Union
def test_example_ga4015we():
    corpus = module_0.Corpus()
    doc = module_0.Document(docid='test_doc', tags={'tag1', 'tag2'})
    corpus.add_doc(doc)
    assert 'test_doc' in corpus.query('tag1')


def test_example_w53qb27l():
    corpus = module_0.Corpus()
    doc1 = module_0.Document(docid='doc1', properties=[('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document(docid='doc2', properties=[('key1', 'value1'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert 'doc1' in corpus.query('key1:value1')
    assert 'doc2' in corpus.query('key1:value1')
    assert 'doc1' not in corpus.query('key3:value3')


def test_example_iio4cprt():
    corpus = module_0.Corpus()
    doc1 = module_0.Document(docid='doc1', tags={'tag1', 'tag2'})
    doc2 = module_0.Document(docid='doc2', tags={'tag2', 'tag3'})
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert 'doc1' in corpus.query('tag1 or tag2')
    assert 'doc2' in corpus.query('tag1 or tag2')
    assert 'doc1' not in corpus.query('tag3')


def test_example_7d7v840d():
    corpus = module_0.Corpus()
    doc1 = module_0.Document(docid='doc1', tags={'tag1', 'tag2'})
    doc2 = module_0.Document(docid='doc2', tags={'tag2', 'tag3'})
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert 'doc1' not in corpus.query('not tag1')
    assert 'doc2' in corpus.query('not tag1')


def test_example_bi3h0fls():
    corpus = module_0.Corpus()
    doc1 = module_0.Document(docid='doc1', tags={'tag1', 'tag2'})
    doc2 = module_0.Document(docid='doc2', tags={'tag2', 'tag3'})
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert 'doc1' in corpus.query('tag1 and tag2')
    assert 'doc2' not in corpus.query('tag1 and tag2')


def test_example_6o6qg8xv():
    corpus = module_0.Corpus()
    doc1 = module_0.Document(docid='doc1', properties=[('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document(docid='doc2', properties=[('key1', 'value1'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert 'doc1' in corpus.query('key1:value1 and key2:value2')
    assert 'doc2' not in corpus.query('key1:value1 and key2:value2')


def test_example_8i7jyzhd():
    corpus = module_0.Corpus()
    doc1 = module_0.Document(docid='doc1', tags={'tag1', 'tag2'})
    doc2 = module_0.Document(docid='doc2', tags={'tag2', 'tag3'})
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert 'doc1' in corpus.query('(tag1 or tag2) and not tag3')
    assert 'doc2' not in corpus.query('(tag1 or tag2) and not tag3')


def test_example_5hlpyk0j():
    corpus = module_0.Corpus()
    doc1 = module_0.Document(docid='doc1', properties=[('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document(docid='doc2', properties=[('key1', 'value1'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert 'doc1' in corpus.query('key1:value1 or key2:value2')
    assert 'doc2' in corpus.query('key1:value1 or key2:value2')
    assert 'doc1' in corpus.query('key1:value1 or key3:value3')
    assert 'doc2' in corpus.query('key1:value1 or key3:value3')


