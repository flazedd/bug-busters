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
def test_example_thzw0tuo():
    docstring = module_0.parse('\n    Short description.\n\n    Long description.\n\n    @param arg1: Description of arg1\n    @param arg2: Description of arg2\n    @return: Description of return value\n    @raise ValueError: Description of ValueError\n    @meta info: Some meta information\n    ')
    rendered_docstring = module_0.compose(docstring)
    assert 'Short description.\n\nLong description.\n\n@param arg1: Description of arg1\n@param arg2: Description of arg2\n@return: Description of return value\n@raise ValueError: Description of ValueError\n@meta info: Some meta information' == rendered_docstring











def test_example_1wdsi909():
    docstring = module_0.parse('\n    This is a short description.\n\n    This is a long description that spans multiple lines.\n    It has multiple sentences.\n\n    @param foo: This is a parameter\n    @param bar: This is another parameter\n    @return: This is the return value\n    @raise TypeError: This is an error\n    @meta info: This is some meta information\n    ')
    rendered_docstring = module_0.compose(docstring)
    assert 'This is a short description.\n\nThis is a long description that spans multiple lines.\nIt has multiple sentences.\n\n@param foo: This is a parameter\n@param bar: This is another parameter\n@return: This is the return value\n@raise TypeError: This is an error\n@meta info: This is some meta information' == rendered_docstring











def test_example_ps1ee5bs():
    docstring = module_0.parse('\n    Short description.\n\n    @param arg1: Description of arg1\n    @param arg2: Description of arg2 with default value, defaults to 10\n    @return: Description of return value\n    @raise ValueError: Description of ValueError\n    @meta info: Some meta information\n    ')
    rendered_docstring = module_0.compose(docstring)
    assert 'Short description.\n\n@param arg1: Description of arg1\n@param arg2: Description of arg2 with default value, defaults to 10\n@return: Description of return value\n@raise ValueError: Description of ValueError\n@meta info: Some meta information' == rendered_docstring











def test_example_hfqxfm9a():
    docstring = module_0.parse('\n    Short description.\n\n    @param arg1: Description of arg1\n    @param arg2?: Description of arg2\n    @return: Description of return value\n    @raise ValueError: Description of ValueError\n    @meta info: Some meta information\n    ')
    rendered_docstring = module_0.compose(docstring)
    assert 'Short description.\n\n@param arg1: Description of arg1\n@param arg2?: Description of arg2\n@return: Description of return value\n@raise ValueError: Description of ValueError\n@meta info: Some meta information' == rendered_docstring











def test_example_cejoyj8z():
    docstring_text = '\n    This is a short description.\n\n    This is a long description that spans multiple lines.\n\n    @param foo: This is a parameter description.\n    @type foo: int\n    @return: This is a return description.\n    @rtype: str\n    @raise ValueError: This is a raise description.\n    @meta author: John Doe\n    '
    parsed_docstring = module_0.parse(docstring_text)
    rendered_docstring = module_0.compose(parsed_docstring)
    assert rendered_docstring.startswith('This is a short description.')


def test_example_7402y9z2():
    docstring_text = '\n    This is a short description.\n\n    This is a long description that spans multiple lines.\n\n    @param bar: This is a parameter description.\n    @type bar: float?\n    @param baz: This is another parameter description.\n    @type baz: str\n    @return: This is a return description.\n    @rtype: list\n    @raise TypeError: This is a raise description.\n    @meta version: 1.0\n    '
    parsed_docstring = module_0.parse(docstring_text)
    rendered_docstring = module_0.compose(parsed_docstring, RenderingStyle.EXPANDED)
    assert 'This is a long description that spans multiple lines.' in rendered_docstring


def test_example_gkc9j5w2():
    docstring_text = '\n    This is a short description.\n\n    @param foo: This is a parameter description.\n    @type foo: int\n    @param bar: This is another parameter description.\n    @type bar: str\n    @return: This is a return description.\n    @rtype: list\n    @raise ValueError: This is a raise description.\n    @meta author: John Doe\n    @meta version: 1.0\n    '
    parsed_docstring = module_0.parse(docstring_text)
    rendered_docstring = module_0.compose(parsed_docstring, RenderingStyle.COMPACT)
    assert 'This is a short description.' in rendered_docstring


def test_example_za5i2xrv():
    docstring_text = '\n    This is a short description.\n\n    @param foo: This is a parameter description.\n    @type foo: int\n    @param bar: This is another parameter description.\n    @type bar: str\n    @return: This is a return description.\n    @rtype: list\n    @raise ValueError: This is a raise description.\n    @meta author: John Doe\n    @meta version: 1.0\n    @meta license: MIT\n    '
    parsed_docstring = module_0.parse(docstring_text)
    rendered_docstring = module_0.compose(parsed_docstring, RenderingStyle.CLEAN, indent='  ')
    assert 'This is a short description.' in rendered_docstring


