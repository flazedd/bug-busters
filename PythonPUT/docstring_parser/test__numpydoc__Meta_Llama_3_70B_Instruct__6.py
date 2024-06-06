from common import Docstring
import re
from textwrap import dedent
from common import DocstringReturns
from common import DocstringRaises
from common import DocstringDeprecated
from common import DocstringStyle
import numpydoc as module_0
from common import RenderingStyle
import typing
import itertools
from common import DocstringExample
from common import DocstringMeta
import pytest
from common import DocstringParam
import inspect
def test_example_05v4bz3f():
    docstring = '\n    This is a sample docstring.\n\n    Parameters:\n    arg1 (int): This is the first argument.\n    arg2 (str): This is the second argument.\n\n    Returns:\n    int: The sum of arg1 and the length of arg2.\n\n    Raises:\n    ValueError: If arg1 is not a positive integer.\n    '
    parsed_docstring = module_0.parse(docstring)
    rendered_docstring = module_0.compose(parsed_docstring, rendering_style=module_0.RenderingStyle.COMPACT, indent='    ')
    assert rendered_docstring.strip() == dedent('\n    This is a sample docstring.\n\n    Parameters:\n    arg1 (int): This is the first argument.\n    arg2 (str): This is the second argument.\n\n    Returns:\n    int: The sum of arg1 and the length of arg2.\n\n    Raises:\n    ValueError: If arg1 is not a positive integer.\n    ').strip()





def test_example_r4bxtlp8():
    docstring = '\n    This is a sample docstring.\n\n    Parameters:\n    arg1 (int, optional): This is the first argument. Defaults to 1.\n    arg2 (str): This is the second argument.\n\n    Returns:\n    int: The sum of arg1 and the length of arg2.\n\n    Raises:\n    ValueError: If arg1 is not a positive integer.\n    '
    parsed_docstring = module_0.parse(docstring)
    rendered_docstring = module_0.compose(parsed_docstring, rendering_style=module_0.RenderingStyle.COMPACT, indent='    ')
    assert rendered_docstring.strip() == dedent('\n    This is a sample docstring.\n\n    Parameters:\n    arg1 (int, optional): This is the first argument. Defaults to 1.\n    arg2 (str): This is the second argument.\n\n    Returns:\n    int: The sum of arg1 and the length of arg2.\n\n    Raises:\n    ValueError: If arg1 is not a positive integer.\n    ').strip()





def test_example_zudd60m2():
    docstring = module_0.parse('\n    This is a short description.\n\n    This is a long description.\n\n    Parameters\n    ----------\n    param1 : int\n        This is a parameter.\n    param2 : str\n        This is another parameter.\n\n    Returns\n    -------\n    int\n        This is a return value.\n\n    Raises\n    ------\n    ValueError\n        This is an exception.\n    ')
    assert isinstance(docstring, module_0.Docstring)
    assert docstring.short_description == 'This is a short description.'
    assert docstring.long_description == 'This is a long description.'
    assert len(docstring.meta) == 4
    assert isinstance(docstring.meta[0], module_0.DocstringParam)
    assert isinstance(docstring.meta[1], module_0.DocstringParam)
    assert isinstance(docstring.meta[2], module_0.DocstringReturns)
    assert isinstance(docstring.meta[3], module_0.DocstringRaises)


def test_example_ohc4fsd9():
    docstring = module_0.parse('\n    This is a short description.\n\n    This is a long description.\n\n    Parameters\n    ----------\n    param1 : int, optional\n        This is an optional parameter.\n    param2 : str\n        This is another parameter.\n\n    Returns\n    -------\n    int\n        This is a return value.\n\n    Yields\n    ------\n    str\n        This is a yield value.\n    ')
    assert isinstance(docstring, module_0.Docstring)
    assert docstring.short_description == 'This is a short description.'
    assert docstring.long_description == 'This is a long description.'
    assert len(docstring.meta) == 4
    assert isinstance(docstring.meta[0], module_0.DocstringParam)
    assert docstring.meta[0].is_optional == True
    assert isinstance(docstring.meta[1], module_0.DocstringParam)
    assert isinstance(docstring.meta[2], module_0.DocstringReturns)
    assert isinstance(docstring.meta[3], module_0.DocstringReturns)
    assert docstring.meta[3].is_generator == True


def test_example_0c2fbjah():
    docstring = module_0.parse('\n    This is a short description.\n\n    This is a long description.\n\n    Attributes\n    ----------\n    attr1 : int\n        This is an attribute.\n    attr2 : str\n        This is another attribute.\n\n    Warnings\n    --------\n    Warning\n        This is a warning.\n    ')
    assert isinstance(docstring, module_0.Docstring)
    assert docstring.short_description == 'This is a short description.'
    assert docstring.long_description == 'This is a long description.'
    assert len(docstring.meta) == 3
    assert isinstance(docstring.meta[0], module_0.DocstringParam)
    assert isinstance(docstring.meta[1], module_0.DocstringParam)
    assert isinstance(docstring.meta[2], module_0.DocstringMeta)
    assert docstring.meta[2].args[0] == 'warnings'


def test_example_34rodcvs():
    docstring = module_0.parse('\n    This is a short description.\n\n    This is a long description.\n\n    Examples\n    --------\n    >>> import numpy.matlib\n    >>> np.matlib.empty((2, 2))    # filled with random data\n    matrix([[  6.76425276e-320,   9.79033856e-307], # random\n            [  7.39337286e-309,   3.22135945e-309]])\n    >>> np.matlib.empty((2, 2), dtype=int)\n    matrix([[ 6600475,        0], # random\n            [ 6586976, 22740995]])\n    ')
    assert isinstance(docstring, module_0.Docstring)
    assert docstring.short_description == 'This is a short description.'
    assert docstring.long_description == 'This is a long description.'
    assert len(docstring.meta) == 2
    assert all((isinstance(example, module_0.DocstringExample) for example in docstring.meta))
    assert docstring.meta[0].snippet.startswith('>>> import numpy.matlib')
    assert docstring.meta[1].snippet.startswith('>>> np.matlib.empty((2, 2), dtype=int)')


def test_example_nt0fm3wm():
    docstring = module_0.parse('\n    This is a short description.\n\n    This is a long description.\n\n    See Also\n    --------\n    numpy.array\n    numpy.matlib\n    ')
    assert isinstance(docstring, module_0.Docstring)
    assert docstring.short_description == 'This is a short description.'
    assert docstring.long_description == 'This is a long description.'
    assert len(docstring.meta) == 1
    assert isinstance(docstring.meta[0], module_0.DocstringMeta)
    assert docstring.meta[0].args[0] == 'see_also'
    assert len(docstring.meta[0].description.splitlines()) == 2
    assert 'numpy.array' in docstring.meta[0].description
    assert 'numpy.matlib' in docstring.meta[0].description


def test_example_3wz78ueg():
    docstring = module_0.parse('\n    This is a short description.\n\n    This is a long description.\n\n    Notes\n    -----\n    This is a note.\n    This is another note.\n    ')
    assert isinstance(docstring, module_0.Docstring)
    assert docstring.short_description == 'This is a short description.'
    assert docstring.long_description == 'This is a long description.'
    assert len(docstring.meta) == 1
    assert isinstance(docstring.meta[0], module_0.DocstringMeta)
    assert docstring.meta[0].args[0] == 'notes'
    assert len(docstring.meta[0].description.splitlines()) == 2
    assert 'This is a note.' in docstring.meta[0].description
    assert 'This is another note.' in docstring.meta[0].description


