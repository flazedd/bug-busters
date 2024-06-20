from common import Docstring
import pytest
from enum import IntEnum
from collections import namedtuple
from common import RenderingStyle
import typing
from common import YIELDS_KEYWORDS
from common import ParseError
from common import PARAM_KEYWORDS
from collections import OrderedDict
from common import DocstringStyle
from common import DocstringRaises
from common import DocstringMeta
from common import EXAMPLES_KEYWORDS
import re
from common import RAISES_KEYWORDS
from common import DocstringParam
from common import DocstringExample
from common import RETURNS_KEYWORDS
from common import DocstringReturns
import google as module_0
import inspect
def test_example_xxrbcnik():
    docstring = module_0.parse('\n    This is a short description.\n\n    This is a long description.\n\n    Args:\n        param1: This is a parameter.\n        param2: This is another parameter.\n\n    Returns:\n        This is a return value.\n\n    Raises:\n        ValueError: This is an error.\n    ')
    assert isinstance(docstring, module_0.Docstring)


def test_example_p1w90l4w():
    docstring = module_0.parse('\n    This is a short description.\n\n    Attributes:\n        attr1: This is an attribute.\n        attr2: This is another attribute.\n\n    Yields:\n        This is a yield value.\n\n    Examples:\n        This is an example.\n    ')
    assert isinstance(docstring, module_0.Docstring)


def test_example_vzwuc1h0():
    docstring = module_0.parse('\n    This is a short description.\n\n    Args:\n        param1: This is a parameter.\n        param2 (int): This is another parameter with a default value of 5.\n\n    Returns:\n        This is a return value.\n\n    Raises:\n        ValueError: This is an error.\n    ')
    assert len(docstring.params) == 2


def test_example_2qvx0apk():
    docstring = module_0.parse('\n    This is a short description.\n\n    Attributes:\n        attr1: This is an attribute.\n        attr2: This is another attribute.\n\n    Yields:\n        This is a yield value.\n\n    Examples:\n        >>> 1 + 1\n        2\n    ')
    assert len(docstring.examples) == 1


def test_example_i3zsd7lw():
    docstring = module_0.parse('\n    This is a short description.\n\n    Args:\n        param1: This is a parameter.\n        param2: This is another parameter.\n\n    Returns:\n        This is a return value.\n\n    Raises:\n        ValueError: This is an error.\n    ')
    rendered_docstring = module_0.compose(docstring, rendering_style=module_0.RenderingStyle.EXPANDED)
    assert 'param1:' in rendered_docstring
    assert 'param2:' in rendered_docstring


def test_example_1nw7w462():
    docstring = module_0.parse('\n    This is a short description.\n\n    Attributes:\n        attr1: This is an attribute.\n        attr2: This is another attribute.\n\n    Yields:\n        This is a yield value.\n\n    Examples:\n        >>> 1 + 1\n        2\n        >>> 2 + 2\n        4\n    ')
    rendered_docstring = module_0.compose(docstring)
    assert 'Examples:' in rendered_docstring
    assert '>>> 1 + 1' in rendered_docstring
    assert '>>> 2 + 2' in rendered_docstring


def test_example_wn38102w():
    docstring = module_0.parse('\n    This is a short description.\n\n    Args:\n        param1: This is a parameter.\n        param2: This is another parameter.\n\n    Returns:\n        This is a return value.\n\n    Raises:\n        ValueError: This is an error.\n    ')
    assert docstring.short_description == 'This is a short description.'
    assert docstring.blank_after_short_description
    assert docstring.long_description is None


def test_example_u7gx8dsk():
    docstring = module_0.parse('\n    This is a short description.\n\n    Args:\n        param1: This is a parameter.\n        param2: This is another parameter.\n\n    Returns:\n        This is a return value.\n\n    Raises:\n        ValueError: This is an error.\n        TypeError: This is another error.\n    ')
    assert len(docstring.raises) == 2


