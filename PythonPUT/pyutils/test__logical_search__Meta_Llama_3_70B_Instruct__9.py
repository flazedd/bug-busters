from __future__ import annotations
import logical_search as module_0
from dataclasses import dataclass
from __exceptions import PyUtilsParseError
import doctest
from typing import Optional
from dataclasses import field
import logging
import enum
from typing import Dict
from typing import Sequence
from typing import Any
from typing import List
from typing import Tuple
from typing import Set
import pytest
from typing import Union
from collections import defaultdict
def test_example_5x1n3gzw():
    corpus = module_0.Corpus()
    doc = module_0.Document(docid='doc1', tags={'tag1', 'tag2'}, properties=[('key1', 'value1')])
    corpus.add_doc(doc)
    assert corpus.query('tag1') == {'doc1'}


def test_example_4axh0v4j():
    corpus = module_0.Corpus()
    doc1 = module_0.Document(docid='doc1', tags={'tag1', 'tag2'}, properties=[('key1', 'value1')])
    doc2 = module_0.Document(docid='doc2', tags={'tag2', 'tag3'}, properties=[('key2', 'value2')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('tag1 and tag2') == {'doc1'}


def test_example_fr8nt4kw():
    corpus = module_0.Corpus()
    doc1 = module_0.Document(docid='doc1', tags={'tag1', 'tag2'}, properties=[('key1', 'value1')])
    doc2 = module_0.Document(docid='doc2', tags={'tag2', 'tag3'}, properties=[('key2', 'value2')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('not tag3') == {'doc1'}


def test_example_645nugkp():
    corpus = module_0.Corpus()
    doc1 = module_0.Document(docid='doc1', tags={'tag1', 'tag2'}, properties=[('key1', 'value1')])
    doc2 = module_0.Document(docid='doc2', tags={'tag2', 'tag3'}, properties=[('key2', 'value2')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('tag1 or tag3') == {'doc1', 'doc2'}


def test_example_qujsg3fd():
    corpus = module_0.Corpus()
    doc1 = module_0.Document(docid='doc1', tags={'tag1', 'tag2'}, properties=[('key1', 'value1')])
    doc2 = module_0.Document(docid='doc2', tags={'tag2', 'tag3'}, properties=[('key2', 'value2')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('key1:value1') == {'doc1'}


def test_example_gjm2ech6():
    corpus = module_0.Corpus()
    doc1 = module_0.Document(docid='doc1', tags={'tag1', 'tag2'}, properties=[('key1', 'value1')])
    doc2 = module_0.Document(docid='doc2', tags={'tag2', 'tag3'}, properties=[('key2', 'value2')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('tag2 and not tag3') == {'doc1'}


def test_example_kcw9sd76():
    corpus = module_0.Corpus()
    doc1 = module_0.Document(docid='doc1', tags={'tag1', 'tag2'}, properties=[('key1', 'value1')])
    doc2 = module_0.Document(docid='doc2', tags={'tag2', 'tag3'}, properties=[('key2', 'value2')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('key1:*') == {'doc1'}


def test_example_r230pt1z():
    corpus = module_0.Corpus()
    doc1 = module_0.Document(docid='doc1', tags={'tag1', 'tag2'}, properties=[('key1', 'value1')])
    doc2 = module_0.Document(docid='doc2', tags={'tag2', 'tag3'}, properties=[('key2', 'value2')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('tag1 or (tag2 and not tag3)') == {'doc1'}


