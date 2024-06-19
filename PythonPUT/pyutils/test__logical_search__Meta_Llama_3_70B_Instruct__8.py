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
def test_example_d47edt1h():
    corpus = module_0.Corpus()
    doc = module_0.Document('docid1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    corpus.add_doc(doc)
    assert corpus.query('tag1 and key1:value1') == {'docid1'}


def test_example_yss29wbs():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('docid1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('docid2', {'tag1', 'tag3'}, [('key1', 'value1'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('tag1 or key1:value1') == {'docid1', 'docid2'}


def test_example_tmt1jsz8():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('docid1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('docid2', {'tag1', 'tag3'}, [('key1', 'value1'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('not tag3') == {'docid1'}


def test_example_n16ctixu():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('docid1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('docid2', {'tag1', 'tag3'}, [('key1', 'value1'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('tag1 and not tag3') == {'docid1'}


def test_example_21286svr():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('docid1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('docid2', {'tag1', 'tag3'}, [('key1', 'value1'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('key1:value1') == {'docid1', 'docid2'}


def test_example_fj0gx7ll():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('docid1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('docid2', {'tag1', 'tag3'}, [('key1', 'value1'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('tag1 and key1:*') == {'docid1', 'docid2'}


def test_example_aj91yh7w():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('docid1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('docid2', {'tag1', 'tag3'}, [('key1', 'value1'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('(tag1 and key1:value1) or tag2') == {'docid1', 'docid2'}


def test_example_1mp6iqez():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('docid1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('docid2', {'tag1', 'tag3'}, [('key1', 'value1'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('tag1 and (key1:value1 and not key2:value2)') == {'docid2'}


