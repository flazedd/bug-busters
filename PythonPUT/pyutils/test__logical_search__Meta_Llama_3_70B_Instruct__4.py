from __future__ import annotations
from typing import List
from typing import Tuple
from __exceptions import PyUtilsParseError
import doctest
import pytest
from dataclasses import dataclass
from typing import Any
from typing import Sequence
from typing import Optional
from dataclasses import field
from typing import Union
import logging
import enum
from collections import defaultdict
import logical_search as module_0
from typing import Set
from typing import Dict
def test_example_sn5frq6g():
    corpus = module_0.Corpus()
    doc = module_0.Document('docid1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    corpus.add_doc(doc)
    assert corpus.query('tag1') == {'docid1'}


def test_example_fdyprusa():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('docid1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('docid2', {'tag2', 'tag3'}, [('key2', 'value2'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('tag1 or tag3') == {'docid1', 'docid2'}


def test_example_yr5cm8li():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('docid1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('docid2', {'tag2', 'tag3'}, [('key2', 'value2'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('not tag3') == {'docid1'}


def test_example_tgv40hu3():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('docid1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('docid2', {'tag2', 'tag3'}, [('key2', 'value2'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('key1:value1') == {'docid1'}


def test_example_bn0sk9jo():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('docid1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('docid2', {'tag2', 'tag3'}, [('key2', 'value2'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('tag2 and not tag3') == {'docid1'}


def test_example_fkpr868y():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('docid1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('docid2', {'tag2', 'tag3'}, [('key2', 'value2'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('key2:value2') == {'docid1', 'docid2'}


def test_example_1o5q9aqs():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('docid1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('docid2', {'tag2', 'tag3'}, [('key2', 'value2'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('tag1 or key2:value2') == {'docid1', 'docid2'}


def test_example_8nfmhz89():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('docid1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('docid2', {'tag2', 'tag3'}, [('key2', 'value2'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('(tag1 or tag2) and key2:value2') == {'docid1', 'docid2'}


