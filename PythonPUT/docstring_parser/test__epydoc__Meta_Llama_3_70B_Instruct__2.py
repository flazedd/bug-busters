from common import Docstring
import re
import pytest
import typing
from common import RenderingStyle
from common import DocstringReturns
from common import DocstringRaises
from common import ParseError
import epydoc as module_0
from common import DocstringMeta
from common import DocstringParam
from common import DocstringStyle
import inspect
def test_example_4h9cgddm():
    text = '\n    This is a short description.\n\n    This is a long description.\n\n    @param foo: This is a parameter description.\n    @return: This is a return description.\n    @raise ValueError: This is a raise description.\n    @meta some_meta: This is a meta description.\n    '
    docstring = module_0.parse(text)
    assert module_0.compose(docstring) == '\nThis is a short description.\n\nThis is a long description.\n\n@param foo: This is a parameter description.\n@return: This is a return description.\n@raise ValueError: This is a raise description.\n@meta some_meta: This is a meta description.\n'.strip()








def test_example_nbywd8ot():
    text = '\n    This is a short description.\n\n    @param foo: This is a parameter description.\n    @return: This is a return description.\n    @raise ValueError: This is a raise description.\n    @meta some_meta: This is a meta description.\n    '
    docstring = module_0.parse(text)
    assert module_0.compose(docstring) == '\nThis is a short description.\n\n@param foo: This is a parameter description.\n@return: This is a return description.\n@raise ValueError: This is a raise description.\n@meta some_meta: This is a meta description.\n'.strip()








def test_example_725mfyel():
    text = '\n    This is a short description.\n\n    This is a long description.\n\n    @param foo: This is a parameter description with multiple lines.\n    This is the second line of the description.\n    @return: This is a return description.\n    @raise ValueError: This is a raise description.\n    @meta some_meta: This is a meta description.\n    '
    docstring = module_0.parse(text)
    assert module_0.compose(docstring) == '\nThis is a short description.\n\nThis is a long description.\n\n@param foo: This is a parameter description with multiple lines.\n    This is the second line of the description.\n@return: This is a return description.\n@raise ValueError: This is a raise description.\n@meta some_meta: This is a meta description.\n'.strip()








def test_example_qny2q0tw():
    text = '\n    This is a short description.\n\n    This is a long description.\n\n    @param foo: This is a parameter description.\n    @param bar: This is another parameter description with a default value, defaults to 10.\n    @return: This is a return description.\n    @raise ValueError: This is a raise description.\n    @meta some_meta: This is a meta description.\n    '
    docstring = module_0.parse(text)
    assert module_0.compose(docstring) == '\nThis is a short description.\n\nThis is a long description.\n\n@param foo: This is a parameter description.\n@param bar: This is another parameter description with a default value, defaults to 10.\n@return: This is a return description.\n@raise ValueError: This is a raise description.\n@meta some_meta: This is a meta description.\n'.strip()








def test_example_c51o0cuw():
    text = '\n    This is a short description.\n\n    @param foo: This is a parameter description.\n    @return: This is a return description with multiple lines.\n    This is the second line of the return description.\n    @raise ValueError: This is a raise description.\n    @meta some_meta: This is a meta description.\n    '
    docstring = module_0.parse(text)
    assert module_0.compose(docstring) == '\nThis is a short description.\n\n@param foo: This is a parameter description.\n@return: This is a return description with multiple lines.\n    This is the second line of the return description.\n@raise ValueError: This is a raise description.\n@meta some_meta: This is a meta description.\n'.strip()








def test_example_p7kb5eh2():
    text = '\n    This is a short description.\n\n    @param foo: This is a parameter description with a default value, defaults to 10.\n    @return: This is a return description.\n    @raise ValueError: This is a raise description.\n    @meta some_meta: This is a meta description.\n    '
    docstring = module_0.parse(text)
    assert module_0.compose(docstring) == '\nThis is a short description.\n\n@param foo: This is a parameter description with a default value, defaults to 10.\n@return: This is a return description.\n@raise ValueError: This is a raise description.\n@meta some_meta: This is a meta description.\n'.strip()








def test_example_ytkltmnt():
    docstring = module_0.parse('This is a short description.\n\nThis is a long description.\n\n@param foo: This is a parameter description.\n@return: This is a return description.')
    assert docstring.short_description == 'This is a short description.'





def test_example_35qjabh0():
    docstring = module_0.parse('\n    This is a short description.\n\n    This is a long description.\n\n    @param foo: This is a parameter description.\n    @return: This is a return description.\n    @raise ValueError: This is a raise description.\n    ')
    assert docstring.short_description == 'This is a short description.'


