from common import Docstring
import pytest
from enum import IntEnum
from collections import namedtuple
from common import RenderingStyle
import typing
from common import YIELDS_KEYWORDS
from common import ParseError
from common import PARAM_KEYWORDS
from collections import OrderedDict
from common import DocstringStyle
from common import DocstringRaises
from common import DocstringMeta
from common import EXAMPLES_KEYWORDS
import re
from common import RAISES_KEYWORDS
from common import DocstringParam
from common import DocstringExample
from common import RETURNS_KEYWORDS
from common import DocstringReturns
import google as module_0
import inspect
def test_example_lwjilkj6():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n    This is a test docstring.\n\n    Args:\n        arg1: This is the first argument.\n        arg2: This is the second argument.\n\n    Returns:\n        This is the return value.\n\n    Raises:\n        ValueError: This is the error message.\n    ')
    assert isinstance(docstring, module_0.Docstring)


def test_example_hnqbeiwo():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n    This is a test docstring.\n\n    Examples:\n        This is an example.\n\n    Attributes:\n        attr1: This is the first attribute.\n        attr2: This is the second attribute.\n    ')
    assert len(docstring.meta) == 3


def test_example_he8cvvv0():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n    This is a test docstring.\n\n    Yields:\n        This is the yield value.\n\n    Raises:\n        TypeError: This is the error message.\n    ')
    assert any((isinstance(meta, module_0.DocstringReturns) for meta in docstring.meta))


def test_example_o795jly6():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n    This is a test docstring.\n\n    Parameters:\n        param1 (int): This is the first parameter.\n        param2 (str): This is the second parameter.\n\n    Returns:\n        This is the return value.\n    ')
    assert any((isinstance(meta, module_0.DocstringParam) for meta in docstring.meta))


def test_example_qoq3i02h():
    parser = module_0.GoogleParser()
    docstring = parser.parse("\n    This is a test docstring.\n\n    Args:\n        arg1: This is the first argument with default value. Defaults to 10.\n        arg2: This is the second argument with default value. Defaults to 'hello'.\n\n    Returns:\n        This is the return value.\n    ")
    assert any((meta.default == '10' or meta.default == "'hello'" for meta in docstring.meta))


def test_example_r4ywecly():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n    This is a test docstring.\n\n    Attributes:\n        attr1: This is the first attribute.\n        attr2: This is the second attribute with default value. Defaults to 20.\n\n    Returns:\n        This is the return value.\n    ')
    assert any((isinstance(meta, module_0.DocstringParam) and meta.default == '20' for meta in docstring.meta))


def test_example_d6vvql5v():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n    This is a test docstring.\n\n    Args:\n        arg1 (int): This is the first argument.\n        arg2 (str): This is the second argument.\n\n    Yields:\n        This is the yield value.\n\n    Raises:\n        ValueError: This is the error message.\n    ')
    assert any((isinstance(meta, module_0.DocstringRaises) for meta in docstring.meta))


def test_example_2wubwq27():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n    This is a test docstring.\n\n    Examples:\n        This is an example.\n\n    Returns:\n        This is the return value.\n\n    Raises:\n        TypeError: This is the error message.\n    ')
    assert docstring.short_description == 'This is a test docstring.'


