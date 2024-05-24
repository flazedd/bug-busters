from common import ParseError
import typing
from common import DocstringMeta
import re
from common import DocstringStyle
from common import DocstringRaises
import pytest
from common import YIELDS_KEYWORDS
from common import DocstringReturns
from common import DocstringDeprecated
from common import RETURNS_KEYWORDS
import inspect
from common import PARAM_KEYWORDS
from common import Docstring
from common import DEPRECATION_KEYWORDS
import rest as module_0
from common import DocstringParam
from common import RenderingStyle
from common import RAISES_KEYWORDS
def test_example_hnllykfp():
    docstring = module_0.parse('\n    This is a test docstring.\n\n    :param foo: This is a parameter\n    :param bar: This is another parameter\n    :returns: This is the return value\n    ')
    assert docstring.short_description == 'This is a test docstring.'


def test_example_19hqwxhp():
    docstring = module_0.parse('\n    This is a test docstring.\n\n    :param baz: This is an optional parameter, defaults to 42\n    :rtype: int\n    ')
    assert docstring.meta[0].default == '42'


def test_example_6isau18s():
    docstring = module_0.parse('\n    This is a test docstring.\n\n    :raises ValueError: This is an error\n    :raises TypeError: This is another error\n    ')
    assert len(docstring.meta) == 2


def test_example_jhgo2sao():
    docstring = module_0.parse('\n    This is a test docstring.\n\n    :param spam: This is a parameter\n    :type spam: int\n    :returns: This is the return value\n    ')
    assert docstring.meta[0].type_name == 'int'


def test_example_f5q2ltrq():
    docstring = module_0.parse('\n    This is a test docstring.\n\n    :deprecated: This function is deprecated since v2.0\n    ')
    assert isinstance(docstring.meta[0], module_0.DocstringDeprecated)


def test_example_1bcjh84v():
    docstring = module_0.parse('\n    This is a test docstring.\n\n    :yields: This is the yield value\n    ')
    assert docstring.meta[0].is_generator


def test_example_0r6lyaua():
    rendered_docstring = module_0.compose(module_0.parse('\n    This is a test docstring.\n\n    :param foo: This is a parameter\n    :returns: This is the return value\n    '))
    assert 'This is a test docstring.' in rendered_docstring


def test_example_q412vigi():
    docstring = module_0.parse('\n    This is a test docstring.\n\n    :param foo: This is a parameter\n    :param bar: This is another parameter with type, defaults to 42\n    ')
    assert docstring.meta[1].default == '42'


