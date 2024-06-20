from __future__ import annotations
from typing import Dict
from typing import Union
from typing import List
from typing import Optional
from typing import Tuple
from typing import Any
import logical_search as module_0
from collections import defaultdict
from __exceptions import PyUtilsParseError
import doctest
from typing import Sequence
from dataclasses import field
from dataclasses import dataclass
import logging
import enum
import pytest
from typing import Set
def test_example_6r2cip2s():
    corpus = module_0.Corpus()
    doc = module_0.Document('doc1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    corpus.add_doc(doc)
    assert corpus.query('tag1 and tag2') == {'doc1'}


def test_example_fd94npj5():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('doc1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('doc2', {'tag2', 'tag3'}, [('key2', 'value2'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('tag2') == {'doc1', 'doc2'}


def test_example_yhj4gxih():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('doc1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('doc2', {'tag2', 'tag3'}, [('key2', 'value2'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('not tag3') == {'doc1'}


def test_example_tei085yf():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('doc1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('doc2', {'tag2', 'tag3'}, [('key2', 'value2'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('tag1 or tag3') == {'doc1', 'doc2'}


def test_example_ww4ajreu():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('doc1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('doc2', {'tag2', 'tag3'}, [('key2', 'value2'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('key1:value1') == {'doc1'}


def test_example_tnht050y():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('doc1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('doc2', {'tag2', 'tag3'}, [('key2', 'value2'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('tag2 and key2:value2') == {'doc1', 'doc2'}


def test_example_eqqoqk8e():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('doc1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('doc2', {'tag2', 'tag3'}, [('key2', 'value2'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('tag2 and not tag3') == {'doc1'}


def test_example_p7m4nrya():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('doc1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('doc2', {'tag2', 'tag3'}, [('key2', 'value2'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('key2:value2') == {'doc1', 'doc2'}


