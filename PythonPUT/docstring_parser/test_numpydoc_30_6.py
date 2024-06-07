# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import numpydoc as module_0
import common as module_1
import ast as module_2


def test_case_0():
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


def test_case_1():
    str_0 = "Sl%\\\\eFWj|S"
    docstring_0 = module_0.parse(str_0)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description == "Sl%\\\\eFWj|S"
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


def test_case_2():
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


def test_case_3():
    str_0 = "8\nZ+F<;|yvxaQdVQa"
    docstring_0 = module_0.parse(str_0)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description == "8"
    assert docstring_0.long_description == "Z+F<;|yvxaQdVQa"
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
    docstring_1 = module_0.parse(str_0)
    assert (
        f"{type(docstring_1).__module__}.{type(docstring_1).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_1.short_description == "8"
    assert docstring_1.long_description == "Z+F<;|yvxaQdVQa"
    assert docstring_1.blank_after_short_description is False
    assert docstring_1.blank_after_long_description is False
    assert docstring_1.meta == []
    assert docstring_1.style == module_1.DocstringStyle.NUMPYDOC
    assert module_1.PARAM_KEYWORDS == {
        "attribute",
        "key",
        "keyword",
        "argument",
        "param",
        "arg",
        "parameter",
    }
    assert module_1.RAISES_KEYWORDS == {"raise", "except", "exception", "raises"}
    assert module_1.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_1.RETURNS_KEYWORDS == {"returns", "return"}
    assert module_1.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_1.EXAMPLES_KEYWORDS == {"example", "examples"}
    str_1 = "^]M\n>ohRHK%Kc"
    k_v_section_0 = module_0._KVSection(str_0, str_1)
    assert (
        f"{type(k_v_section_0).__module__}.{type(k_v_section_0).__qualname__}"
        == "numpydoc._KVSection"
    )
    assert k_v_section_0.title == "8\nZ+F<;|yvxaQdVQa"
    assert k_v_section_0.key == "^]M\n>ohRHK%Kc"
    str_2 = "\x0b"
    str_3 = "e&U<]U}#\x0c:7Paw_|P9])"
    str_4 = "t?M|&yN\rx\\\nfc#b%I:"
    k_v_section_1 = module_0._KVSection(str_3, str_4)
    assert (
        f"{type(k_v_section_1).__module__}.{type(k_v_section_1).__qualname__}"
        == "numpydoc._KVSection"
    )
    assert k_v_section_1.title == "e&U<]U}#\x0c:7Paw_|P9])"
    assert k_v_section_1.key == "t?M|&yN\rx\\\nfc#b%I:"
    docstring_2 = module_0.parse(str_2)
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


def test_case_4():
    str_0 = "8\nZ+F<;|yvxaQdVQa"
    docstring_0 = module_0.parse(str_0)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description == "8"
    assert docstring_0.long_description == "Z+F<;|yvxaQdVQa"
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


def test_case_5():
    str_0 = "y"
    docstring_0 = module_0.parse(str_0)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description == "y"
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
    str_1 = module_0.compose(docstring_0)
    assert str_1 == "y"
    assert module_1.PARAM_KEYWORDS == {
        "attribute",
        "key",
        "keyword",
        "argument",
        "param",
        "arg",
        "parameter",
    }
    assert module_1.RAISES_KEYWORDS == {"raise", "except", "exception", "raises"}
    assert module_1.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_1.RETURNS_KEYWORDS == {"returns", "return"}
    assert module_1.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_1.EXAMPLES_KEYWORDS == {"example", "examples"}
    str_2 = "4`(Nt~\n?"
    docstring_1 = module_0.parse(str_2)
    assert (
        f"{type(docstring_1).__module__}.{type(docstring_1).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_1.short_description == "4`(Nt~"
    assert docstring_1.long_description == "?"
    assert docstring_1.blank_after_short_description is False
    assert docstring_1.blank_after_long_description is False
    assert docstring_1.meta == []
    assert docstring_1.style == module_1.DocstringStyle.NUMPYDOC


def test_case_6():
    str_0 = ""
    docstring_0 = module_0.parse(str_0)
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
    str_1 = module_0.compose(docstring_0)
    assert str_1 == ""
    assert module_1.PARAM_KEYWORDS == {
        "attribute",
        "key",
        "keyword",
        "argument",
        "param",
        "arg",
        "parameter",
    }
    assert module_1.RAISES_KEYWORDS == {"raise", "except", "exception", "raises"}
    assert module_1.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_1.RETURNS_KEYWORDS == {"returns", "return"}
    assert module_1.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_1.EXAMPLES_KEYWORDS == {"example", "examples"}
    str_2 = "<(o3+wl]^p=\x0c"
    section_0 = module_0.Section(str_1, str_2)
    assert (
        f"{type(section_0).__module__}.{type(section_0).__qualname__}"
        == "numpydoc.Section"
    )
    assert section_0.title == ""
    assert section_0.key == "<(o3+wl]^p=\x0c"
    assert (
        f"{type(module_0.Section.title_pattern).__module__}.{type(module_0.Section.title_pattern).__qualname__}"
        == "builtins.property"
    )
    str_3 = "4`O(Nt~\nZ."
    docstring_1 = module_0.parse(str_3)
    assert (
        f"{type(docstring_1).__module__}.{type(docstring_1).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_1.short_description == "4`O(Nt~"
    assert docstring_1.long_description == "Z."
    assert docstring_1.blank_after_short_description is False
    assert docstring_1.blank_after_long_description is False
    assert docstring_1.meta == []
    assert docstring_1.style == module_1.DocstringStyle.NUMPYDOC
    docstring_2 = module_0.parse(str_0)
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


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "%OLa]!V\t"
    module_0.NumpydocParser(str_0)


def test_case_8():
    str_0 = "Yy2VeU)7|"
    none_type_0 = None
    str_1 = "^]M\n>ohRHK%Kc"
    docstring_0 = module_0.parse(str_1)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description == "^]M"
    assert docstring_0.long_description == ">ohRHK%Kc"
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
    str_2 = module_0.compose(docstring_0, indent=none_type_0)
    assert str_2 == "^]M\n>ohRHK%Kc"
    assert module_1.PARAM_KEYWORDS == {
        "attribute",
        "key",
        "keyword",
        "argument",
        "param",
        "arg",
        "parameter",
    }
    assert module_1.RAISES_KEYWORDS == {"raise", "except", "exception", "raises"}
    assert module_1.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_1.RETURNS_KEYWORDS == {"returns", "return"}
    assert module_1.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_1.EXAMPLES_KEYWORDS == {"example", "examples"}
    section_0 = module_0.Section(str_2, none_type_0)
    assert (
        f"{type(section_0).__module__}.{type(section_0).__qualname__}"
        == "numpydoc.Section"
    )
    assert section_0.title == "^]M\n>ohRHK%Kc"
    assert section_0.key is None
    assert (
        f"{type(module_0.Section.title_pattern).__module__}.{type(module_0.Section.title_pattern).__qualname__}"
        == "builtins.property"
    )
    with pytest.raises(TypeError):
        module_2.dump(str_0, docstring_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
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