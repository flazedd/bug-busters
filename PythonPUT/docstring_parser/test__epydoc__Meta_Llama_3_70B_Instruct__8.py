from common import DocstringMeta
import epydoc as module_0
from common import RenderingStyle
from common import Docstring
from common import DocstringStyle
import inspect
from common import ParseError
import pytest
import typing
from common import DocstringParam
from common import DocstringRaises
from common import DocstringReturns
import re
def test_example_xjgd2qk1():
    docstring = module_0.parse('\n    This is a short description.\n\n    This is a long description.\n\n    @param foo: This is a parameter description.\n    @return: This is a return description.\n    @raise ValueError: This is a raise description.\n    @meta meta_key: This is a meta description.\n    ')
    rendered_docstring = module_0.compose(docstring)
    assert rendered_docstring == '\nThis is a short description.\n\nThis is a long description.\n\n@param foo: This is a parameter description.\n@return: This is a return description.\n@raise ValueError: This is a raise description.\n@meta meta_key: This is a meta description.\n'.strip()


def test_example_8nn1qqis():
    docstring = module_0.parse('\n    This is a short description.\n\n    This is a long description.\n\n    @param bar: This is a parameter description with a default value, defaults to 5.\n    @return: This is a return description with a type, -> int\n    @raise TypeError: This is a raise description.\n    @meta meta_key: This is a meta description.\n    ')
    rendered_docstring = module_0.compose(docstring)
    assert rendered_docstring == '\nThis is a short description.\n\nThis is a long description.\n\n@param bar: This is a parameter description with a default value, defaults to 5.\n@return: This is a return description with a type, -> int\n@raise TypeError: This is a raise description.\n@meta meta_key: This is a meta description.\n'.strip()


def test_example_osa1wlhb():
    docstring = module_0.parse('\n    This is a short description.\n\n    This is a long description.\n\n    @param baz: This is a parameter description with an optional type,?str\n    @return: This is a return description with a generator type, -> yield str\n    @raise RuntimeError: This is a raise description.\n    @meta meta_key: This is a meta description.\n    ')
    rendered_docstring = module_0.compose(docstring)
    assert rendered_docstring == '\nThis is a short description.\n\nThis is a long description.\n\n@param baz: This is a parameter description with an optional type,?str\n@return: This is a return description with a generator type, -> yield str\n@raise RuntimeError: This is a raise description.\n@meta meta_key: This is a meta description.\n'.strip()


def test_example_tss9opt1():
    docstring = module_0.parse('\n    This is a short description.\n\n    @param qux: This is a parameter description with multiple lines.\n                This is the second line.\n    @return: This is a return description.\n    @raise ValueError: This is a raise description.\n    @meta meta_key: This is a meta description.\n    ')
    rendered_docstring = module_0.compose(docstring)
    assert rendered_docstring == '\nThis is a short description.\n\n@param qux: This is a parameter description with multiple lines.\n    This is the second line.\n@return: This is a return description.\n@raise ValueError: This is a raise description.\n@meta meta_key: This is a meta description.\n'.strip()


def test_example_d8fqyx0i():
    docstring = module_0.parse('\n    This is a short description.\n\n    @param foo: This is a parameter description.\n    @return: This is a return description with multiple lines.\n             This is the second line.\n    @raise ValueError: This is a raise description.\n    @meta meta_key: This is a meta description.\n    ')
    rendered_docstring = module_0.compose(docstring)
    assert rendered_docstring == '\nThis is a short description.\n\n@param foo: This is a parameter description.\n@return: This is a return description with multiple lines.\n    This is the second line.\n@raise ValueError: This is a raise description.\n@meta meta_key: This is a meta description.\n'.strip()


def test_example_s134s5v5():
    docstring = module_0.parse('\n    This is a short description.\n\n    @param foo: This is a parameter description.\n    @param bar: This is another parameter description.\n    @return: This is a return description.\n    @raise ValueError: This is a raise description.\n    @meta meta_key: This is a meta description.\n    ')
    rendered_docstring = module_0.compose(docstring)
    assert rendered_docstring == '\nThis is a short description.\n\n@param foo: This is a parameter description.\n@param bar: This is another parameter description.\n@return: This is a return description.\n@raise ValueError: This is a raise description.\n@meta meta_key: This is a meta description.\n'.strip()


def test_example_u15yctkl():
    docstring = module_0.parse('\n    This is a short description.\n\n    @param foo: This is a parameter description with a type, str\n    @return: This is a return description with a type, -> str\n    @raise ValueError: This is a raise description.\n    @meta meta_key: This is a meta description.\n    ')
    rendered_docstring = module_0.compose(docstring)
    assert rendered_docstring == '\nThis is a short description.\n\n@param foo: This is a parameter description with a type, str\n@return: This is a return description with a type, -> str\n@raise ValueError: This is a raise description.\n@meta meta_key: This is a meta description.\n'.strip()


def test_example_qywwabpe():
    docstring = module_0.parse('\n    This is a short description.\n\n    @param foo: This is a parameter description.\n    @return: This is a return description.\n    @raise ValueError: This is a raise description.\n    @meta meta_key: This is a meta description with multiple lines.\n             This is the second line.\n    ')
    rendered_docstring = module_0.compose(docstring)
    assert rendered_docstring == '\nThis is a short description.\n\n@param foo: This is a parameter description.\n@return: This is a return description.\n@raise ValueError: This is a raise description.\n@meta meta_key: This is a meta description with multiple lines.\n    This is the second line.\n'.strip()


