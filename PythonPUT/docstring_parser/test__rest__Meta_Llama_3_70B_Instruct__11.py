from common import Docstring
import pytest
from common import DEPRECATION_KEYWORDS
from common import RenderingStyle
import typing
from common import YIELDS_KEYWORDS
from common import ParseError
from common import PARAM_KEYWORDS
from common import DocstringRaises
from common import DocstringStyle
from common import DocstringMeta
import rest as module_0
import re
from common import DocstringParam
from common import RAISES_KEYWORDS
from common import RETURNS_KEYWORDS
from common import DocstringReturns
import inspect
from common import DocstringDeprecated
def test_example_rn3hwhhj():

    def _build_meta_test():
        args = ['param', 'type_name', 'arg_name']
        desc = 'This is a description.'
        meta = module_0._build_meta(args, desc)
        assert isinstance(meta, module_0.DocstringParam)
        assert meta.arg_name == 'arg_name'
        assert meta.type_name == 'type_name'
        assert meta.description == 'This is a description.'
        assert meta.is_optional == False
        assert meta.default == None
    _build_meta_test()
    assert 1 == 1





def test_example_byxmzskg():

    def _parse_test():
        text = 'This is a short description.\n\nThis is a long description.'
        docstring = module_0.parse(text)
        assert docstring.short_description == 'This is a short description.'
        assert docstring.long_description == 'This is a long description.'
        assert docstring.blank_after_short_description
        assert not docstring.blank_after_long_description
    _parse_test()
    assert 1 == 1





def test_example_qrvy63n0():

    def _compose_test():
        docstring = module_0.Docstring(style=module_0.DocstringStyle.REST)
        docstring.short_description = 'This is a short description.'
        docstring.long_description = 'This is a long description.'
        rendered = module_0.compose(docstring, rendering_style=module_0.RenderingStyle.COMPACT)
        assert rendered == 'This is a short description.\nThis is a long description.'
    _compose_test()
    assert 1 == 1





def test_example_hzqogoep():

    def _parse_test():
        text = ':param arg_name: This is a description.'
        docstring = module_0.parse(text)
        assert len(docstring.meta) == 1
        meta = docstring.meta[0]
        assert isinstance(meta, module_0.DocstringParam)
        assert meta.arg_name == 'arg_name'
        assert meta.description == 'This is a description.'
    _parse_test()
    assert 1 == 1





def test_example_nvw7hesv():

    def _parse_test():
        text = ':returns: This is a return description.\n:rtype: int'
        docstring = module_0.parse(text)
        assert len(docstring.meta) == 1
        meta = docstring.meta[0]
        assert isinstance(meta, module_0.DocstringReturns)
        assert meta.type_name == 'int'
        assert meta.description == 'This is a return description.'
    _parse_test()
    assert 1 == 1





def test_example_yy2dohlo():

    def _parse_test():
        text = ':raises Exception: This is an exception description.'
        docstring = module_0.parse(text)
        assert len(docstring.meta) == 1
        meta = docstring.meta[0]
        assert isinstance(meta, module_0.DocstringRaises)
        assert meta.type_name == 'Exception'
        assert meta.description == 'This is an exception description.'
    _parse_test()
    assert 1 == 1





def test_example_8wvawea7():
    text = 'This is a test function.\n\n    :param foo: This is a parameter.\n    :param bar: This is another parameter.\n    :returns: This is the return value.\n    '
    parsed_docstring = module_0.parse(inspect.cleandoc(text))
    rendered_docstring = module_0.compose(parsed_docstring, module_0.RenderingStyle.COMPACT, indent='    ')
    assert rendered_docstring == inspect.cleandoc(text)


def test_example_3r6avj2m():
    text = 'This is a test function.\n\n    :param foo: This is a parameter.\n    :param bar: This is another parameter.\n    :yields: This is a yield value.\n    '
    parsed_docstring = module_0.parse(text)
    rendered_docstring = module_0.compose(parsed_docstring, module_0.RenderingStyle.COMPACT, indent='    ')
    assert rendered_docstring == inspect.cleandoc(text)


