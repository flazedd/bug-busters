import re
import typing
from common import DocstringMeta
from common import DocstringStyle
from common import DocstringParam
from common import ParseError
from common import RenderingStyle
from common import Docstring
from common import DocstringReturns
from common import DocstringRaises
import inspect
import epydoc as module_0
import pytest
def test_example_th1w1kxm():
    text = 'This is a test docstring.\n\n    It has a short description and a long description.\n\n    @param foo: This is a parameter\n    @param bar: This is another parameter\n    @return: This is the return value\n    @raise ValueError: This is an exception\n    '
    docstring = module_0.parse(text)
    assert docstring.style == module_0.DocstringStyle.EPYDOC


def test_example_oicr5606():
    text = 'This is a test docstring.\n\n    It has a short description and a long description.\n\n    @type baz: This is a type\n    @param qux: This is a parameter with a default value, defaults to 5\n    @return: This is the return value\n    @raise RuntimeError: This is an exception\n    '
    docstring = module_0.parse(text)
    assert len(docstring.meta) == 4


def test_example_t99xi7hh():
    text = 'This is a test docstring.\n\n    It has a short description and a long description.\n\n    @param foo: This is a parameter\n    @param bar: This is another parameter\n    @return: This is the return value\n    @raise ValueError: This is an exception\n    '
    docstring = module_0.parse(text)
    assert len([meta for meta in docstring.meta if isinstance(meta, module_0.DocstringParam)]) == 2


def test_example_6qdq0vw7():
    text = 'This is a test docstring.\n\n    It has a short description and a long description.\n\n    @param baz: This is a parameter with a default value, defaults to 5\n    @return: This is the return value\n    @raise RuntimeError: This is an exception\n    '
    docstring = module_0.parse(text)
    assert any((isinstance(meta, module_0.DocstringParam) and meta.default is not None for meta in docstring.meta))


def test_example_nhsz03ge():
    text = 'This is a test docstring.\n\n    It has a short description and a long description.\n\n    @param foo: This is a parameter\n    @return: This is the return value\n    @raise ValueError: This is an exception\n    '
    docstring = module_0.parse(text)
    assert docstring.short_description == 'This is a test docstring.'


def test_example_90bpe1op():
    text = 'This is a test docstring.\n\n    It has a short description and a long description.\n\n    @param foo: This is a parameter\n    @return: This is the return value\n    @raise ValueError: This is an exception\n    '
    docstring = module_0.parse(text)
    composed = module_0.compose(docstring)
    assert composed.startswith('This is a test docstring.')


def test_example_fzc2g2ol():
    text = 'This is a test docstring.\n\n    It has a short description and a long description.\n\n    @param foo: This is a parameter\n    @return: This is the return value\n    @raise ValueError: This is an exception\n    '
    docstring = module_0.parse(text)
    composed = module_0.compose(docstring, rendering_style=module_0.RenderingStyle.CLEAN)
    assert '@return:' in composed


def test_example_ih6n6g5o():
    text = 'This is a test docstring.\n\n    It has a short description and a long description.\n\n    @param foo: This is a parameter with a default value, defaults to 5\n    @return: This is the return value\n    @raise ValueError: This is an exception\n    '
    docstring = module_0.parse(text)
    composed = module_0.compose(docstring, rendering_style=module_0.RenderingStyle.COMPACT)
    assert 'defaults to 5' in composed


