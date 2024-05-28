import pytest
from common import PARAM_KEYWORDS
import google as module_0
from common import DocstringRaises
from common import YIELDS_KEYWORDS
from collections import OrderedDict
import re
import typing
from collections import namedtuple
import inspect
from common import DocstringMeta
from common import RenderingStyle
from common import EXAMPLES_KEYWORDS
from common import ParseError
from common import DocstringParam
from common import DocstringStyle
from common import DocstringReturns
from common import RETURNS_KEYWORDS
from enum import IntEnum
from common import RAISES_KEYWORDS
from common import Docstring
from common import DocstringExample
def test_example_0h8crbwn():
    docstring = module_0.parse('This is a short description.\n\nThis is a long description.\n\nArgs:\n    arg1: This is arg1.\n    arg2: This is arg2.\nReturns:\n    This is the return value.')
    assert docstring.short_description == 'This is a short description.'





def test_example_odlysyb1():
    docstring = module_0.parse('This is a short description.\n\nRaises:\n    ValueError: This is an error.\n    TypeError: This is another error.')
    assert len(docstring.raises) == 2





def test_example_o9eewyqy():
    docstring = module_0.parse('This is a short description.\n\nExample:\n    This is an example.')
    assert isinstance(docstring.meta[0], module_0.DocstringExample)





def test_example_lwr0ntuz():
    docstring = module_0.parse('This is a short description.\n\nYields:\n    This is the yield value.')
    assert docstring.many_returns[0].is_generator





def test_example_rbeuzcjm():
    rendered_docstring = module_0.compose(module_0.parse('This is a short description.\n\nArgs:\n    arg1: This is arg1.\n    arg2: This is arg2.\nReturns:\n    This is the return value.'))
    assert 'Args:' in rendered_docstring





def test_example_dyvgkaeo():
    docstring = module_0.parse('This is a short description.\n\nAttributes:\n    attr1: This is attr1.\n    attr2: This is attr2.')
    assert len([p for p in docstring.params or [] if p.args[0] == 'attribute']) == 2





def test_example_ac32hwvj():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n        This is a short description.\n\n        This is a long description that spans multiple lines.\n\n        Args:\n            param1 (int): This is a parameter.\n            param2 (str): This is another parameter.\n\n        Returns:\n            int: This is the return value.\n\n        Raises:\n            ValueError: This is an exception.\n    ')
    assert len(docstring.meta) == 4


def test_example_nk7ap72c():
    parser = module_0.GoogleParser()
    docstring = parser.parse('\n        This is a short description.\n\n        Attributes:\n            attr1 (int): This is an attribute.\n            attr2 (str): This is another attribute.\n\n        Examples:\n            >>> 1 + 1\n            2\n    ')
    assert len(docstring.meta) == 3


