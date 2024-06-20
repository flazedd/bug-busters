import epydoc as module_0
from common import DocstringStyle
import inspect
from common import DocstringRaises
import typing
from common import DocstringMeta
from common import Docstring
import re
import pytest
from common import DocstringParam
from common import DocstringReturns
from common import RenderingStyle
from common import ParseError
def test_example_nuoatfnt():
    text = 'This is a test docstring.\n\n    It has multiple lines.\n\n    @param foo: This is a parameter\n    @type foo: int\n    @return: This is a return value\n    @rtype: str\n    @raise ValueError: This is an exception\n    '
    docstring = module_0.parse(text)
    assert len(docstring.meta) == 3





def test_example_1grmtj01():
    text = 'This is a test docstring.\n\n    It has multiple lines.\n\n    @param bar: This is another parameter\n    @type bar: str\n    @return: This is another return value\n    @rtype: int\n    @raise TypeError: This is another exception\n    '
    docstring = module_0.parse(text)
    assert len(docstring.meta) == 3





def test_example_fuwzyeb4():
    text = 'This is a test docstring.\n\n    It has multiple lines.\n\n    @keyword baz: This is a keyword\n    @return: This is a return value\n    @rtype: float\n    '
    docstring = module_0.parse(text)
    assert len(docstring.meta) == 2





def test_example_9h1oiq0p():
    text = 'This is a test docstring.\n\n    It has multiple lines.\n\n    @param foo: This is a parameter\n    @type foo: int?\n    @return: This is a return value\n    @rtype: str\n    '
    docstring = module_0.parse(text)
    assert docstring.meta[0].is_optional





def test_example_zy7vygjy():
    text = 'This is a test docstring.\n\n    It has multiple lines.\n\n    @param foo: This is a parameter\n    @type foo: int\n    @return: This is a return value\n    @rtype: str\n    '
    docstring = module_0.parse(text)
    composed_text = module_0.compose(docstring)
    assert 'This is a test docstring.' in composed_text
    assert '@param foo: This is a parameter' in composed_text
    assert '@return: This is a return value' in composed_text





def test_example_ov6uhv15():
    text = 'This is a test docstring.\n\n    It has multiple lines.\n\n    @param foo: This is a parameter\n    @return: This is the return value\n    @raise ValueError: This is an error\n    '
    docstring = module_0.parse(text)
    assert isinstance(docstring, module_0.Docstring)


def test_example_y4c984rf():
    text = 'This is a test docstring.\n\n    It has multiple lines.\n\n    @param foo: This is a parameter\n    @param bar: This is another parameter\n    @return: This is the return value\n    '
    docstring = module_0.parse(text)
    composed = module_0.compose(docstring, rendering_style=module_0.RenderingStyle.EXPANDED)
    assert 'This is a test docstring.' in composed
    assert 'This is a parameter' in composed
    assert 'This is another parameter' in composed
    assert 'This is the return value' in composed


def test_example_7e97ybaf():
    text = 'This is a test docstring.\n\n    It has multiple lines.\n\n    @raise ValueError: This is an error\n    @raise TypeError: This is another error\n    '
    docstring = module_0.parse(text)
    composed = module_0.compose(docstring)
    assert 'This is an error' in composed
    assert 'This is another error' in composed


