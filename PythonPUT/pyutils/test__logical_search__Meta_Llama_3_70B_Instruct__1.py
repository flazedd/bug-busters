from __future__ import annotations
from typing import List
from typing import Dict
from __exceptions import PyUtilsParseError
from dataclasses import dataclass
import logical_search as module_0
from collections import defaultdict
from typing import Union
from typing import Sequence
from typing import Optional
from dataclasses import field
from typing import Tuple
import logging
from typing import Set
import pytest
import enum
from typing import Any
import doctest
def test_example_7259rcvu():
    c = module_0.Corpus()
    doc = module_0.Document(docid='1', tags={'urgent', 'important'})
    c.add_doc(doc)
    assert c.query('urgent') == {'1'}


def test_example_opkuspna():
    c = module_0.Corpus()
    doc1 = module_0.Document(docid='1', properties=[('author', 'Scott')])
    doc2 = module_0.Document(docid='2', properties=[('author', 'John')])
    c.add_doc(doc1)
    c.add_doc(doc2)
    assert c.query('author:Scott') == {'1'}


def test_example_5mf9imu8():
    c = module_0.Corpus()
    doc1 = module_0.Document(docid='1', tags={'tag1', 'tag2'})
    doc2 = module_0.Document(docid='2', tags={'tag2', 'tag3'})
    c.add_doc(doc1)
    c.add_doc(doc2)
    assert c.query('tag2') == {'1', '2'}


def test_example_atnukmeg():
    c = module_0.Corpus()
    doc1 = module_0.Document(docid='1', properties=[('category', 'mystery')])
    doc2 = module_0.Document(docid='2', properties=[('category', 'thriller')])
    c.add_doc(doc1)
    c.add_doc(doc2)
    assert c.query('category:mystery') == {'1'}


def test_example_0c9z0m5i():
    c = module_0.Corpus()
    doc1 = module_0.Document(docid='1', tags={'tag1', 'tag2'}, properties=[('author', 'Scott')])
    doc2 = module_0.Document(docid='2', tags={'tag2', 'tag3'}, properties=[('author', 'John')])
    c.add_doc(doc1)
    c.add_doc(doc2)
    assert c.query('tag2 and author:Scott') == {'1'}


def test_example_m2ziob2d():
    c = module_0.Corpus()
    doc1 = module_0.Document(docid='1', tags={'urgent'})
    doc2 = module_0.Document(docid='2', tags={'important'})
    c.add_doc(doc1)
    c.add_doc(doc2)
    assert c.query('not urgent') == {'2'}


def test_example_qnozniwj():
    c = module_0.Corpus()
    doc1 = module_0.Document(docid='1', tags={'tag1', 'tag2'})
    doc2 = module_0.Document(docid='2', tags={'tag2', 'tag3'})
    doc3 = module_0.Document(docid='3', tags={'tag3', 'tag4'})
    c.add_doc(doc1)
    c.add_doc(doc2)
    c.add_doc(doc3)
    assert c.query('(tag2 or tag3) and not tag1') == {'2', '3'}


def test_example_pjyn3pve():
    c = module_0.Corpus()
    doc1 = module_0.Document(docid='1', properties=[('key', 'value1')])
    doc2 = module_0.Document(docid='2', properties=[('key', 'value2')])
    c.add_doc(doc1)
    c.add_doc(doc2)
    assert c.query('key:*') == {'1', '2'}


