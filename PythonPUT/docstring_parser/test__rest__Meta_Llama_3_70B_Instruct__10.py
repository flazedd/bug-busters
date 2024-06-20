from common import DEPRECATION_KEYWORDS
import re
import typing
from common import RETURNS_KEYWORDS
from common import DocstringRaises
from common import PARAM_KEYWORDS
from common import DocstringReturns
from common import DocstringParam
import rest as module_0
from common import YIELDS_KEYWORDS
from common import ParseError
from common import DocstringStyle
from common import Docstring
from common import DocstringMeta
from common import DocstringDeprecated
import pytest
from common import RAISES_KEYWORDS
from common import RenderingStyle
import inspect
def test_example_wu7iv1bf():
    docstring_text = '\n    This is a short description.\n\n    This is a long description.\n\n    :param foo: This is a parameter description.\n    :param bar: This is another parameter description.\n    :returns: This is a return description.\n    :raises ValueError: This is a raise description.\n    '
    parsed_docstring = module_0.parse(docstring_text)
    rendered_docstring = module_0.compose(parsed_docstring)
    assert rendered_docstring.startswith('This is a short description.')





def test_example_jhgdmvrj():
    docstring = module_0.parse('\n    This is a short description.\n\n    This is a long description.\n\n    :param arg1: This is a parameter description.\n    :param arg2: This is another parameter description.\n    :returns: This is a return description.\n    :raises ValueError: This is a raise description.\n    ')
    rendered_docstring = module_0.compose(docstring)
    assert rendered_docstring == '\nThis is a short description.\n\nThis is a long description.\n\n:param arg1: This is a parameter description.\n:param arg2: This is another parameter description.\n:returns: This is a return description.\n:raises ValueError : This is a raise description.\n'.strip()


def test_example_ddb2dpbf():
    docstring = module_0.parse('\n    This is a short description.\n\n    This is a long description.\n\n    :param arg1: This is a parameter description.\n    :param arg1: This is another parameter description for arg1.\n    :returns: This is a return description.\n    :rtype: int\n    ')
    rendered_docstring = module_0.compose(docstring)
    assert rendered_docstring == '\nThis is a short description.\n\nThis is a long description.\n\n:param arg1: This is a parameter description.\n:param arg1: This is another parameter description for arg1.\n:returns int: This is a return description.\n'.strip()


def test_example_fkr0tuhz():
    docstring = module_0.parse('\n    This is a short description.\n\n    This is a long description.\n\n    :param arg1: This is a parameter description. Defaults to 5.\n    :returns: This is a return description.\n    ')
    rendered_docstring = module_0.compose(docstring)
    assert rendered_docstring == '\nThis is a short description.\n\nThis is a long description.\n\n:param arg1: This is a parameter description. Defaults to 5.\n:returns: This is a return description.\n'.strip()


def test_example_33lhjyb8():
    docstring = module_0.parse('\n    This is a short description.\n\n    This is a long description.\n\n    :deprecated: This function is deprecated since version 2.0.\n    ')
    rendered_docstring = module_0.compose(docstring)
    assert rendered_docstring == '\nThis is a short description.\n\nThis is a long description.\n\n:deprecated: This function is deprecated since version 2.0.\n'.strip()


def test_example_px7ctt8e():
    docstring = module_0.parse('\n    This is a short description.\n\n    This is a long description.\n\n    :param arg1: This is a parameter description.\n    :param arg2?: This is another parameter description.\n    :returns: This is a return description.\n    ')
    rendered_docstring = module_0.compose(docstring)
    assert rendered_docstring == '\nThis is a short description.\n\nThis is a long description.\n\n:param arg1: This is a parameter description.\n:param arg2?: This is another parameter description.\n:returns: This is a return description.\n'.strip()


def test_example_hopwtb3o():
    docstring = module_0.parse('\n    This is a short description.\n\n    This is a long description.\n\n    :raises ValueError: This is a raise description.\n    :raises TypeError: This is another raise description.\n    ')
    rendered_docstring = module_0.compose(docstring)
    assert rendered_docstring == '\nThis is a short description.\n\nThis is a long description.\n\n:raises ValueError : This is a raise description.\n:raises TypeError : This is another raise description.\n'.strip()


def test_example_6jsf13ne():
    docstring = module_0.parse('\n    This is a short description.\n\n    This is a long description.\n\n    :param arg1: This is a parameter description.\n    :type arg1: int\n    :returns: This is a return description.\n    ')
    rendered_docstring = module_0.compose(docstring)
    assert rendered_docstring == '\nThis is a short description.\n\nThis is a long description.\n\n:param int arg1: This is a parameter description.\n:returns: This is a return description.\n'.strip()


