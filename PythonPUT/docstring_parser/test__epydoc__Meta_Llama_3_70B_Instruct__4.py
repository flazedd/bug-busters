from common import DocstringMeta
import pytest
import inspect
from common import ParseError
import epydoc as module_0
from common import Docstring
from common import DocstringStyle
from common import RenderingStyle
from common import DocstringParam
from common import DocstringRaises
from common import DocstringReturns
import typing
import re
def test_example_b839c2dr():
    assert module_0.parse('This is a short description.\n\nThis is a long description.').short_description == 'This is a short description.'


def test_example_lybic9o7():
    docstring = '\n    This is a short description.\n\n    This is a long description.\n\n    @param arg1: This is a parameter description.\n    @param arg2: This is another parameter description.\n    @return: This is a return description.\n    @raise ValueError: This is a raise description.\n    '
    parsed_docstring = module_0.parse(docstring)
    assert len(parsed_docstring.meta) == 4


def test_example_5wluhcwo():
    docstring = '\n    This is a short description.\n\n    This is a long description.\n\n    @param arg1: This is a parameter description.\n    @type arg1: int\n    @param arg2: This is another parameter description.\n    @type arg2: str\n    @return: This is a return description.\n    @rtype: float\n    @raise ValueError: This is a raise description.\n    '
    parsed_docstring = module_0.parse(docstring)
    assert parsed_docstring.meta[0].type_name == 'int'
    assert parsed_docstring.meta[1].type_name == 'str'
    assert parsed_docstring.meta[2].type_name == 'float'


def test_example_74j2rw58():
    docstring = '\n    This is a short description.\n\n    This is a long description.\n\n    @param arg1: This is a parameter description. Defaults to 10.\n    @param arg2: This is another parameter description. Defaults to "hello".\n    '
    parsed_docstring = module_0.parse(docstring)
    assert 'Defaults to 10' in parsed_docstring.meta[0].description
    assert 'Defaults to "hello"' in parsed_docstring.meta[1].description


def test_example_438p37pr():
    docstring = '\n    This is a short description.\n\n    This is a long description.\n\n    @return: This is a return description.\n    @rtype: float\n    '
    parsed_docstring = module_0.parse(docstring)
    assert isinstance(parsed_docstring.meta[0], module_0.DocstringReturns)
    assert parsed_docstring.meta[0].type_name == 'float'


def test_example_6hg074i3():
    docstring = '\n    This is a short description.\n\n    This is a long description.\n\n    @raise ValueError: This is a raise description.\n    '
    parsed_docstring = module_0.parse(docstring)
    assert isinstance(parsed_docstring.meta[0], module_0.DocstringRaises)
    assert parsed_docstring.meta[0].type_name == 'ValueError'


def test_example_7xdseyn7():
    docstring = '\n    This is a short description.\n\n    This is a long description.\n\n    @param arg1: This is a parameter description.\n    @type arg1: int?\n    '
    parsed_docstring = module_0.parse(docstring)
    assert parsed_docstring.meta[0].is_optional


def test_example_13sq52y4():
    docstring = '\n    This is a short description.\n\n    This is a long description.\n\n    @param arg1: This is a parameter description.\n    @param arg2: This is another parameter description.\n    '
    parsed_docstring = module_0.parse(docstring)
    assert len(parsed_docstring.meta) == 2
    assert isinstance(parsed_docstring.meta[0], module_0.DocstringParam)
    assert isinstance(parsed_docstring.meta[1], module_0.DocstringParam)


