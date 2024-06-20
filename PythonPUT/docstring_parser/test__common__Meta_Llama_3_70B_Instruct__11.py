import pytest
import enum
import common as module_0
import typing
def test_example_331ubdtf():
    docstring = module_0.Docstring()
    docstring.short_description = 'This is a short description'
    docstring.long_description = 'This is a long description'
    docstring.blank_after_short_description = True
    docstring.meta = [module_0.DocstringParam(['arg'], 'description', 'arg_name', 'type_name', True, 'default')]
    assert docstring.description == 'This is a short description\n\nThis is a long description'
    assert len(docstring.params) == 1
    assert docstring.params[0].arg_name == 'arg_name'
    assert docstring.params[0].type_name == 'type_name'
    assert docstring.params[0].is_optional == True
    assert docstring.params[0].default == 'default'


def test_example_3i760l0i():
    docstring = module_0.Docstring()
    docstring.meta = [module_0.DocstringReturns(['return'], 'description', 'type_name', True, 'return_name')]
    assert docstring.returns.return_name == 'return_name'
    assert docstring.returns.type_name == 'type_name'
    assert docstring.returns.is_generator == True
    assert docstring.returns.description == 'description'


def test_example_nr4eok9j():
    docstring = module_0.Docstring()
    docstring.meta = [module_0.DocstringRaises(['exception'], 'description', 'type_name')]
    assert len(docstring.raises) == 1
    assert docstring.raises[0].type_name == 'type_name'
    assert docstring.raises[0].description == 'description'


def test_example_au085hwh():
    docstring = module_0.Docstring()
    docstring.meta = [module_0.DocstringExample(['example'], 'snippet', 'description')]
    assert len(docstring.examples) == 1
    assert docstring.examples[0].snippet == 'snippet'
    assert docstring.examples[0].description == 'description'


def test_example_l1w0gm9d():
    docstring = module_0.Docstring()
    docstring.meta = [module_0.DocstringDeprecated(['deprecated'], 'description', 'version')]
    assert docstring.deprecation.version == 'version'
    assert docstring.deprecation.description == 'description'


def test_example_8qzwawnd():
    docstring = module_0.Docstring()
    docstring.meta = [module_0.DocstringParam(['arg1'], 'description1', 'arg_name1', 'type_name1', True, 'default1'), module_0.DocstringParam(['arg2'], 'description2', 'arg_name2', 'type_name2', False, 'default2')]
    assert len(docstring.params) == 2
    assert docstring.params[0].arg_name == 'arg_name1'
    assert docstring.params[0].type_name == 'type_name1'
    assert docstring.params[0].is_optional == True
    assert docstring.params[0].default == 'default1'
    assert docstring.params[1].arg_name == 'arg_name2'
    assert docstring.params[1].type_name == 'type_name2'
    assert docstring.params[1].is_optional == False
    assert docstring.params[1].default == 'default2'


def test_example_9ps1pj7w():
    docstring = module_0.Docstring()
    docstring.meta = [module_0.DocstringReturns(['return1'], 'description1', 'type_name1', True, 'return_name1'), module_0.DocstringReturns(['return2'], 'description2', 'type_name2', False, 'return_name2')]
    assert len(docstring.many_returns) == 2
    assert docstring.many_returns[0].return_name == 'return_name1'
    assert docstring.many_returns[0].type_name == 'type_name1'
    assert docstring.many_returns[0].is_generator == True
    assert docstring.many_returns[0].description == 'description1'
    assert docstring.many_returns[1].return_name == 'return_name2'
    assert docstring.many_returns[1].type_name == 'type_name2'
    assert docstring.many_returns[1].is_generator == False
    assert docstring.many_returns[1].description == 'description2'


def test_example_y0xf9anf():
    docstring = module_0.Docstring(style=module_0.DocstringStyle.GOOGLE)
    assert docstring.style == module_0.DocstringStyle.GOOGLE


