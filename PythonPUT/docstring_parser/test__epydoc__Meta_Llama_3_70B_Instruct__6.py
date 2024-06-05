from common import DocstringRaises
import re
from common import DocstringReturns
from common import Docstring
import inspect
import epydoc as module_0
from common import ParseError
import typing
from common import DocstringStyle
from common import DocstringParam
from common import RenderingStyle
import pytest
from common import DocstringMeta
def test_example_b6737bym():
    docstring_text = '\n    This is a short description.\n\n    This is a long description that spans multiple lines.\n\n    @param foo: This is a parameter description.\n    @type foo: int\n    @return: This is a return description.\n    @rtype: str\n    @raise ValueError: This is a raise description.\n    @meta meta_key: This is a meta description.\n    '
    parsed_docstring = module_0.parse(docstring_text)
    rendered_docstring = module_0.compose(parsed_docstring, RenderingStyle.COMPACT, indent='    ')
    assert rendered_docstring == '\nThis is a short description.\n\nThis is a long description that spans multiple lines.\n\n@type foo: int\n@param foo: This is a parameter description.\n@return: This is a return description.\n@rtype: str\n@raise ValueError: This is a raise description.\n@meta meta_key: This is a meta description.\n'.strip()


