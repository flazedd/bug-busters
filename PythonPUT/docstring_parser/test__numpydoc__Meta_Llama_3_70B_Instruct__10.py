from common import DocstringStyle
import numpydoc as module_0
import typing
from common import Docstring
import re
import pytest
from common import DocstringReturns
from common import RenderingStyle
from textwrap import dedent
from common import DocstringExample
import itertools
import inspect
from common import DocstringRaises
from common import DocstringMeta
from common import DocstringParam
from common import DocstringDeprecated
def test_example_ig09vqee():
    docstring = module_0.parse('\n    This is a test docstring.\n\n    Parameters\n    ----------\n    param1 : int\n        This is the first parameter.\n    param2 : str\n        This is the second parameter.\n\n    Returns\n    -------\n    int\n        This is the return value.\n\n    Raises\n    ------\n    ValueError\n        If the input is invalid.\n    ')
    assert isinstance(docstring, module_0.Docstring)


def test_example_kr3xi94u():
    docstring = module_0.parse('\n    This is a test docstring.\n\n    Examples\n    --------\n    >>> import numpy as np\n    >>> np.array([1, 2, 3])\n    array([1, 2, 3])\n    ')
    assert isinstance(docstring, module_0.Docstring)


def test_example_w5imlqlp():
    docstring = module_0.parse('\n    This is a test docstring.\n\n    Deprecation\n    ----------\n   .. deprecated:: 1.2.3\n       This function is deprecated.\n    ')
    assert isinstance(docstring.deprecation, module_0.DocstringDeprecated)


def test_example_c2m3k57g():
    docstring = module_0.parse('\n    This is a test docstring.\n\n    Attributes\n    ----------\n    attr1 : int\n        This is the first attribute.\n    attr2 : str\n        This is the second attribute.\n    ')
    assert len(docstring.params) == 2


def test_example_z6r8siy9():
    docstring = module_0.parse('\n    This is a test docstring.\n\n    Yields\n    ------\n    int\n        This is the yield value.\n    ')
    assert isinstance(docstring.returns, module_0.DocstringReturns)


def test_example_xg36ceww():
    docstring = module_0.parse('\n    This is a test docstring.\n\n    See Also\n    --------\n    some_function\n    ')
    assert len(docstring.meta) == 1


def test_example_vt33q6dn():
    docstring = module_0.parse('\n    This is a test docstring.\n\n    Warnings\n    --------\n    Warning\n        This is a warning.\n    ')
    assert len(docstring.meta) == 1


def test_example_hzf0sfob():
    docstring = module_0.parse('\n    This is a test docstring.\n\n    Notes\n    -----\n    This is a note.\n    ')
    assert len(docstring.meta) == 1


