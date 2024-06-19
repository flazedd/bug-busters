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
def test_example_ipbcl293():
    docstring_text = '\n    This is a short description.\n\n    This is a long description.\n\n    :param int x: This is a parameter description.\n    :param y: This is another parameter description.\n    :returns: This is a return description.\n    :raises ValueError: This is a raise description.\n    '
    parsed_docstring = module_0.parse(docstring_text)
    rendered_docstring = module_0.compose(parsed_docstring)
    assert rendered_docstring == '\nThis is a short description.\n\nThis is a long description.\n\n:param int x: This is a parameter description.\n:param y: This is another parameter description.\n:returns: This is a return description.\n:raises ValueError : This is a raise description.\n'.strip()








def test_example_h3fivvfi():
    docstring_text = '\n    This is a short description.\n\n    :param int x: This is a parameter description.\n    :param y: This is another parameter description.\n    :returns: This is a return description.\n    :raises ValueError: This is a raise description.\n    :raises TypeError: This is another raise description.\n    '
    parsed_docstring = module_0.parse(docstring_text)
    rendered_docstring = module_0.compose(parsed_docstring)
    assert rendered_docstring == '\nThis is a short description.\n\n:param int x: This is a parameter description.\n:param y: This is another parameter description.\n:returns: This is a return description.\n:raises ValueError : This is a raise description.\n:raises TypeError : This is another raise description.\n'.strip()








def test_example_qrnwr1mo():
    docstring_text = '\n    This is a short description.\n\n    This is a long description.\n\n    :param x: This is a parameter description.\n    :param y: This is another parameter description.\n    :deprecated: This is a deprecated description.\n    '
    parsed_docstring = module_0.parse(docstring_text)
    rendered_docstring = module_0.compose(parsed_docstring)
    assert rendered_docstring == '\nThis is a short description.\n\nThis is a long description.\n\n:param x: This is a parameter description.\n:param y: This is another parameter description.\n:deprecated: This is a deprecated description.\n'.strip()








def test_example_r0vmurvj():
    docstring_text = '\n    This is a short description.\n\n    This is a long description.\n\n    :param x: This is a parameter description.\n    :param y: This is another parameter description.\n    :raises ValueError: This is a raise description.\n    :raises TypeError: This is another raise description.\n    '
    parsed_docstring = module_0.parse(docstring_text)
    rendered_docstring = module_0.compose(parsed_docstring)
    assert rendered_docstring == '\nThis is a short description.\n\nThis is a long description.\n\n:param x: This is a parameter description.\n:param y: This is another parameter description.\n:raises ValueError : This is a raise description.\n:raises TypeError : This is another raise description.\n'.strip()








def test_example_orjc959f():
    docstring_text = '\n    This is a short description.\n\n    This is a long description.\n\n    :param x: This is a parameter description.\n    :param y: This is another parameter description.\n    :returns str: This is a return description.\n    '
    parsed_docstring = module_0.parse(docstring_text)
    rendered_docstring = module_0.compose(parsed_docstring)
    assert rendered_docstring == '\nThis is a short description.\n\nThis is a long description.\n\n:param x: This is a parameter description.\n:param y: This is another parameter description.\n:returns str: This is a return description.\n'.strip()








def test_example_avh9orjl():
    docstring_text = '\n    This is a short description.\n\n    This is a long description.\n\n    :param x: This is a parameter description.\n    :param y: This is another parameter description.\n    :yields int: This is a yield description.\n    '
    parsed_docstring = module_0.parse(docstring_text)
    rendered_docstring = module_0.compose(parsed_docstring)
    assert rendered_docstring == '\nThis is a short description.\n\nThis is a long description.\n\n:param x: This is a parameter description.\n:param y: This is another parameter description.\n:yields int: This is a yield description.\n'.strip()








def test_example_njce2pqp():
    text = '\n    This is a short description.\n\n    This is a long description.\n\n    :param int x: This is a parameter description.\n    :param y: This is another parameter description.\n    :returns: This is a return description.\n    :raises ValueError: This is a raise description.\n    '
    docstring = module_0.parse(text)
    result = module_0.compose(docstring, rendering_style=module_0.RenderingStyle.COMPACT)
    assert result == '\nThis is a short description.\n\nThis is a long description.\n\n:param int x: This is a parameter description.\n:param y: This is another parameter description.\n:returns: This is a return description.\n:raises ValueError : This is a raise description.\n'.strip()





def test_example_44mqrw4n():
    docstring_text = '\n    This is a test docstring.\n\n    :param foo: This is a parameter.\n    :param bar: This is another parameter.\n    :returns: This is the return value.\n    :raises ValueError: This is an error.\n    '
    parsed_docstring = module_0.parse(docstring_text)
    rendered_docstring = module_0.compose(parsed_docstring)
    assert rendered_docstring.startswith('This is a test docstring.')


