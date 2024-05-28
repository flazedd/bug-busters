import re
from common import PARAM_KEYWORDS
from common import DocstringMeta
from common import DocstringStyle
from enum import IntEnum
from common import DocstringParam
from common import RenderingStyle
from common import DocstringRaises
import inspect
from common import EXAMPLES_KEYWORDS
import google as module_0
from common import DocstringExample
from common import YIELDS_KEYWORDS
from collections import namedtuple
import typing
from common import ParseError
from common import RETURNS_KEYWORDS
from collections import OrderedDict
from common import Docstring
from common import DocstringReturns
from common import RAISES_KEYWORDS
import pytest
def test_example_x8fm2zku():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n    This is a short description.\n\n    This is a long description.\n\n    Args:\n        param1: This is a parameter.\n        param2: This is another parameter.\n\n    Returns:\n        This is a return value.\n\n    Raises:\n        ValueError: This is an error.\n    ')
    assert isinstance(docstring, module_0.Docstring)


def test_example_w4gizxtm():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n    This is a short description.\n\n    Attributes:\n        attr1: This is an attribute.\n        attr2: This is another attribute.\n\n    Examples:\n        >>> print("Hello, World!")\n        Hello, World!\n    ')
    assert len(docstring.meta) == 3


def test_example_mtfaqi82():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n    This is a short description.\n\n    Yields:\n        This is a yield value.\n\n    Raises:\n        TypeError: This is an error.\n    ')
    assert any((isinstance(meta, module_0.DocstringReturns) for meta in docstring.meta))


def test_example_ryrg1csz():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n    This is a short description.\n\n    Parameters:\n        param1 (int): This is a parameter.\n        param2 (str): This is another parameter.\n\n    Returns:\n        str: This is a return value.\n    ')
    assert any((isinstance(meta, module_0.DocstringParam) for meta in docstring.meta))


def test_example_q808pqeo():
    docstring = module_0.Docstring(style=module_0.DocstringStyle.GOOGLE)
    rendered_docstring = module_0.compose(docstring, module_0.RenderingStyle.COMPACT)
    assert rendered_docstring == ''


def test_example_xj7ot9qy():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n    This is a short description.\n\n    Args:\n        * param1: This is a parameter.\n        * param2: This is another parameter.\n\n    Returns:\n        This is a return value.\n\n    Raises:\n        ValueError: This is an error.\n    ')
    assert any((isinstance(meta, module_0.DocstringParam) and meta.arg_name.startswith('*') for meta in docstring.meta))


def test_example_gle0dndu():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n    This is a short description.\n\n    Example:\n        >>> print("Hello, World!")\n        Hello, World!\n    ')
    assert any((isinstance(meta, module_0.DocstringExample) for meta in docstring.meta))


def test_example_hmdc2kf7():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n    This is a short description.\n\n    Parameters:\n        param1: This is a parameter. Defaults to 5.\n        param2: This is another parameter. Defaults to "hello".\n\n    Returns:\n        This is a return value.\n    ')
    assert any((isinstance(meta, module_0.DocstringParam) and meta.default is not None for meta in docstring.meta))


