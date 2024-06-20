from common import Docstring
import pytest
from common import DEPRECATION_KEYWORDS
from common import RenderingStyle
import typing
from common import YIELDS_KEYWORDS
from common import ParseError
from common import PARAM_KEYWORDS
from common import DocstringRaises
from common import DocstringStyle
from common import DocstringMeta
import rest as module_0
import re
from common import DocstringParam
from common import RAISES_KEYWORDS
from common import RETURNS_KEYWORDS
from common import DocstringReturns
import inspect
from common import DocstringDeprecated
def test_example_ozbh2scw():
    docstring = module_0.parse('\n    This is a short description.\n\n    This is a long description.\n\n    :param foo: This is a parameter description.\n    :param bar: This is another parameter description.\n    :returns: This is a return description.\n    :raises ValueError: This is a raise description.\n    ')
    assert isinstance(docstring, module_0.Docstring)


def test_example_g01art9v():
    docstring = module_0.parse('\n    This is a short description.\n\n    :rtype: int\n    :returns: This is a return description.\n    ')
    assert isinstance(docstring.meta[0], module_0.DocstringReturns)


def test_example_oix30kq6():
    docstring = module_0.parse('\n    This is a short description.\n\n    :param foo: This is a parameter description.\n    :type foo: int\n    ')
    assert docstring.meta[0].type_name == 'int'


def test_example_jar8w9po():
    docstring = module_0.parse('\n    This is a short description.\n\n    :deprecated: This function is deprecated since v2.0.\n    ')
    assert isinstance(docstring.meta[0], module_0.DocstringDeprecated)


def test_example_jruo2un0():
    docstring = module_0.parse('\n    This is a short description.\n\n    :raises ValueError: This is a raise description.\n    ')
    assert isinstance(docstring.meta[0], module_0.DocstringRaises)


def test_example_bqzwczlm():
    docstring = module_0.compose(module_0.parse('\n    This is a short description.\n\n    :param foo: This is a parameter description.\n    :returns: This is a return description.\n    '), RenderingStyle.COMPACT)
    assert 'This is a short description.' in docstring


def test_example_ln9lqfyq():
    docstring = module_0.parse('\n    This is a short description.\n\n    :param foo: This is a parameter description.\n    :param bar baz: This is another parameter description.\n    ')
    assert len(docstring.meta) == 2


def test_example_yulur88m():
    docstring = module_0.parse('\n    This is a short description.\n\n    :yields: This is a yield description.\n    ')
    assert isinstance(docstring.meta[0], module_0.DocstringReturns)


