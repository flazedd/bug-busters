from __future__ import annotations
from dataclasses import field
import pytest
from typing import List
from typing import Optional
from typing import Tuple
from typing import Any
from typing import Dict
import doctest
import logical_search as module_0
from collections import defaultdict
import enum
from typing import Sequence
import logging
from typing import Set
from typing import Union
from dataclasses import dataclass
from __exceptions import PyUtilsParseError
def test_example_ro0o1c4r():
    corpus = module_0.Corpus()
    doc = module_0.Document('doc1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    corpus.add_doc(doc)
    assert corpus.query('tag1') == {'doc1'}


def test_example_mr66jdup():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('doc1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('doc2', {'tag1', 'tag3'}, [('key1', 'value1'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('tag1 and not tag2') == {'doc2'}


def test_example_coipoggb():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('doc1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('doc2', {'tag1', 'tag3'}, [('key1', 'value1'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('key1:value1') == {'doc1', 'doc2'}


def test_example_s6a3u652():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('doc1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('doc2', {'tag1', 'tag3'}, [('key1', 'value1'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('tag1 or tag3') == {'doc1', 'doc2'}


def test_example_shfl9o3b():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('doc1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('doc2', {'tag1', 'tag3'}, [('key1', 'value1'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('key1:value1 and tag1') == {'doc1', 'doc2'}


def test_example_fbu30l9s():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('doc1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('doc2', {'tag1', 'tag3'}, [('key1', 'value1'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('not tag2') == {'doc2'}


def test_example_qdcvt8gd():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('doc1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('doc2', {'tag1', 'tag3'}, [('key1', 'value1'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('tag1 and (key1:value1 or key3:value3)') == {'doc1', 'doc2'}


def test_example_zwe25poe():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('doc1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('doc2', {'tag1', 'tag3'}, [('key1', 'value1'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('(tag1 and key1:value1) or tag3') == {'doc1', 'doc2'}


