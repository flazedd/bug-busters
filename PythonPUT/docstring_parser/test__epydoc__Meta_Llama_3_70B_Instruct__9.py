from common import ParseError
import epydoc as module_0
from common import DocstringStyle
from common import DocstringReturns
import inspect
import typing
import re
from common import RenderingStyle
from common import DocstringParam
from common import Docstring
import pytest
from common import DocstringMeta
from common import DocstringRaises
def test_example_4gs1t0pt():
    text = '\n    This is a short description.\n\n    This is a long description that spans multiple lines.\n    It can be formatted with blank lines.\n\n    @param foo: This is a parameter description.\n    @param bar: This is another parameter description.\n    @return: This is a return description.\n    @raise ValueError: This is a raise description.\n    @meta info: This is a meta description.\n    '
    docstring = module_0.parse(text)
    assert docstring.short_description == 'This is a short description.'
    assert docstring.long_description == 'This is a long description that spans multiple lines.\nIt can be formatted with blank lines.'
    assert len(docstring.meta) == 5
    assert isinstance(docstring.meta[0], module_0.DocstringParam)
    assert isinstance(docstring.meta[1], module_0.DocstringParam)
    assert isinstance(docstring.meta[2], module_0.DocstringReturns)
    assert isinstance(docstring.meta[3], module_0.DocstringRaises)
    assert isinstance(docstring.meta[4], module_0.DocstringMeta)
    rendered_docstring = module_0.compose(docstring)
    assert rendered_docstring.startswith('This is a short description.')








def test_example_8mj2f6j5():
    text = '\n    This is a short description.\n\n    This is a long description that spans multiple lines.\n    It can be formatted with blank lines.\n\n    @param foo: This is a parameter description with a default value, defaults to 10.\n    @return: This is a return description.\n    @raise ValueError: This is a raise description.\n    @meta info: This is a meta description.\n    '
    docstring = module_0.parse(text)
    assert docstring.short_description == 'This is a short description.'
    assert docstring.long_description == 'This is a long description that spans multiple lines.\nIt can be formatted with blank lines.'
    assert len(docstring.meta) == 4
    assert isinstance(docstring.meta[0], module_0.DocstringParam)
    assert docstring.meta[0].default == '10'
    assert isinstance(docstring.meta[1], module_0.DocstringReturns)
    assert isinstance(docstring.meta[2], module_0.DocstringRaises)
    assert isinstance(docstring.meta[3], module_0.DocstringMeta)
    rendered_docstring = module_0.compose(docstring, rendering_style=module_0.RenderingStyle.CLEAN)
    assert 'defaults to 10' in rendered_docstring








def test_example_s1mqurmb():
    text = '\n    This is a short description.\n\n    This is a long description that spans multiple lines.\n    It can be formatted with blank lines.\n\n    @param foo: This is a parameter description with a default value, defaults to 10.\n    @param bar: This is another parameter description with a default value, defaults to 20.\n    @return: This is a return description.\n    @raise ValueError: This is a raise description.\n    @meta info: This is a meta description.\n    '
    docstring = module_0.parse(text)
    assert docstring.short_description == 'This is a short description.'
    assert docstring.long_description == 'This is a long description that spans multiple lines.\nIt can be formatted with blank lines.'
    assert len(docstring.meta) == 5
    assert isinstance(docstring.meta[0], module_0.DocstringParam)
    assert docstring.meta[0].default == '10'
    assert isinstance(docstring.meta[1], module_0.DocstringParam)
    assert docstring.meta[1].default == '20'
    assert isinstance(docstring.meta[2], module_0.DocstringReturns)
    assert isinstance(docstring.meta[3], module_0.DocstringRaises)
    assert isinstance(docstring.meta[4], module_0.DocstringMeta)
    rendered_docstring = module_0.compose(docstring, rendering_style=module_0.RenderingStyle.EXPANDED, indent='    ')
    assert 'defaults to 10' in rendered_docstring
    assert 'defaults to 20' in rendered_docstring








def test_example_ahaxk2ek():
    text = 'This is a test docstring.\n\n    It has multiple lines.\n\n    @param foo: This is a parameter.\n    @type foo: int\n    @return: This is the return value.\n    @rtype: str\n    @raise ValueError: This is an error.\n    '
    docstring = module_0.parse(text)
    assert docstring.short_description == 'This is a test docstring.'


def test_example_c3f8zte9():
    text = 'This is a test docstring.\n\n    It has multiple lines.\n\n    @param foo: This is a parameter.\n    @type foo: int\n    @param bar: This is another parameter.\n    @type bar: float?\n    @return: This is the return value.\n    @rtype: str\n    @raise ValueError: This is an error.\n    @raise TypeError: This is another error.\n    '
    docstring = module_0.parse(text)
    assert isinstance(docstring.meta[0], module_0.DocstringParam)


def test_example_vcpmcir5():
    text = 'This is a test docstring.\n\n    It has multiple lines.\n\n    @keyword baz: This is a keyword parameter.\n    @type baz: str\n    @return: This is the return value.\n    @rtype: int\n    @raise RuntimeError: This is an error.\n    '
    docstring = module_0.parse(text)
    assert isinstance(docstring.meta[0], module_0.DocstringParam)


def test_example_l79tua6t():
    text = 'This is a test docstring.\n\n    It has multiple lines.\n\n    @param spam: This is a parameter.\n    @type spam: list\n    @param eggs: This is another parameter.\n    @type eggs: dict?\n    @return: This is the return value.\n    @rtype: tuple\n    @raise IndexError: This is an error.\n    @raise KeyError: This is another error.\n    '
    docstring = module_0.parse(text)
    assert len([meta for meta in docstring.meta if isinstance(meta, module_0.DocstringParam)]) == 2


def test_example_u4cfpxi5():
    text = 'This is a test docstring.\n\n    It has multiple lines.\n\n    @param eggs: This is a parameter.\n    @type eggs: dict\n    @return: This is the return value.\n    @rtype: list\n    @raise ValueError: This is an error.\n    @meta author: John Doe\n    @meta date: 2022-01-01\n    '
    docstring = module_0.parse(text)
    assert isinstance(docstring.meta[-1], module_0.DocstringMeta)


