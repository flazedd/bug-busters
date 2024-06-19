from common import RenderingStyle
from common import Docstring
from common import DocstringStyle
import inspect
from common import DocstringDeprecated
from common import ParseError
from common import DocstringRaises
from common import DocstringReturns
import re
from common import RAISES_KEYWORDS
from common import DocstringMeta
import rest as module_0
from common import YIELDS_KEYWORDS
import pytest
import typing
from common import PARAM_KEYWORDS
from common import DocstringParam
from common import RETURNS_KEYWORDS
from common import DEPRECATION_KEYWORDS
def test_example_5emvlt4k():
    docstring = module_0.parse('\n    Short description.\n\n    Long description.\n\n    :param foo: Foo parameter\n    :param bar: Bar parameter\n    :returns: Return value\n    :raises ValueError: Raised when something goes wrong\n    ')
    assert isinstance(docstring, module_0.Docstring)
    assert docstring.short_description == 'Short description.'
    assert docstring.long_description == 'Long description.'
    assert len(docstring.meta) == 4
    assert isinstance(docstring.meta[0], module_0.DocstringParam)
    assert isinstance(docstring.meta[1], module_0.DocstringParam)
    assert isinstance(docstring.meta[2], module_0.DocstringReturns)
    assert isinstance(docstring.meta[3], module_0.DocstringRaises)





def test_example_jsesdqds():
    docstring = module_0.parse('\n    Short description.\n\n    :param foo: Foo parameter with default value, defaults to 10.\n    :rtype: int\n    ')
    assert isinstance(docstring, module_0.Docstring)
    assert docstring.short_description == 'Short description.'
    assert docstring.long_description is None
    assert len(docstring.meta) == 2
    assert isinstance(docstring.meta[0], module_0.DocstringParam)
    assert isinstance(docstring.meta[1], module_0.DocstringReturns)
    assert docstring.meta[0].default == '10'
    assert docstring.meta[1].type_name == 'int'





def test_example_ckg39s5j():
    docstring = module_0.parse('\n    Short description.\n\n    :param foo: Foo parameter\n    :param bar: Bar parameter with default value, defaults to 10.\n    ')
    assert isinstance(docstring, module_0.Docstring)
    assert docstring.short_description == 'Short description.'
    assert docstring.long_description is None
    assert len(docstring.meta) == 2
    assert isinstance(docstring.meta[0], module_0.DocstringParam)
    assert isinstance(docstring.meta[1], module_0.DocstringParam)
    assert docstring.meta[0].default is None
    assert docstring.meta[1].default == '10'





def test_example_zulh03g1():
    docstring = module_0.parse('\n    Short description.\n\n    :param foo: Foo parameter\n    ')
    rendered_docstring = module_0.compose(docstring, rendering_style=module_0.RenderingStyle.CLEAN)
    assert rendered_docstring.startswith('Short description.')
    assert ' Foo parameter' in rendered_docstring





def test_example_zr5tvgr8():
    docstring = module_0.parse('\n    Short description.\n\n    :param foo: Foo parameter\n    :param bar: Bar parameter\n    :yields: Yield value\n    :yields: Another yield value\n    ')
    rendered_docstring = module_0.compose(docstring)
    assert rendered_docstring.startswith('Short description.')
    assert ':param foo: Foo parameter' in rendered_docstring
    assert ':param bar: Bar parameter' in rendered_docstring
    assert ':yields: Yield value' in rendered_docstring
    assert ':yields: Another yield value' in rendered_docstring





def test_example_hxfszvc5():

    def test_docstring():
        doc = '\n        This is a test docstring.\n\n        It has a short description and a longer description.\n\n        :param arg1: This is the first argument.\n        :param arg2: This is the second argument.\n        :returns: This is the return value.\n        '
        parsed_doc = module_0.parse(doc)
        rendered_doc = module_0.compose(parsed_doc)
        assert rendered_doc.startswith('This is a test docstring.')
        assert 'This is the first argument.' in rendered_doc
        assert 'This is the second argument.' in rendered_doc
        assert 'This is the return value.' in rendered_doc
    test_docstring()


def test_example_g7mluy7q():

    def test_raises_docstring():
        doc = '\n        This is a function that raises an exception.\n\n        :raises ValueError: This is the error message.\n        '
        parsed_doc = module_0.parse(doc)
        rendered_doc = module_0.compose(parsed_doc)
        assert 'This is a function that raises an exception.' in rendered_doc
        assert 'ValueError' in rendered_doc
        assert 'This is the error message.' in rendered_doc
    test_raises_docstring()


def test_example_j7ackxhn():

    def test_yield_docstring():
        doc = '\n        This is a generator function.\n\n        :yields str: This is the yield value.\n        '
        parsed_doc = module_0.parse(doc)
        rendered_doc = module_0.compose(parsed_doc)
        assert 'This is a generator function.' in rendered_doc
        assert 'yields' in rendered_doc
        assert 'str' in rendered_doc
        assert 'This is the yield value.' in rendered_doc
    test_yield_docstring()


