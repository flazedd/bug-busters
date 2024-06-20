from common import Docstring
import pytest
import epydoc as module_0
from common import RenderingStyle
import typing
from common import ParseError
from common import DocstringReturns
from common import DocstringRaises
from common import DocstringStyle
from common import DocstringMeta
import re
from common import DocstringParam
import inspect
def test_example_fjljd4ur():
    text = 'This is a sample docstring.\n\n    It has multiple lines.\n\n    @param foo: This is a param.\n    @return: This is a return value.\n    @raise ValueError: This is a raised error.\n    '
    docstring = module_0.parse(text)
    rendered_docstring = module_0.compose(docstring)
    assert rendered_docstring.startswith('This is a sample docstring.')


def test_example_o41ufrtl():
    text = 'This is a sample docstring with a short description.\n\n    This is a long description.\n\n    @param bar: This is a param with a default value, defaults to 10.\n    @type bar: int\n    @return: This is a return value.\n    @raise TypeError: This is a raised error.\n    '
    docstring = module_0.parse(text)
    rendered_docstring = module_0.compose(docstring)
    assert 'defaults to 10' in rendered_docstring


def test_example_vo7f1sp9():
    text = 'This is a sample docstring with a yield.\n\n    @yield: This is a generator.\n    @param baz: This is a param.\n    @raise RuntimeError: This is a raised error.\n    '
    docstring = module_0.parse(text)
    rendered_docstring = module_0.compose(docstring)
    assert '@yield:' in rendered_docstring


def test_example_cdqp91az():
    text = 'This is a sample docstring with a meta tag.\n\n    @meta author: John Doe\n    @param bar: This is a param.\n    @return: This is a return value.\n    '
    docstring = module_0.parse(text)
    rendered_docstring = module_0.compose(docstring)
    assert '@meta author: John Doe' in rendered_docstring


def test_example_8oofiex9():
    text = 'This is a sample docstring with a type.\n\n    @param foo: This is a param.\n    @type foo: int\n    @return: This is a return value.\n    '
    docstring = module_0.parse(text)
    rendered_docstring = module_0.compose(docstring)
    assert '@type foo: int' in rendered_docstring


def test_example_hz0r67ne():
    text = 'This is a sample docstring with multiple params.\n\n    @param foo: This is a param.\n    @param bar: This is another param.\n    @return: This is a return value.\n    '
    docstring = module_0.parse(text)
    rendered_docstring = module_0.compose(docstring)
    assert '@param foo: This is a param.' in rendered_docstring
    assert '@param bar: This is another param.' in rendered_docstring


def test_example_zd5lg10h():
    text = 'This is a sample docstring with an optional param.\n\n    @param foo?: This is an optional param.\n    @return: This is a return value.\n    '
    docstring = module_0.parse(text)
    rendered_docstring = module_0.compose(docstring)
    assert '@param foo?: This is an optional param.' in rendered_docstring


def test_example_4ivt3ah8():
    text = 'This is a sample docstring with a long description.\n\n    This is a long description that spans multiple lines.\n\n    @param foo: This is a param.\n    @return: This is a return value.\n    '
    docstring = module_0.parse(text)
    rendered_docstring = module_0.compose(docstring)
    assert 'This is a long description that spans multiple lines.' in rendered_docstring


