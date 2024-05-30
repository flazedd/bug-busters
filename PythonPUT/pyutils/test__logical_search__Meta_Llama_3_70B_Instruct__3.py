from __future__ import annotations
from __exceptions import PyUtilsParseError
from typing import Any
from typing import List
from dataclasses import dataclass
import pytest
from dataclasses import field
from typing import Sequence
from typing import Optional
from collections import defaultdict
from typing import Set
import logical_search as module_0
import doctest
from typing import Union
import logging
import enum
from typing import Tuple
from typing import Dict
def test_example_ugsjqjxn():
    corpus = module_0.Corpus()
    doc = module_0.Document(docid='doc1', tags=['tag1', 'tag2'], properties=[('key', 'value')])
    corpus.add_doc(doc)
    assert corpus.query('tag1') == {'doc1'}


def test_example_dzfnxomk():
    corpus = module_0.Corpus()
    doc1 = module_0.Document(docid='doc1', tags=['tag1', 'tag2'], properties=[('key', 'value1')])
    doc2 = module_0.Document(docid='doc2', tags=['tag1', 'tag3'], properties=[('key', 'value2')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('tag1 and key:value1') == {'doc1'}


def test_example_x53hnp3z():
    corpus = module_0.Corpus()
    doc1 = module_0.Document(docid='doc1', tags=['tag1', 'tag2'], properties=[('key', 'value1')])
    doc2 = module_0.Document(docid='doc2', tags=['tag1', 'tag3'], properties=[('key', 'value2')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('not tag3') == {'doc1'}


def test_example_9eb3q15d():
    corpus = module_0.Corpus()
    doc1 = module_0.Document(docid='doc1', tags=['tag1', 'tag2'], properties=[('key', 'value1')])
    doc2 = module_0.Document(docid='doc2', tags=['tag1', 'tag3'], properties=[('key', 'value2')])
    doc3 = module_0.Document(docid='doc3', tags=['tag4'], properties=[('key', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    corpus.add_doc(doc3)
    assert corpus.query('tag1 or tag4') == {'doc1', 'doc2', 'doc3'}


def test_example_wcoycutm():
    corpus = module_0.Corpus()
    doc1 = module_0.Document(docid='doc1', tags=['tag1', 'tag2'], properties=[('key', 'value1')])
    doc2 = module_0.Document(docid='doc2', tags=['tag1', 'tag3'], properties=[('key', 'value2')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('tag1 and not tag3') == {'doc1'}


def test_example_dsezcwi3():
    corpus = module_0.Corpus()
    doc1 = module_0.Document(docid='doc1', tags=['tag1', 'tag2'], properties=[('key', 'value1')])
    doc2 = module_0.Document(docid='doc2', tags=['tag1', 'tag3'], properties=[('key', 'value2')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('key:value1') == {'doc1'}


def test_example_cisxv0d0():
    corpus = module_0.Corpus()
    doc1 = module_0.Document(docid='doc1', tags=['tag1', 'tag2'], properties=[('key', 'value1')])
    doc2 = module_0.Document(docid='doc2', tags=['tag1', 'tag3'], properties=[('key', 'value2')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('tag1 and (key:value1 or key:value2)') == {'doc1', 'doc2'}


def test_example_eqfpa8ix():
    corpus = module_0.Corpus()
    doc1 = module_0.Document(docid='doc1', tags=['tag1', 'tag2'], properties=[('key', 'value1')])
    doc2 = module_0.Document(docid='doc2', tags=['tag1', 'tag3'], properties=[('key', 'value2')])
    doc3 = module_0.Document(docid='doc3', tags=['tag4'], properties=[('key', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    corpus.add_doc(doc3)
    assert corpus.query('not (tag1 and key:value1)') == {'doc2', 'doc3'}


