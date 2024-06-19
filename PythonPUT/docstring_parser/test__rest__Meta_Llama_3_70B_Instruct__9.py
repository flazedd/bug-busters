import rest as module_0
from common import DocstringReturns
import inspect
from common import DEPRECATION_KEYWORDS
from common import PARAM_KEYWORDS
from common import RenderingStyle
from common import YIELDS_KEYWORDS
from common import Docstring
from common import DocstringMeta
from common import DocstringRaises
from common import RETURNS_KEYWORDS
from common import ParseError
from common import DocstringDeprecated
from common import DocstringStyle
import typing
import re
from common import RAISES_KEYWORDS
from common import DocstringParam
import pytest
def test_example_xnrt54dt():
    docstring = module_0.parse('\n    Short description.\n\n    Long description.\n\n    :param arg1: This is arg1.\n    :param arg2: This is arg2.\n    :returns: This is the return value.\n    ')
    rendered_docstring = module_0.compose(docstring)
    assert rendered_docstring == '\nShort description.\n\nLong description.\n\n:param arg1: This is arg1.\n:param arg2: This is arg2.\n:returns: This is the return value.\n'.strip()





def test_example_b2u0d2bo():
    docstring = module_0.parse('\n    Short description.\n\n    :param arg1: This is arg1. (default is 5)\n    :returns: This is the return value.\n    ')
    rendered_docstring = module_0.compose(docstring)
    assert rendered_docstring == '\nShort description.\n\n:param arg1: This is arg1. (default is 5)\n:returns: This is the return value.\n'.strip()





def test_example_v523zfhk():
    docstring = module_0.parse('\n    Short description.\n\n    :param arg1: This is arg1.\n    :param arg2: This is arg2.\n    :deprecated: This function is deprecated.\n    ')
    rendered_docstring = module_0.compose(docstring)
    assert rendered_docstring == '\nShort description.\n\n:param arg1: This is arg1.\n:param arg2: This is arg2.\n:deprecated: This function is deprecated.\n'.strip()





def test_example_vsqqzeb2():
    docstring = module_0.parse('\n    Short description.\n\n    :param arg1: This is arg1. (default is 5)\n    :param arg2: This is arg2.\n    :returns: This is the return value.\n    ')
    rendered_docstring = module_0.compose(docstring, rendering_style=module_0.RenderingStyle.COMPACT)
    assert rendered_docstring == '\nShort description.\n\n:param arg1: This is arg1. (default is 5)\n:param arg2: This is arg2.\n:returns: This is the return value.\n'.strip()





def test_example_3avlf5e9():
    docstring = module_0.parse('\n    Short description.\n\n    :param arg1: This is arg1.\n    :param arg2: This is arg2.\n    :deprecated: This function is deprecated since version 1.2.\n    ')
    rendered_docstring = module_0.compose(docstring)
    assert rendered_docstring == '\nShort description.\n\n:param arg1: This is arg1.\n:param arg2: This is arg2.\n:deprecated: This function is deprecated since version 1.2.\n'.strip()





def test_example_0zvqst8g():
    docstring = module_0.parse('\n    This is a test function.\n\n    :param foo: This is a parameter\n    :type foo: str\n    :returns: This is a return value\n    :rtype: int\n    ')
    assert isinstance(docstring, module_0.Docstring)


def test_example_539hqr84():
    docstring = module_0.parse('\n    This is a test function.\n\n    :raises ValueError: This is an exception\n    :raises TypeError: This is another exception\n    ')
    assert len(docstring.meta) == 2
    assert all((isinstance(m, module_0.DocstringRaises) for m in docstring.meta))


def test_example_gty31s82():
    docstring = module_0.parse('\n    This is a test function.\n\n    :param foo: This is a parameter\n    :param bar: This is another parameter\n    ')
    assert len(docstring.meta) == 2
    assert all((isinstance(m, module_0.DocstringParam) for m in docstring.meta))


