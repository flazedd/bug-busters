from common import Docstring
import typing
from common import DocstringExample
from common import DocstringReturns
import itertools
import numpydoc as module_0
from common import DocstringParam
from common import DocstringStyle
import pytest
from textwrap import dedent
from common import DocstringRaises
import re
from common import DocstringDeprecated
from common import RenderingStyle
import inspect
from common import DocstringMeta
def test_example_ia9v4sll():
    docstring = module_0.parse('\n    This is a short description.\n\n    This is a long description.\n\n    Parameters\n    ----------\n    param1 : str\n        This is a parameter.\n    param2 : int\n        This is another parameter.\n\n    Returns\n    -------\n    str\n        This is a return value.\n\n    Raises\n    ------\n    ValueError\n        This is a value error.\n    ')
    assert isinstance(docstring, module_0.Docstring)





def test_example_e4b9aclj():
    docstring = module_0.parse('\n    This is a short description.\n\n    This is a long description.\n\n    Examples\n    --------\n    >>> import numpy as np\n    >>> np.array([1, 2, 3])\n    array([1, 2, 3])\n    ')
    assert any((isinstance(item, module_0.DocstringExample) for item in docstring.meta))





def test_example_ye6xdyke():
    docstring = module_0.parse('\n    This is a short description.\n\n    This is a long description.\n\n    Parameters\n    ----------\n    param1 : str, optional\n        This is a parameter.\n    ')
    assert any((item.is_optional for item in docstring.params))





def test_example_oz2lcap4():
    docstring = module_0.parse('\n    This is a short description.\n\n    This is a long description.\n\n    Yields\n    ------\n    str\n        This is a yield value.\n    ')
    assert any((item.is_generator for item in docstring.many_returns))





def test_example_7hkt1sym():
    docstring = module_0.parse('\n    This is a short description.\n\n    This is a long description.\n\n    Warnings\n    --------\n    This is a warning.\n    ')
    assert any((item.args[0] == 'warnings' for item in docstring.meta))





def test_example_gxx04c0z():
    docstring = module_0.parse('\n    This is a short description.\n\n    This is a long description.\n\n    Attributes\n    ----------\n    attr1 : str\n        This is an attribute.\n    ')
    assert any((item.args[0] == 'attribute' for item in docstring.params))





def test_example_xt45567c():
    docstring = module_0.parse('\n    This is a short description.\n\n    This is a long description.\n\n    Notes\n    -----\n    This is a note.\n    ')
    assert any((item.args[0] == 'notes' for item in docstring.meta))





def test_example_ax32g0we():
    docstring = module_0.parse('\n        This is a test docstring.\n\n        Parameters\n        ----------\n        param1 : str\n            This is a parameter.\n        param2 : int\n            This is another parameter.\n\n        Returns\n        -------\n        str\n            This is the return value.\n\n        Raises\n        ------\n        ValueError\n            This is a raised error.\n    ')
    assert isinstance(docstring, module_0.Docstring)


