import common as module_0
import enum
import pytest
import typing
def test_docstring_init_9zu6ubwh():
    docstring = module_0.Docstring(style=module_0.DocstringStyle.GOOGLE)
    assert docstring.style == module_0.DocstringStyle.GOOGLE





def test_docstring_description_v3iggdci():
    docstring = module_0.Docstring()
    docstring.short_description = 'This is a short description'
    docstring.long_description = 'This is a long description'
    assert docstring.description == 'This is a short description\nThis is a long description'





def test_docstring_params_ya3ru1pe():
    docstring = module_0.Docstring()
    param_meta = module_0.DocstringParam(['arg'], 'Description', 'arg', 'int', False, None)
    docstring.meta.append(param_meta)
    assert docstring.params[0].type_name == 'int'





def test_docstring_deprecation_yqmbi0v1():
    docstring = module_0.Docstring()
    deprecation_meta = module_0.DocstringDeprecated([], 'Deprecation note', '1.0')
    docstring.meta.append(deprecation_meta)
    assert docstring.deprecation.version == '1.0'





def test_docstring_examples_cisgrdl4():
    docstring = module_0.Docstring()
    example_meta = module_0.DocstringExample(['example'], 'snippet', 'Description')
    docstring.meta.append(example_meta)
    assert docstring.examples[0].snippet == 'snippet'





def test_docstring_raises_qupo3irw():
    docstring = module_0.Docstring()
    raises_meta = module_0.DocstringRaises(['ValueError'], 'Raised when something happens', 'ValueError')
    docstring.meta.append(raises_meta)
    assert docstring.raises[0].type_name == 'ValueError'





def test_docstring_blank_after_short_description_tjpu7bh3():
    docstring = module_0.Docstring()
    docstring.short_description = 'This is a short description'
    docstring.blank_after_short_description = True
    docstring.long_description = 'This is a long description'
    assert docstring.description == 'This is a short description\n\nThis is a long description'





def test_example_dc0htply():
    docstring = module_0.Docstring()
    docstring.meta = [module_0.DocstringParam(['arg'], 'description', 'arg_name', 'type_name', False, 'default')]
    assert len(docstring.params) == 1


