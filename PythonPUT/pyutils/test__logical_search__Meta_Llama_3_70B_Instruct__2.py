import logical_search as module_0
import pytest
def test_example_spq8quxo():
    corpus = module_0.Corpus()
    doc = module_0.Document('doc1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    corpus.add_doc(doc)
    assert corpus.query('tag1 and key1:value1') == {'doc1'}


def test_example_zeuu6gu3():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('doc1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('doc2', {'tag2', 'tag3'}, [('key2', 'value2'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('tag2 or key2:value2') == {'doc1', 'doc2'}


def test_example_vwrcq09s():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('doc1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('doc2', {'tag2', 'tag3'}, [('key2', 'value2'), ('key3', 'value3')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    assert corpus.query('not tag3') == {'doc1'}


def test_example_s4robxxq():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('doc1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('doc2', {'tag2', 'tag3'}, [('key2', 'value2'), ('key3', 'value3')])
    doc3 = module_0.Document('doc3', {'tag3', 'tag4'}, [('key3', 'value3'), ('key4', 'value4')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    corpus.add_doc(doc3)
    assert corpus.query('(tag2 or key2:value2) and not tag3') == {'doc1'}


def test_example_fon88rpv():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('doc1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('doc2', {'tag2', 'tag3'}, [('key2', 'value2'), ('key3', 'value3')])
    doc3 = module_0.Document('doc3', {'tag3', 'tag4'}, [('key3', 'value3'), ('key4', 'value4')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    corpus.add_doc(doc3)
    assert corpus.query('tag2 and (key2:value2 or key3:value3)') == {'doc1', 'doc2'}


def test_example_atl45ehe():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('doc1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('doc2', {'tag2', 'tag3'}, [('key2', 'value2'), ('key3', 'value3')])
    doc3 = module_0.Document('doc3', {'tag3', 'tag4'}, [('key3', 'value3'), ('key4', 'value4')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    corpus.add_doc(doc3)
    assert corpus.query('tag2 and not key3:value3') == {'doc1'}


def test_example_wd71r4db():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('doc1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('doc2', {'tag2', 'tag3'}, [('key2', 'value2'), ('key3', 'value3')])
    doc3 = module_0.Document('doc3', {'tag3', 'tag4'}, [('key3', 'value3'), ('key4', 'value4')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    corpus.add_doc(doc3)
    assert corpus.query('tag2 or key2:value2') == {'doc1', 'doc2'}


def test_example_qxiwxbhd():
    corpus = module_0.Corpus()
    doc1 = module_0.Document('doc1', {'tag1', 'tag2'}, [('key1', 'value1'), ('key2', 'value2')])
    doc2 = module_0.Document('doc2', {'tag2', 'tag3'}, [('key2', 'value2'), ('key3', 'value3')])
    doc3 = module_0.Document('doc3', {'tag3', 'tag4'}, [('key3', 'value3'), ('key4', 'value4')])
    corpus.add_doc(doc1)
    corpus.add_doc(doc2)
    corpus.add_doc(doc3)
    assert corpus.query('(tag2 or key2:value2) and not tag3') == {'doc1'}


