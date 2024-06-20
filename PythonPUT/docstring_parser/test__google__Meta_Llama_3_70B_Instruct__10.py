from common import DocstringStyle
from common import EXAMPLES_KEYWORDS
from common import RAISES_KEYWORDS
import typing
from common import Docstring
import re
import pytest
from enum import IntEnum
from common import DocstringReturns
from common import RenderingStyle
from common import YIELDS_KEYWORDS
from common import PARAM_KEYWORDS
from common import DocstringExample
from collections import OrderedDict
from collections import namedtuple
from common import RETURNS_KEYWORDS
import inspect
from common import DocstringRaises
import google as module_0
from common import DocstringMeta
from common import DocstringParam
from common import ParseError
def test_example_rh0jx75a():
    docstring = module_0.parse('\n    This is a test docstring.\n\n    Args:\n        param1 (int): This is a parameter.\n        param2 (str): This is another parameter.\n\n    Returns:\n        int: This is a return value.\n\n    Raises:\n        ValueError: This is an exception.\n    ')
    assert isinstance(docstring, module_0.Docstring)


def test_example_tiuban5q():
    docstring = module_0.parse('\n    This is a test docstring.\n\n    Examples:\n        >>> 1 + 1\n        2\n    ')
    assert len(docstring.meta) == 1


def test_example_jfbaf0nz():
    docstring = module_0.parse('\n    This is a test docstring.\n\n    Attributes:\n        attr1 (str): This is an attribute.\n        attr2 (int): This is another attribute.\n    ')
    assert all((isinstance(meta, module_0.DocstringParam) for meta in docstring.meta))


def test_example_gwl0lnh1():
    docstring = module_0.parse('\n    This is a test docstring.\n\n    Yields:\n        int: This is a yield value.\n    ')
    assert any((isinstance(meta, module_0.DocstringReturns) and meta.is_generator for meta in docstring.meta))


def test_example_qq92gwnh():
    docstring = module_0.parse('\n    This is a test docstring.\n\n    Parameters:\n        param1 (int): This is a parameter.\n        param2 (str): This is another parameter.\n    ')
    assert all((isinstance(meta, module_0.DocstringParam) for meta in docstring.meta))


def test_example_08xqny3p():
    docstring = module_0.parse('\n    This is a test docstring.\n\n    Raises:\n        ValueError: This is an exception.\n        TypeError: This is another exception.\n    ')
    assert len([meta for meta in docstring.meta if isinstance(meta, module_0.DocstringRaises)]) == 2


def test_example_lfeg64wn():
    docstring = module_0.parse('\n    This is a test docstring.\n\n    Args:\n        param1 (int): This is a parameter with default value. Defaults to 10.\n    ')
    assert docstring.meta[0].default == '10'


def test_example_ndv3f1lg():
    docstring = module_0.parse('\n    This is a test docstring.\n\n    Parameters:\n        param1 (int, optional): This is a parameter. Defaults to 10.\n    ')
    assert docstring.meta[0].is_optional


