import re
import typing
import rest as module_0
from common import DocstringMeta
from common import Docstring
from common import DocstringParam
from common import DocstringDeprecated
from common import RenderingStyle
from common import RAISES_KEYWORDS
from common import ParseError
from common import PARAM_KEYWORDS
from common import RETURNS_KEYWORDS
from common import DEPRECATION_KEYWORDS
from common import DocstringReturns
import pytest
from common import DocstringStyle
from common import YIELDS_KEYWORDS
import inspect
from common import DocstringRaises
def test_example_8wwbzk7k():
    docstring = module_0.parse('\n    This is a short description.\n\n    This is a long description.\n\n    :param int x: This is a parameter.\n    :param y: This is another parameter.\n    :returns: This is the return value.\n    :raises ValueError: This is an exception.\n    ')
    assert isinstance(docstring, module_0.Docstring)
    assert docstring.short_description == 'This is a short description.'
    assert docstring.long_description == 'This is a long description.'
    assert len(docstring.meta) == 4
    assert isinstance(docstring.meta[0], module_0.DocstringParam)
    assert isinstance(docstring.meta[1], module_0.DocstringParam)
    assert isinstance(docstring.meta[2], module_0.DocstringReturns)
    assert isinstance(docstring.meta[3], module_0.DocstringRaises)








def test_example_rqsejx5s():
    docstring = module_0.parse('This is a test docstring.\n\n:param foo: This is a parameter.\n:returns: This is a return value.')
    assert isinstance(docstring, module_0.Docstring)


def test_example_2ujnv5vy():
    docstring = module_0.parse(':param foo: This is a parameter.\n:raises ValueError: This is an error.')
    assert len(docstring.meta) == 2


def test_example_i6g2wy5d():
    docstring = module_0.parse('This is a test docstring.\n\n:yields: This is a yield value.')
    assert any((isinstance(meta, module_0.DocstringReturns) and meta.is_generator for meta in docstring.meta))


def test_example_65n7gjj8():
    docstring = module_0.parse(':param foo: This is a parameter.\n:type foo: int')
    assert docstring.meta[0].type_name == 'int'


def test_example_6dtzejk8():
    docstring = module_0.parse(':deprecated: This is a deprecated function.')
    assert any((isinstance(meta, module_0.DocstringDeprecated) for meta in docstring.meta))


def test_example_2369qn4t():
    docstring = module_0.parse('This is a test docstring.\n\n:param foo: This is a parameter.\n:rtype: int')
    assert any((isinstance(meta, module_0.DocstringReturns) and meta.type_name == 'int' for meta in docstring.meta))


def test_example_r2n3j682():
    docstring = module_0.parse(':param foo: This is a parameter.\n:param bar: This is another parameter.')
    assert len([meta for meta in docstring.meta if isinstance(meta, module_0.DocstringParam)]) == 2


