import itertools
from common import DocstringExample
from common import DocstringParam
import inspect
from common import DocstringRaises
from common import DocstringDeprecated
from common import DocstringStyle
from common import DocstringReturns
import re
import pytest
import typing
from textwrap import dedent
from common import Docstring
from common import DocstringMeta
import numpydoc as module_0
from common import RenderingStyle
def test_example_ozk00g74():
    assert 1 == 1








def test_example_mmu8754c():
    docstring = module_0.parse('\n    This is a test docstring.\n\n    Parameters:\n    arg1 (int): The first argument.\n    arg2 (str): The second argument.\n\n    Returns:\n    int: The sum of arg1 and the length of arg2.\n\n    Raises:\n    ValueError: If arg1 is not a positive integer.\n    ')
    assert docstring.short_description == 'This is a test docstring.'








def test_example_u9tb4p7k():
    docstring = module_0.parse('\n    This is a test docstring.\n\n    Parameters:\n    arg1 (int): The first argument.\n    arg2 (str): The second argument.\n\n    Returns:\n    int: The sum of arg1 and the length of arg2.\n\n    Raises:\n    ValueError: If arg1 is not a positive integer.\n    ')
    assert docstring.style == DocstringStyle.NUMPYDOC








def test_example_ja5uxk0m():
    docstring = module_0.parse('\n    This is a test docstring.\n\n    Parameters:\n    arg1 (int): The first argument.\n    arg2 (str): The second argument.\n\n    Returns:\n    int: The sum of arg1 and the length of arg2.\n\n    Raises:\n    ValueError: If arg1 is not a positive integer.\n    ')
    rendered_docstring = module_0.compose(docstring)
    assert 'Parameters:' in rendered_docstring








def test_parse_wn7ltnha():
    docstring = '\n    This is a short description.\n\n    This is a long description that spans multiple lines.\n\n    Parameters\n    ----------\n    param1 : int\n        This is the first parameter.\n    param2 : str\n        This is the second parameter.\n\n    Returns\n    -------\n    int\n        This is the return value.\n\n    Raises\n    ------\n    ValueError\n        This is raised when something goes wrong.\n    '
    parsed_docstring = module_0.parse(docstring)
    assert isinstance(parsed_docstring, module_0.Docstring)
    assert parsed_docstring.short_description == 'This is a short description.'
    assert parsed_docstring.long_description == 'This is a long description that spans multiple lines.'
    assert len(parsed_docstring.meta) == 4
    assert isinstance(parsed_docstring.meta[0], module_0.DocstringParam)
    assert isinstance(parsed_docstring.meta[1], module_0.DocstringParam)
    assert isinstance(parsed_docstring.meta[2], module_0.DocstringReturns)
    assert isinstance(parsed_docstring.meta[3], module_0.DocstringRaises)





def test_parse_deprecation_ohoyktwr():
    docstring = '\n    This is a short description.\n\n.. deprecated:: 1.2.3\n       This is a deprecation warning.\n    '
    parsed_docstring = module_0.parse(docstring)
    assert isinstance(parsed_docstring, module_0.Docstring)
    assert parsed_docstring.short_description == '    This is a short description.'
    assert len(parsed_docstring.meta) == 1
    assert isinstance(parsed_docstring.meta[0], module_0.DocstringDeprecated)
    assert parsed_docstring.meta[0].version == '1.2.3'
    assert parsed_docstring.meta[0].description == 'This is a deprecation warning.'





def test_parse_example_ermekkhs():
    docstring = '\n    This is a short description.\n\n    Examples\n    --------\n    >>> import numpy as np\n    >>> np.array([1, 2, 3])\n    array([1, 2, 3])\n    '
    parsed_docstring = module_0.parse(docstring)
    assert isinstance(parsed_docstring, module_0.Docstring)
    assert parsed_docstring.short_description == 'This is a short description.'
    assert len(parsed_docstring.meta) == 1
    assert isinstance(parsed_docstring.meta[0], module_0.DocstringExample)
    assert parsed_docstring.meta[0].snippet == '>>> import numpy as np\n>>> np.array([1, 2, 3])'
    assert parsed_docstring.meta[0].description == 'array([1, 2, 3])'





def test_example_9a2kelan():
    assert 1 == 1


