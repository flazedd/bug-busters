import pytest
import typing
import common as module_0
import enum
def test_example_j19o15lr():
    docstring = module_0.Docstring()
    docstring.short_description = 'This is a short description'
    docstring.long_description = 'This is a long description'
    docstring.blank_after_short_description = True
    param = module_0.DocstringParam(['arg'], 'description', 'arg_name', 'type_name', True, 'default')
    docstring.meta.append(param)
    assert docstring.description == 'This is a short description\n\nThis is a long description'
    assert len(docstring.params) == 1


