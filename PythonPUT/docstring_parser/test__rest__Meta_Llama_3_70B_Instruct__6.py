from common import Docstring
import rest as module_0
from common import PARAM_KEYWORDS
import re
from common import RAISES_KEYWORDS
from common import DocstringReturns
from common import DocstringRaises
from common import DocstringDeprecated
from common import DocstringStyle
from common import RenderingStyle
import typing
from common import DEPRECATION_KEYWORDS
from common import RETURNS_KEYWORDS
from common import ParseError
from common import DocstringMeta
import pytest
from common import DocstringParam
from common import YIELDS_KEYWORDS
import inspect
def test_example_pxb6exu4():
    assert module_0.parse('This is a test docstring.') != None


def test_example_nmsy3xwc():
    assert module_0.compose(module_0.parse('This is a test docstring.'), RenderingStyle.COMPACT) != ''


def test_example_nw5nb2s4():
    assert module_0.parse(':param foo: This is a test parameter.\n:returns: This is a test return.').meta[0].arg_name == 'foo'


def test_example_q98fon1z():
    assert module_0.parse(':raises ValueError: This is a test error.').meta[0].type_name == 'ValueError'


def test_example_t64x4iuy():
    assert module_0.parse(':param foo: This is a test parameter.\n:rtype: int').meta[1].type_name == 'int'


def test_example_mt5yib49():
    assert module_0.parse(':param foo: This is a test parameter.\n:returns: This is a test return.').meta[1].type_name is None


def test_example_pf9p6zxf():
    assert module_0.parse(':param foo: This is a test parameter.\n:param bar: This is another test parameter.').meta[1].arg_name == 'bar'


def test_example_tqo9vcnk():
    assert module_0.parse(':param foo: This is a test parameter.\n:deprecated: This is a deprecated function.').meta[1].args[0] == 'deprecated'


