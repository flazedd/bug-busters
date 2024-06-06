from __future__ import annotations
from typing import Tuple
from dataclasses import field
from typing import Union
from typing import Set
import logical_search as module_0
from collections import defaultdict
import pytest
from typing import Optional
from typing import Any
from dataclasses import dataclass
from __exceptions import PyUtilsParseError
from typing import Sequence
from typing import List
import doctest
from typing import Dict
import logging
import enum
def test_example_rd1a41hj():
    corpus = module_0.Corpus()
    doc = module_0.Document(docid='doc1', tags={'tag1', 'tag2'}, properties=[('key', 'value')])
    corpus.add_doc(doc)
    assert corpus.query('tag1') == {'doc1'}


def test_example_pm9ap3iv():
    corpus = module_0.Corpus()
    doc1 = module_0.Document(docid='doc1', tags={'tag1', 'tag2'}, properties=[('key', 'value')])
    doc2 = module_0.Document(docid='doc2', tags={'tag2', 'tag3'}, properties=[('key', 'value2')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('tag1 or tag3') == {'doc1', 'doc2'}


def test_example_yy8l2can():
    corpus = module_0.Corpus()
    doc1 = module_0.Document(docid='doc1', tags={'tag1', 'tag2'}, properties=[('key', 'value')])
    doc2 = module_0.Document(docid='doc2', tags={'tag2', 'tag3'}, properties=[('key', 'value2')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('tag1 and not tag3') == {'doc1'}


def test_example_yt6y9v98():
    corpus = module_0.Corpus()
    doc1 = module_0.Document(docid='doc1', tags={'tag1', 'tag2'}, properties=[('key', 'value')])
    doc2 = module_0.Document(docid='doc2', tags={'tag2', 'tag3'}, properties=[('key', 'value2')])
    doc3 = module_0.Document(docid='doc3', tags={'tag3', 'tag4'}, properties=[('key', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    corpus.add_doc(doc3)
    assert corpus.query('(tag1 or tag2) and not tag3') == {'doc1'}


def test_example_2ja4ghnk():
    corpus = module_0.Corpus()
    doc1 = module_0.Document(docid='doc1', tags={'tag1', 'tag2'}, properties=[('key', 'value')])
    doc2 = module_0.Document(docid='doc2', tags={'tag2', 'tag3'}, properties=[('key', 'value2')])
    doc3 = module_0.Document(docid='doc3', tags={'tag3', 'tag4'}, properties=[('key', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    corpus.add_doc(doc3)
    assert corpus.query('tag2 and (tag1 or tag3)') == {'doc1', 'doc2'}


def test_example_ympiv1cl():
    corpus = module_0.Corpus()
    doc1 = module_0.Document(docid='doc1', tags={'tag1', 'tag2'}, properties=[('key', 'value')])
    doc2 = module_0.Document(docid='doc2', tags={'tag2', 'tag3'}, properties=[('key', 'value2')])
    doc3 = module_0.Document(docid='doc3', tags={'tag3', 'tag4'}, properties=[('key', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    corpus.add_doc(doc3)
    assert corpus.query('not (tag1 or tag4)') == {'doc2'}


def test_example_gxtvg0lj():
    corpus = module_0.Corpus()
    doc1 = module_0.Document(docid='doc1', tags={'tag1', 'tag2'}, properties=[('key', 'value')])
    doc2 = module_0.Document(docid='doc2', tags={'tag2', 'tag3'}, properties=[('key', 'value2')])
    doc3 = module_0.Document(docid='doc3', tags={'tag3', 'tag4'}, properties=[('key', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    corpus.add_doc(doc3)
    assert corpus.query('key:value') == {'doc1'}


def test_example_b3rtx2og():
    corpus = module_0.Corpus()
    doc1 = module_0.Document(docid='doc1', tags={'tag1', 'tag2'}, properties=[('key', 'value')])
    doc2 = module_0.Document(docid='doc2', tags={'tag2', 'tag3'}, properties=[('key', 'value2')])
    doc3 = module_0.Document(docid='doc3', tags={'tag3', 'tag4'}, properties=[('key', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    corpus.add_doc(doc3)
    assert corpus.query('key:*') == {'doc1', 'doc2', 'doc3'}


