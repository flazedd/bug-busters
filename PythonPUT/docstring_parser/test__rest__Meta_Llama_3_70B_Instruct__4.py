from common import RETURNS_KEYWORDS
from common import YIELDS_KEYWORDS
import typing
import inspect
from common import DocstringStyle
from common import DocstringRaises
from common import DocstringReturns
from common import DEPRECATION_KEYWORDS
from common import RAISES_KEYWORDS
from common import DocstringParam
from common import DocstringMeta
import re
import pytest
from common import Docstring
from common import RenderingStyle
from common import DocstringDeprecated
from common import PARAM_KEYWORDS
from common import ParseError
import rest as module_0
def test_example_e0cqo4gf():
    docstring = module_0.parse('\n    This is a test docstring.\n\n    :param foo: This is a parameter.\n    :param bar: This is another parameter.\n    :returns: This is the return value.\n    ')
    assert isinstance(docstring, Docstring)

















def test_example_v69xbo1w():
    docstring = module_0.parse('\n    This is a test docstring.\n\n    :param foo: This is a param\n    :param bar: This is another param\n    :returns: This is a return value\n    ')
    assert isinstance(docstring, module_0.Docstring)














def test_example_qb0f7jeu():
    docstring = module_0.parse('\n    This is a test docstring.\n\n    :raises ValueError: This is a raised error\n    :rtype: This is a return type\n    ')
    assert len(docstring.meta) == 2














def test_example_dqcqabp8():
    docstring = module_0.parse('\n    This is a test docstring.\n\n    :param baz: This is an optional param, defaults to 42.\n    ')
    assert docstring.meta[0].default == '42'














def test_example_brenbbz5():
    docstring = module_0.parse('\n    This is a test docstring.\n\n    :deprecated: This is a deprecated function, use something else instead.\n    ')
    assert isinstance(docstring.meta[0], module_0.DocstringDeprecated)











def test_example_q200riay():
    docstring = module_0.parse('\n    Short description.\n\n    Long description.\n\n    :param arg1: This is arg1\n    :param arg2: This is arg2\n    :returns: This is the return value\n    ')
    assert isinstance(docstring, module_0.Docstring)








def test_example_kmeb9slc():
    docstring = module_0.parse('\n    Short description.\n\n    :raises ValueError: This is a value error\n    :raises TypeError: This is a type error\n    ')
    assert len(docstring.meta) == 2
    assert all((isinstance(meta, module_0.DocstringRaises) for meta in docstring.meta))








def test_example_ks7pwav3():
    docstring = module_0.parse('\n    Short description.\n\n    Long description.\n\n    :param foo: This is a parameter.\n    :param bar: This is another parameter.\n    :returns: This is the return value.\n    :raises ValueError: This is an error.\n    ')
    rendered_docstring = module_0.compose(docstring, rendering_style=RenderingStyle.COMPACT)
    assert 'Short description.' in rendered_docstring


