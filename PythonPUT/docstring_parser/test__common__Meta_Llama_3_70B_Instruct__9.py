import pytest
import typing
import common as module_0
import enum
def test_example_2r65do9i():
    docstring = module_0.Docstring()
    docstring.short_description = 'This is a short description'
    docstring.long_description = 'This is a long description'
    docstring.blank_after_short_description = True
    param = module_0.DocstringParam(['arg'], 'description', 'arg_name', 'type_name', True, 'default')
    docstring.meta.append(param)
    assert docstring.description == 'This is a short description\n\nThis is a long description'
    assert len(docstring.params) == 1
    assert docstring.params[0].arg_name == 'arg_name'


def test_example_1wu17ywp():
    docstring = module_0.Docstring()
    raises = module_0.DocstringRaises(['exception'], 'description', 'type_name')
    docstring.meta.append(raises)
    assert len(docstring.raises) == 1
    assert docstring.raises[0].type_name == 'type_name'


def test_example_eai6f5e7():
    docstring = module_0.Docstring()
    example = module_0.DocstringExample(['example'], 'snippet', 'description')
    docstring.meta.append(example)
    assert len(docstring.examples) == 1
    assert docstring.examples[0].snippet == 'snippet'


def test_example_p3jqvni2():
    docstring = module_0.Docstring(style=module_0.DocstringStyle.GOOGLE)
    assert docstring.style == module_0.DocstringStyle.GOOGLE


def test_example_bcajthzn():
    docstring = module_0.Docstring()
    returns = module_0.DocstringReturns(['return'], 'description', 'type_name', True, 'return_name')
    docstring.meta.append(returns)
    assert docstring.returns.type_name == 'type_name'
    assert docstring.many_returns[0].type_name == 'type_name'


def test_example_zhb26ryg():
    docstring = module_0.Docstring()
    deprecation = module_0.DocstringDeprecated(['deprecation'], 'description', 'version')
    docstring.meta.append(deprecation)
    assert docstring.deprecation.version == 'version'


def test_example_y6l6yvsb():
    docstring = module_0.Docstring()
    assert docstring.description is None
    assert len(docstring.meta) == 0
    assert docstring.params == []
    assert docstring.raises == []
    assert docstring.returns is None
    assert docstring.many_returns == []
    assert docstring.deprecation is None
    assert docstring.examples == []


def test_example_h61pmoif():
    docstring = module_0.Docstring()
    docstring.blank_after_short_description = True
    assert docstring.description is None
    docstring.short_description = 'This is a short description'
    assert docstring.description == 'This is a short description\n'


