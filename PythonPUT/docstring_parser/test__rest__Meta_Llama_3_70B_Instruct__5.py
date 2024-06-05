from common import PARAM_KEYWORDS
from common import YIELDS_KEYWORDS
from common import RAISES_KEYWORDS
import inspect
from common import DocstringMeta
from common import RETURNS_KEYWORDS
from common import DocstringRaises
from common import RenderingStyle
from common import Docstring
import re
from common import DocstringStyle
from common import DocstringParam
from common import DocstringReturns
import rest as module_0
import pytest
import typing
from common import DocstringDeprecated
from common import ParseError
from common import DEPRECATION_KEYWORDS
def test_example_q1qqt8n9():
    docstring = module_0.parse('\n    This is a short description.\n\n    This is a long description.\n\n    :param foo: This is a parameter description.\n    :param bar: This is another parameter description.\n    :returns: This is a return description.\n    :raises ValueError: This is a raise description.\n    ')
    assert isinstance(docstring, module_0.Docstring)


def test_example_gx0yaign():
    docstring = module_0.parse('\n    This is a short description.\n\n    :rtype: int\n    :returns: This is a return description.\n    ')
    assert isinstance(docstring.meta[0], module_0.DocstringReturns)


def test_example_wmj9v9wj():
    docstring = module_0.parse('\n    This is a short description.\n\n    :param foo: This is a parameter description.\n    ')
    assert docstring.meta[0].arg_name == 'foo'


def test_example_ea68suzl():
    docstring = module_0.parse('\n    This is a short description.\n\n    :deprecated: This is a deprecation description.\n    ')
    assert isinstance(docstring.meta[0], module_0.DocstringDeprecated)


def test_example_600swr31():
    docstring = module_0.parse('\n    This is a short description.\n\n    :param foo: This is a parameter description.\n    :type foo: int\n    ')
    assert docstring.meta[0].type_name == 'int'


def test_example_rhfrnvn4():
    docstring = module_0.compose(module_0.parse('\n    This is a short description.\n\n    :param foo: This is a parameter description.\n    :returns: This is a return description.\n    '), rendering_style=module_0.RenderingStyle.COMPACT)
    assert 'This is a short description.' in docstring


def test_example_vxhq1agn():
    docstring = module_0.parse('\n    This is a short description.\n\n    :raises ValueError: This is a raise description.\n    ')
    assert isinstance(docstring.meta[0], module_0.DocstringRaises)


def test_example_vajep0r7():
    docstring = module_0.parse('\n    This is a short description.\n\n    :yields: This is a yield description.\n    ')
    assert isinstance(docstring.meta[0], module_0.DocstringReturns)


