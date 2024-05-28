import re
from common import PARAM_KEYWORDS
from common import DocstringMeta
from common import DocstringStyle
from common import DocstringParam
from common import RenderingStyle
from common import DocstringDeprecated
from common import DocstringRaises
import inspect
import rest as module_0
from common import YIELDS_KEYWORDS
import typing
from common import ParseError
from common import RETURNS_KEYWORDS
from common import Docstring
from common import DocstringReturns
from common import RAISES_KEYWORDS
from common import DEPRECATION_KEYWORDS
import pytest
def test_example_rpfg777s():
    docstring = module_0.parse('\n        Short description.\n\n        Long description.\n\n        :param foo: Foo parameter\n        :param bar: Bar parameter\n        :returns: Return value\n        :raises ValueError: Raised when invalid\n    ')
    assert module_0.compose(docstring) == 'Short description.\n\nLong description.\n\n:param foo: Foo parameter\n:param bar: Bar parameter\n:returns: Return value\n:raises ValueError : Raised when invalid'


def test_example_x5gq0vet():
    docstring = module_0.parse('\n        Short description.\n\n        :param foo: Foo parameter with default value, defaults to 5.\n        :returns: Return value\n    ')
    assert module_0.compose(docstring) == 'Short description.\n\n:param foo: Foo parameter with default value, defaults to 5.\n:returns: Return value'


def test_example_kw24vpu7():
    docstring = module_0.parse('\n        Short description.\n\n        :type foo: int\n        :param foo: Foo parameter\n        :returns: Return value\n    ')
    assert module_0.compose(docstring) == 'Short description.\n\n:param int foo: Foo parameter\n:returns: Return value'


def test_example_pxe8frx0():
    docstring = module_0.parse('\n        Short description.\n\n        :raises ValueError : Raised when invalid\n        :raises TypeError : Raised when type is wrong\n    ')
    assert module_0.compose(docstring) == 'Short description.\n\n:raises ValueError : Raised when invalid\n:raises TypeError : Raised when type is wrong'


def test_example_ydq2sgf7():
    docstring = module_0.parse('\n        Short description.\n\n        :param foo: Foo parameter\n        :param bar: Bar parameter\n        :rtype: int\n        :returns: Return value\n    ')
    assert module_0.compose(docstring) == 'Short description.\n\n:param foo: Foo parameter\n:param bar: Bar parameter\n:returns int: Return value'


def test_example_8n3hxzxo():
    docstring = module_0.parse('\n        Short description.\n\n        :deprecated: description of deprecation\n    ')
    assert module_0.compose(docstring) == 'Short description.\n\n:deprecated: description of deprecation'


def test_example_c7v8i5ni():
    docstring = module_0.parse('\n        Short description.\n\n        :param foo: Foo parameter\n        :type foo: int\n    ')
    assert module_0.compose(docstring) == 'Short description.\n\n:param int foo: Foo parameter'


def test_example_l5ik151l():
    docstring = module_0.parse('\n        Short description.\n\n        :param foo: Foo parameter\n        :param bar: Bar parameter with default value, defaults to 5.\n    ')
    assert module_0.compose(docstring) == 'Short description.\n\n:param foo: Foo parameter\n:param bar: Bar parameter with default value, defaults to 5.'


