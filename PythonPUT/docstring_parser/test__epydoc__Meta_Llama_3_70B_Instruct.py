import epydoc as module_0
from common import ParseError
import typing
from common import DocstringMeta
import re
from common import DocstringStyle
import inspect
from common import DocstringRaises
from common import Docstring
from common import DocstringParam
import pytest
from common import RenderingStyle
from common import DocstringReturns
def test_example_5a7trkyz():
    docstring = module_0.parse('\n    This is a short description.\n\n    This is a long description.\n\n    @param foo: This is a parameter description.\n    @return: This is a return description.\n    @raise ValueError: This is a raise description.\n    @meta bar: This is a meta description.\n    ')
    assert docstring.meta[0].arg_name == 'foo'


def test_example_3b0uzo6r():
    docstring = module_0.parse('\n    This is a short description.\n\n    @param baz: This is a parameter description with a default value, defaults to 5.\n    @return: This is a return description.\n    @raise TypeError: This is a raise description.\n    @meta qux: This is a meta description.\n    ')
    assert docstring.meta[0].default == '5'


def test_example_q80gnoog():
    docstring = module_0.parse('\n    This is a short description.\n\n    @param foo: This is a parameter description.\n    @param bar: This is another parameter description.\n    @return: This is a return description.\n    @raise ValueError: This is a raise description.\n    @meta baz: This is a meta description.\n    ')
    assert len(docstring.meta) == 5


def test_example_vua6x5m8():
    docstring = module_0.compose(module_0.parse('\n    This is a short description.\n\n    @param foo: This is a parameter description.\n    @return: This is a return description.\n    @raise ValueError: This is a raise description.\n    @meta baz: This is a meta description.\n    '), RenderingStyle.EXPANDED)
    assert '\n    ' in docstring


def test_example_u7wz6l6h():
    docstring = module_0.parse('\n    This is a short description.\n\n    @param foo: This is a parameter description with a default value, defaults to 10.\n    @return: This is a return description.\n    @raise ValueError: This is a raise description.\n    @meta baz: This is a meta description.\n    ')
    assert docstring.meta[0].default == '10'


def test_example_wuh8e95b():
    docstring = module_0.parse('\n    This is a short description.\n\n    @param foo: This is a parameter description with a type, str\n    @return: This is a return description.\n    @raise ValueError: This is a raise description.\n    @meta baz: This is a meta description.\n    ')
    assert docstring.meta[0].description == 'This is a parameter description with a type, str'


def test_example_dhzireyi():
    docstring = module_0.compose(module_0.parse('\n    This is a short description.\n\n    @param foo: This is a parameter description.\n    @return: This is a return description.\n    @raise ValueError: This is a raise description.\n    @meta baz: This is a meta description.\n    '), RenderingStyle.CLEAN)
    assert '@param foo:' in docstring


def test_example_a0prg4gv():
    docstring = module_0.parse('\n    This is a short description.\n\n    This is a long description.\n\n    @param foo: This is a parameter description.\n    @return: This is a return description.\n    @raise ValueError: This is a raise description.\n    @meta baz: This is a meta description.\n    ')
    assert docstring.short_description == 'This is a short description.'


