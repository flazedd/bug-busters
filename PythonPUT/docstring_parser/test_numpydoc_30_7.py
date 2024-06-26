# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import numpydoc as module_0
import common as module_1
import inspect as module_2
import textwrap as module_3
import ast as module_4


def test_case_0():
    str_0 = "~qh^\r0g"
    docstring_0 = module_0.parse(str_0)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description == "~qh^\r0g"
    assert docstring_0.long_description is None
    assert docstring_0.blank_after_short_description is False
    assert docstring_0.blank_after_long_description is False
    assert docstring_0.meta == []
    assert docstring_0.style == module_1.DocstringStyle.NUMPYDOC
    assert (
        f"{type(module_0.KV_REGEX).__module__}.{type(module_0.KV_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.PARAM_KEY_REGEX).__module__}.{type(module_0.PARAM_KEY_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.PARAM_OPTIONAL_REGEX).__module__}.{type(module_0.PARAM_OPTIONAL_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.PARAM_DEFAULT_REGEX).__module__}.{type(module_0.PARAM_DEFAULT_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.RETURN_KEY_REGEX).__module__}.{type(module_0.RETURN_KEY_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.DEFAULT_SECTIONS).__module__}.{type(module_0.DEFAULT_SECTIONS).__qualname__}"
        == "builtins.list"
    )
    assert len(module_0.DEFAULT_SECTIONS) == 31
    assert (
        f"{type(module_1.Docstring.description).__module__}.{type(module_1.Docstring.description).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.params).__module__}.{type(module_1.Docstring.params).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.raises).__module__}.{type(module_1.Docstring.raises).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.returns).__module__}.{type(module_1.Docstring.returns).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.many_returns).__module__}.{type(module_1.Docstring.many_returns).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.deprecation).__module__}.{type(module_1.Docstring.deprecation).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.examples).__module__}.{type(module_1.Docstring.examples).__qualname__}"
        == "builtins.property"
    )


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    docstring_0 = module_0.parse(none_type_0)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description is None
    assert docstring_0.long_description is None
    assert docstring_0.blank_after_short_description is False
    assert docstring_0.blank_after_long_description is False
    assert docstring_0.meta == []
    assert docstring_0.style == module_1.DocstringStyle.NUMPYDOC
    assert (
        f"{type(module_0.KV_REGEX).__module__}.{type(module_0.KV_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.PARAM_KEY_REGEX).__module__}.{type(module_0.PARAM_KEY_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.PARAM_OPTIONAL_REGEX).__module__}.{type(module_0.PARAM_OPTIONAL_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.PARAM_DEFAULT_REGEX).__module__}.{type(module_0.PARAM_DEFAULT_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.RETURN_KEY_REGEX).__module__}.{type(module_0.RETURN_KEY_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.DEFAULT_SECTIONS).__module__}.{type(module_0.DEFAULT_SECTIONS).__qualname__}"
        == "builtins.list"
    )
    assert len(module_0.DEFAULT_SECTIONS) == 31
    assert (
        f"{type(module_1.Docstring.description).__module__}.{type(module_1.Docstring.description).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.params).__module__}.{type(module_1.Docstring.params).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.raises).__module__}.{type(module_1.Docstring.raises).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.returns).__module__}.{type(module_1.Docstring.returns).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.many_returns).__module__}.{type(module_1.Docstring.many_returns).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.deprecation).__module__}.{type(module_1.Docstring.deprecation).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.examples).__module__}.{type(module_1.Docstring.examples).__qualname__}"
        == "builtins.property"
    )
    module_2.getouterframes(docstring_0, docstring_0)


def test_case_2():
    docstring_0 = module_1.Docstring()
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description is None
    assert docstring_0.long_description is None
    assert docstring_0.blank_after_short_description is False
    assert docstring_0.blank_after_long_description is False
    assert docstring_0.meta == []
    assert docstring_0.style is None
    assert module_1.PARAM_KEYWORDS == {
        "parameter",
        "argument",
        "key",
        "keyword",
        "param",
        "arg",
        "attribute",
    }
    assert module_1.RAISES_KEYWORDS == {"raise", "raises", "except", "exception"}
    assert module_1.DEPRECATION_KEYWORDS == {"deprecation", "deprecated"}
    assert module_1.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_1.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_1.EXAMPLES_KEYWORDS == {"example", "examples"}
    assert (
        f"{type(module_1.Docstring.description).__module__}.{type(module_1.Docstring.description).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.params).__module__}.{type(module_1.Docstring.params).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.raises).__module__}.{type(module_1.Docstring.raises).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.returns).__module__}.{type(module_1.Docstring.returns).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.many_returns).__module__}.{type(module_1.Docstring.many_returns).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.deprecation).__module__}.{type(module_1.Docstring.deprecation).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.examples).__module__}.{type(module_1.Docstring.examples).__qualname__}"
        == "builtins.property"
    )
    str_0 = module_0.compose(docstring_0)
    assert str_0 == ""
    assert (
        f"{type(module_0.KV_REGEX).__module__}.{type(module_0.KV_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.PARAM_KEY_REGEX).__module__}.{type(module_0.PARAM_KEY_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.PARAM_OPTIONAL_REGEX).__module__}.{type(module_0.PARAM_OPTIONAL_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.PARAM_DEFAULT_REGEX).__module__}.{type(module_0.PARAM_DEFAULT_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.RETURN_KEY_REGEX).__module__}.{type(module_0.RETURN_KEY_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.DEFAULT_SECTIONS).__module__}.{type(module_0.DEFAULT_SECTIONS).__qualname__}"
        == "builtins.list"
    )
    assert len(module_0.DEFAULT_SECTIONS) == 31


def test_case_3():
    str_0 = "]q [?K%uQ\x0bv!5k{!#"
    sphinx_section_0 = module_0._SphinxSection(str_0, str_0)
    assert (
        f"{type(sphinx_section_0).__module__}.{type(sphinx_section_0).__qualname__}"
        == "numpydoc._SphinxSection"
    )
    assert sphinx_section_0.title == "]q [?K%uQ\x0bv!5k{!#"
    assert sphinx_section_0.key == "]q [?K%uQ\x0bv!5k{!#"
    assert (
        f"{type(module_0.KV_REGEX).__module__}.{type(module_0.KV_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.PARAM_KEY_REGEX).__module__}.{type(module_0.PARAM_KEY_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.PARAM_OPTIONAL_REGEX).__module__}.{type(module_0.PARAM_OPTIONAL_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.PARAM_DEFAULT_REGEX).__module__}.{type(module_0.PARAM_DEFAULT_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.RETURN_KEY_REGEX).__module__}.{type(module_0.RETURN_KEY_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.DEFAULT_SECTIONS).__module__}.{type(module_0.DEFAULT_SECTIONS).__qualname__}"
        == "builtins.list"
    )
    assert len(module_0.DEFAULT_SECTIONS) == 31
    assert (
        f"{type(module_0._SphinxSection.title_pattern).__module__}.{type(module_0._SphinxSection.title_pattern).__qualname__}"
        == "builtins.property"
    )


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "\n?*z3xH3dnZTTJ"
    str_1 = 'J<f"L`C|u\r'
    section_0 = module_3.dedent(str_0)
    assert section_0 == "\n?*z3xH3dnZTTJ"
    examples_section_0 = module_0.ExamplesSection(str_1, str_1)
    assert (
        f"{type(examples_section_0).__module__}.{type(examples_section_0).__qualname__}"
        == "numpydoc.ExamplesSection"
    )
    assert examples_section_0.title == 'J<f"L`C|u\r'
    assert examples_section_0.key == 'J<f"L`C|u\r'
    assert (
        f"{type(module_0.KV_REGEX).__module__}.{type(module_0.KV_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.PARAM_KEY_REGEX).__module__}.{type(module_0.PARAM_KEY_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.PARAM_OPTIONAL_REGEX).__module__}.{type(module_0.PARAM_OPTIONAL_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.PARAM_DEFAULT_REGEX).__module__}.{type(module_0.PARAM_DEFAULT_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.RETURN_KEY_REGEX).__module__}.{type(module_0.RETURN_KEY_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.DEFAULT_SECTIONS).__module__}.{type(module_0.DEFAULT_SECTIONS).__qualname__}"
        == "builtins.list"
    )
    assert len(module_0.DEFAULT_SECTIONS) == 31
    param_section_0 = module_0.ParamSection(str_1, str_1)
    assert (
        f"{type(param_section_0).__module__}.{type(param_section_0).__qualname__}"
        == "numpydoc.ParamSection"
    )
    assert param_section_0.title == 'J<f"L`C|u\r'
    assert param_section_0.key == 'J<f"L`C|u\r'
    module_0.NumpydocParser(param_section_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    numpydoc_parser_0 = module_0.NumpydocParser()
    assert (
        f"{type(numpydoc_parser_0).__module__}.{type(numpydoc_parser_0).__qualname__}"
        == "numpydoc.NumpydocParser"
    )
    assert (
        f"{type(numpydoc_parser_0.sections).__module__}.{type(numpydoc_parser_0.sections).__qualname__}"
        == "builtins.dict"
    )
    assert len(numpydoc_parser_0.sections) == 31
    assert (
        f"{type(numpydoc_parser_0.titles_re).__module__}.{type(numpydoc_parser_0.titles_re).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.KV_REGEX).__module__}.{type(module_0.KV_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.PARAM_KEY_REGEX).__module__}.{type(module_0.PARAM_KEY_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.PARAM_OPTIONAL_REGEX).__module__}.{type(module_0.PARAM_OPTIONAL_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.PARAM_DEFAULT_REGEX).__module__}.{type(module_0.PARAM_DEFAULT_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.RETURN_KEY_REGEX).__module__}.{type(module_0.RETURN_KEY_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.DEFAULT_SECTIONS).__module__}.{type(module_0.DEFAULT_SECTIONS).__qualname__}"
        == "builtins.list"
    )
    assert len(module_0.DEFAULT_SECTIONS) == 31
    numpydoc_parser_0.add_section(numpydoc_parser_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "L\no-'x@4aJHl{b7"
    numpydoc_parser_0 = module_0.NumpydocParser()
    assert (
        f"{type(numpydoc_parser_0).__module__}.{type(numpydoc_parser_0).__qualname__}"
        == "numpydoc.NumpydocParser"
    )
    assert (
        f"{type(numpydoc_parser_0.sections).__module__}.{type(numpydoc_parser_0.sections).__qualname__}"
        == "builtins.dict"
    )
    assert len(numpydoc_parser_0.sections) == 31
    assert (
        f"{type(numpydoc_parser_0.titles_re).__module__}.{type(numpydoc_parser_0.titles_re).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.KV_REGEX).__module__}.{type(module_0.KV_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.PARAM_KEY_REGEX).__module__}.{type(module_0.PARAM_KEY_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.PARAM_OPTIONAL_REGEX).__module__}.{type(module_0.PARAM_OPTIONAL_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.PARAM_DEFAULT_REGEX).__module__}.{type(module_0.PARAM_DEFAULT_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.RETURN_KEY_REGEX).__module__}.{type(module_0.RETURN_KEY_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.DEFAULT_SECTIONS).__module__}.{type(module_0.DEFAULT_SECTIONS).__qualname__}"
        == "builtins.list"
    )
    assert len(module_0.DEFAULT_SECTIONS) == 31
    docstring_0 = numpydoc_parser_0.parse(str_0)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description == "L"
    assert docstring_0.long_description == "o-'x@4aJHl{b7"
    assert docstring_0.blank_after_short_description is False
    assert docstring_0.blank_after_long_description is False
    assert docstring_0.meta == []
    assert docstring_0.style == module_1.DocstringStyle.NUMPYDOC
    assert (
        f"{type(module_1.Docstring.description).__module__}.{type(module_1.Docstring.description).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.params).__module__}.{type(module_1.Docstring.params).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.raises).__module__}.{type(module_1.Docstring.raises).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.returns).__module__}.{type(module_1.Docstring.returns).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.many_returns).__module__}.{type(module_1.Docstring.many_returns).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.deprecation).__module__}.{type(module_1.Docstring.deprecation).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.examples).__module__}.{type(module_1.Docstring.examples).__qualname__}"
        == "builtins.property"
    )
    str_1 = module_0.compose(docstring_0, indent=numpydoc_parser_0)
    assert str_1 == "L\no-'x@4aJHl{b7"
    assert module_1.PARAM_KEYWORDS == {
        "parameter",
        "argument",
        "key",
        "keyword",
        "param",
        "arg",
        "attribute",
    }
    assert module_1.RAISES_KEYWORDS == {"raise", "raises", "except", "exception"}
    assert module_1.DEPRECATION_KEYWORDS == {"deprecation", "deprecated"}
    assert module_1.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_1.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_1.EXAMPLES_KEYWORDS == {"example", "examples"}
    numpydoc_parser_0.add_section(docstring_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "L\no-'x@4aJHl{b7"
    docstring_0 = module_1.Docstring()
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description is None
    assert docstring_0.long_description is None
    assert docstring_0.blank_after_short_description is False
    assert docstring_0.blank_after_long_description is False
    assert docstring_0.meta == []
    assert docstring_0.style is None
    assert module_1.PARAM_KEYWORDS == {
        "parameter",
        "argument",
        "key",
        "keyword",
        "param",
        "arg",
        "attribute",
    }
    assert module_1.RAISES_KEYWORDS == {"raise", "raises", "except", "exception"}
    assert module_1.DEPRECATION_KEYWORDS == {"deprecation", "deprecated"}
    assert module_1.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_1.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_1.EXAMPLES_KEYWORDS == {"example", "examples"}
    assert (
        f"{type(module_1.Docstring.description).__module__}.{type(module_1.Docstring.description).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.params).__module__}.{type(module_1.Docstring.params).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.raises).__module__}.{type(module_1.Docstring.raises).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.returns).__module__}.{type(module_1.Docstring.returns).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.many_returns).__module__}.{type(module_1.Docstring.many_returns).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.deprecation).__module__}.{type(module_1.Docstring.deprecation).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.examples).__module__}.{type(module_1.Docstring.examples).__qualname__}"
        == "builtins.property"
    )
    numpydoc_parser_0 = module_0.NumpydocParser()
    assert (
        f"{type(numpydoc_parser_0).__module__}.{type(numpydoc_parser_0).__qualname__}"
        == "numpydoc.NumpydocParser"
    )
    assert (
        f"{type(numpydoc_parser_0.sections).__module__}.{type(numpydoc_parser_0.sections).__qualname__}"
        == "builtins.dict"
    )
    assert len(numpydoc_parser_0.sections) == 31
    assert (
        f"{type(numpydoc_parser_0.titles_re).__module__}.{type(numpydoc_parser_0.titles_re).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.KV_REGEX).__module__}.{type(module_0.KV_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.PARAM_KEY_REGEX).__module__}.{type(module_0.PARAM_KEY_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.PARAM_OPTIONAL_REGEX).__module__}.{type(module_0.PARAM_OPTIONAL_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.PARAM_DEFAULT_REGEX).__module__}.{type(module_0.PARAM_DEFAULT_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.RETURN_KEY_REGEX).__module__}.{type(module_0.RETURN_KEY_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.DEFAULT_SECTIONS).__module__}.{type(module_0.DEFAULT_SECTIONS).__qualname__}"
        == "builtins.list"
    )
    assert len(module_0.DEFAULT_SECTIONS) == 31
    none_type_0 = None
    docstring_1 = numpydoc_parser_0.parse(str_0)
    assert (
        f"{type(docstring_1).__module__}.{type(docstring_1).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_1.short_description == "L"
    assert docstring_1.long_description == "o-'x@4aJHl{b7"
    assert docstring_1.blank_after_short_description is False
    assert docstring_1.blank_after_long_description is False
    assert docstring_1.meta == []
    assert docstring_1.style == module_1.DocstringStyle.NUMPYDOC
    yields_section_0 = module_0.YieldsSection(none_type_0, none_type_0)
    assert (
        f"{type(yields_section_0).__module__}.{type(yields_section_0).__qualname__}"
        == "numpydoc.YieldsSection"
    )
    assert yields_section_0.title is None
    assert yields_section_0.key is None
    assert module_0.YieldsSection.is_generator is True
    str_1 = module_0.compose(docstring_0)
    assert str_1 == ""
    str_2 = "8YFMaw9e.Mg"
    none_type_1 = None
    raises_section_0 = module_0.RaisesSection(str_2, none_type_1)
    assert (
        f"{type(raises_section_0).__module__}.{type(raises_section_0).__qualname__}"
        == "numpydoc.RaisesSection"
    )
    assert raises_section_0.title == "8YFMaw9e.Mg"
    assert raises_section_0.key is None
    str_3 = " "
    docstring_2 = module_0.parse(str_3)
    assert (
        f"{type(docstring_2).__module__}.{type(docstring_2).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_2.short_description is None
    assert docstring_2.long_description is None
    assert docstring_2.blank_after_short_description is False
    assert docstring_2.blank_after_long_description is False
    assert docstring_2.meta == []
    assert docstring_2.style == module_1.DocstringStyle.NUMPYDOC
    str_4 = "&*f~u0"
    section_0 = module_0.Section(str_4, raises_section_0)
    assert (
        f"{type(section_0).__module__}.{type(section_0).__qualname__}"
        == "numpydoc.Section"
    )
    assert section_0.title == "&*f~u0"
    assert (
        f"{type(section_0.key).__module__}.{type(section_0.key).__qualname__}"
        == "numpydoc.RaisesSection"
    )
    assert (
        f"{type(module_0.Section.title_pattern).__module__}.{type(module_0.Section.title_pattern).__qualname__}"
        == "builtins.property"
    )
    section_0.pop(docstring_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = "L\no-x4a JHl{b7"
    docstring_0 = module_1.Docstring()
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description is None
    assert docstring_0.long_description is None
    assert docstring_0.blank_after_short_description is False
    assert docstring_0.blank_after_long_description is False
    assert docstring_0.meta == []
    assert docstring_0.style is None
    assert module_1.PARAM_KEYWORDS == {
        "parameter",
        "argument",
        "key",
        "keyword",
        "param",
        "arg",
        "attribute",
    }
    assert module_1.RAISES_KEYWORDS == {"raise", "raises", "except", "exception"}
    assert module_1.DEPRECATION_KEYWORDS == {"deprecation", "deprecated"}
    assert module_1.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_1.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_1.EXAMPLES_KEYWORDS == {"example", "examples"}
    assert (
        f"{type(module_1.Docstring.description).__module__}.{type(module_1.Docstring.description).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.params).__module__}.{type(module_1.Docstring.params).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.raises).__module__}.{type(module_1.Docstring.raises).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.returns).__module__}.{type(module_1.Docstring.returns).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.many_returns).__module__}.{type(module_1.Docstring.many_returns).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.deprecation).__module__}.{type(module_1.Docstring.deprecation).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_1.Docstring.examples).__module__}.{type(module_1.Docstring.examples).__qualname__}"
        == "builtins.property"
    )
    numpydoc_parser_0 = module_0.NumpydocParser()
    assert (
        f"{type(numpydoc_parser_0).__module__}.{type(numpydoc_parser_0).__qualname__}"
        == "numpydoc.NumpydocParser"
    )
    assert (
        f"{type(numpydoc_parser_0.sections).__module__}.{type(numpydoc_parser_0.sections).__qualname__}"
        == "builtins.dict"
    )
    assert len(numpydoc_parser_0.sections) == 31
    assert (
        f"{type(numpydoc_parser_0.titles_re).__module__}.{type(numpydoc_parser_0.titles_re).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.KV_REGEX).__module__}.{type(module_0.KV_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.PARAM_KEY_REGEX).__module__}.{type(module_0.PARAM_KEY_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.PARAM_OPTIONAL_REGEX).__module__}.{type(module_0.PARAM_OPTIONAL_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.PARAM_DEFAULT_REGEX).__module__}.{type(module_0.PARAM_DEFAULT_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.RETURN_KEY_REGEX).__module__}.{type(module_0.RETURN_KEY_REGEX).__qualname__}"
        == "re.Pattern"
    )
    assert (
        f"{type(module_0.DEFAULT_SECTIONS).__module__}.{type(module_0.DEFAULT_SECTIONS).__qualname__}"
        == "builtins.list"
    )
    assert len(module_0.DEFAULT_SECTIONS) == 31
    none_type_0 = None
    docstring_1 = numpydoc_parser_0.parse(str_0)
    assert (
        f"{type(docstring_1).__module__}.{type(docstring_1).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_1.short_description == "L"
    assert docstring_1.long_description == "o-x4a JHl{b7"
    assert docstring_1.blank_after_short_description is False
    assert docstring_1.blank_after_long_description is False
    assert docstring_1.meta == []
    assert docstring_1.style == module_1.DocstringStyle.NUMPYDOC
    section_0 = module_0.Section(none_type_0, docstring_1)
    assert (
        f"{type(section_0).__module__}.{type(section_0).__qualname__}"
        == "numpydoc.Section"
    )
    assert section_0.title is None
    assert (
        f"{type(section_0.key).__module__}.{type(section_0.key).__qualname__}"
        == "common.Docstring"
    )
    assert (
        f"{type(module_0.Section.title_pattern).__module__}.{type(module_0.Section.title_pattern).__qualname__}"
        == "builtins.property"
    )
    str_1 = module_0.compose(docstring_0)
    assert str_1 == ""
    str_2 = "eo\n\n#"
    docstring_2 = module_0.parse(str_2)
    assert (
        f"{type(docstring_2).__module__}.{type(docstring_2).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_2.short_description == "eo"
    assert docstring_2.long_description == "#"
    assert docstring_2.blank_after_short_description is True
    assert docstring_2.blank_after_long_description is False
    assert docstring_2.meta == []
    assert docstring_2.style == module_1.DocstringStyle.NUMPYDOC
    var_0 = module_4.iter_child_nodes(str_0)
    assert module_4.PyCF_ALLOW_TOP_LEVEL_AWAIT == 8192
    assert module_4.PyCF_ONLY_AST == 1024
    assert module_4.PyCF_TYPE_COMMENTS == 4096
    str_3 = module_0.compose(docstring_2, var_0)
    assert str_3 == "eo\n\n#"
    str_4 = 'AKil"@K9R!'
    str_5 = "rX9[%?&+T2~r?MI"
    docstring_3 = module_0.parse(str_5)
    assert (
        f"{type(docstring_3).__module__}.{type(docstring_3).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_3.short_description == "rX9[%?&+T2~r?MI"
    assert docstring_3.long_description is None
    assert docstring_3.blank_after_short_description is False
    assert docstring_3.blank_after_long_description is False
    assert docstring_3.meta == []
    assert docstring_3.style == module_1.DocstringStyle.NUMPYDOC
    section_1 = module_0.Section(str_4, str_3)
    assert (
        f"{type(section_1).__module__}.{type(section_1).__qualname__}"
        == "numpydoc.Section"
    )
    assert section_1.title == 'AKil"@K9R!'
    assert section_1.key == "eo\n\n#"
    module_2.getargspec(var_0)
