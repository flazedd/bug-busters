import common as module_0
import enum
import pytest
import typing
def test_example_6cgk3t8t():
    assert isinstance(module_0.DocstringStyle, enum.EnumMeta)


def test_example_tiveq448():
    assert isinstance(module_0.DocstringReturns('args', 'description', 'type_name', True), module_0.DocstringReturns)


def test_example_pzplbxrt():
    assert module_0.PARAM_KEYWORDS == {'param', 'parameter', 'arg', 'argument', 'attribute', 'key', 'keyword'}


def test_example_01nf1kew():
    assert isinstance(module_0.Docstring(), module_0.Docstring)


def test_example_5q06amyk():
    docstring = module_0.Docstring()
    docstring.short_description = 'short description'
    docstring.long_description = 'long description'
    assert docstring.description == 'short description\nlong description'


def test_example_r3j0il93():
    docstring = module_0.Docstring()
    docstring.meta = [module_0.DocstringParam(['arg'], 'description', 'arg_name', 'type_name', True, 'default')]
    assert len(docstring.params) == 1


def test_example_6fh0lu7j():
    docstring = module_0.Docstring()
    docstring.meta = [module_0.DocstringRaises(['raises'], 'description', 'type_name')]
    assert len(docstring.raises) == 1


def test_example_uphowb18():
    docstring = module_0.Docstring()
    docstring.meta = [module_0.DocstringReturns(['returns'], 'description', 'type_name', True)]
    assert docstring.returns is not None


