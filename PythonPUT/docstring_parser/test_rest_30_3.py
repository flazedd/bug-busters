# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import rest as module_0
import common as module_1
import ast as module_2


def test_case_0():
    str_0 = "R$8:6|t5"
    docstring_0 = module_0.parse(str_0)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description == "R$8:6|t5"
    assert docstring_0.long_description is None
    assert docstring_0.blank_after_short_description is False
    assert docstring_0.blank_after_long_description is False
    assert docstring_0.meta == []
    assert docstring_0.style == module_1.DocstringStyle.REST
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.PARAM_KEYWORDS == {
        "keyword",
        "argument",
        "attribute",
        "param",
        "arg",
        "key",
        "parameter",
    }
    assert module_0.RAISES_KEYWORDS == {"except", "raise", "exception", "raises"}
    assert module_0.RETURNS_KEYWORDS == {"returns", "return"}
    assert module_0.YIELDS_KEYWORDS == {"yield", "yields"}
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


def test_case_1():
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
    assert docstring_0.style == module_1.DocstringStyle.REST
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.PARAM_KEYWORDS == {
        "keyword",
        "argument",
        "attribute",
        "param",
        "arg",
        "key",
        "parameter",
    }
    assert module_0.RAISES_KEYWORDS == {"except", "raise", "exception", "raises"}
    assert module_0.RETURNS_KEYWORDS == {"returns", "return"}
    assert module_0.YIELDS_KEYWORDS == {"yield", "yields"}
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
    str_0 = "{0"
    docstring_0 = module_0.parse(str_0)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description == "{0"
    assert docstring_0.long_description is None
    assert docstring_0.blank_after_short_description is False
    assert docstring_0.blank_after_long_description is False
    assert docstring_0.meta == []
    assert docstring_0.style == module_1.DocstringStyle.REST
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.PARAM_KEYWORDS == {
        "keyword",
        "argument",
        "attribute",
        "param",
        "arg",
        "key",
        "parameter",
    }
    assert module_0.RAISES_KEYWORDS == {"except", "raise", "exception", "raises"}
    assert module_0.RETURNS_KEYWORDS == {"returns", "return"}
    assert module_0.YIELDS_KEYWORDS == {"yield", "yields"}
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
    str_1 = module_0.compose(docstring_0, str_0)
    assert str_1 == "{0"
    assert module_1.PARAM_KEYWORDS == {
        "keyword",
        "argument",
        "attribute",
        "param",
        "arg",
        "key",
        "parameter",
    }
    assert module_1.RAISES_KEYWORDS == {"except", "raise", "exception", "raises"}
    assert module_1.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_1.RETURNS_KEYWORDS == {"returns", "return"}
    assert module_1.YIELDS_KEYWORDS == {"yield", "yields"}
    assert module_1.EXAMPLES_KEYWORDS == {"example", "examples"}
    str_2 = "E>1IA%X\ncbo"
    docstring_1 = module_0.parse(str_2)
    assert (
        f"{type(docstring_1).__module__}.{type(docstring_1).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_1.short_description == "E>1IA%X"
    assert docstring_1.long_description == "cbo"
    assert docstring_1.blank_after_short_description is False
    assert docstring_1.blank_after_long_description is False
    assert docstring_1.meta == []
    assert docstring_1.style == module_1.DocstringStyle.REST


def test_case_3():
    none_type_0 = None
    str_0 = "O|#z4Xi*1RZZ"
    docstring_0 = module_0.parse(str_0)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description == "O|#z4Xi*1RZZ"
    assert docstring_0.long_description is None
    assert docstring_0.blank_after_short_description is False
    assert docstring_0.blank_after_long_description is False
    assert docstring_0.meta == []
    assert docstring_0.style == module_1.DocstringStyle.REST
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.PARAM_KEYWORDS == {
        "keyword",
        "argument",
        "attribute",
        "param",
        "arg",
        "key",
        "parameter",
    }
    assert module_0.RAISES_KEYWORDS == {"except", "raise", "exception", "raises"}
    assert module_0.RETURNS_KEYWORDS == {"returns", "return"}
    assert module_0.YIELDS_KEYWORDS == {"yield", "yields"}
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
    docstring_1 = module_1.Docstring()
    assert (
        f"{type(docstring_1).__module__}.{type(docstring_1).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_1.short_description is None
    assert docstring_1.long_description is None
    assert docstring_1.blank_after_short_description is False
    assert docstring_1.blank_after_long_description is False
    assert docstring_1.meta == []
    assert docstring_1.style is None
    assert module_1.PARAM_KEYWORDS == {
        "keyword",
        "argument",
        "attribute",
        "param",
        "arg",
        "key",
        "parameter",
    }
    assert module_1.RAISES_KEYWORDS == {"except", "raise", "exception", "raises"}
    assert module_1.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_1.RETURNS_KEYWORDS == {"returns", "return"}
    assert module_1.YIELDS_KEYWORDS == {"yield", "yields"}
    assert module_1.EXAMPLES_KEYWORDS == {"example", "examples"}
    docstring_2 = module_0.parse(str_0)
    assert (
        f"{type(docstring_2).__module__}.{type(docstring_2).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_2.short_description == "O|#z4Xi*1RZZ"
    assert docstring_2.long_description is None
    assert docstring_2.blank_after_short_description is False
    assert docstring_2.blank_after_long_description is False
    assert docstring_2.meta == []
    assert docstring_2.style == module_1.DocstringStyle.REST
    str_1 = "x(on24!05lH*p0cd"
    str_2 = module_0.compose(docstring_1, indent=str_1)
    assert str_2 == ""
    docstring_3 = module_0.parse(none_type_0)
    assert (
        f"{type(docstring_3).__module__}.{type(docstring_3).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_3.short_description is None
    assert docstring_3.long_description is None
    assert docstring_3.blank_after_short_description is False
    assert docstring_3.blank_after_long_description is False
    assert docstring_3.meta == []
    assert docstring_3.style == module_1.DocstringStyle.REST
    with pytest.raises(TypeError):
        module_2.get_docstring(docstring_1)


def test_case_4():
    str_0 = " R);L C#,2]\nZ16"
    docstring_0 = module_0.parse(str_0)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description == "R);L C#,2]"
    assert docstring_0.long_description == "Z16"
    assert docstring_0.blank_after_short_description is False
    assert docstring_0.blank_after_long_description is False
    assert docstring_0.meta == []
    assert docstring_0.style == module_1.DocstringStyle.REST
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.PARAM_KEYWORDS == {
        "keyword",
        "argument",
        "attribute",
        "param",
        "arg",
        "key",
        "parameter",
    }
    assert module_0.RAISES_KEYWORDS == {"except", "raise", "exception", "raises"}
    assert module_0.RETURNS_KEYWORDS == {"returns", "return"}
    assert module_0.YIELDS_KEYWORDS == {"yield", "yields"}
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
    str_1 = module_0.compose(docstring_0, indent=str_0)
    assert str_1 == "R);L C#,2]\nZ16"
    assert module_1.PARAM_KEYWORDS == {
        "keyword",
        "argument",
        "attribute",
        "param",
        "arg",
        "key",
        "parameter",
    }
    assert module_1.RAISES_KEYWORDS == {"except", "raise", "exception", "raises"}
    assert module_1.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_1.RETURNS_KEYWORDS == {"returns", "return"}
    assert module_1.YIELDS_KEYWORDS == {"yield", "yields"}
    assert module_1.EXAMPLES_KEYWORDS == {"example", "examples"}
    str_2 = ":CcfJtkX\n."
    with pytest.raises(module_1.ParseError):
        module_0.parse(str_2)


def test_case_5():
    str_0 = "E>1IA%X\ncbo"
    docstring_0 = module_0.parse(str_0)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description == "E>1IA%X"
    assert docstring_0.long_description == "cbo"
    assert docstring_0.blank_after_short_description is False
    assert docstring_0.blank_after_long_description is False
    assert docstring_0.meta == []
    assert docstring_0.style == module_1.DocstringStyle.REST
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.PARAM_KEYWORDS == {
        "keyword",
        "argument",
        "attribute",
        "param",
        "arg",
        "key",
        "parameter",
    }
    assert module_0.RAISES_KEYWORDS == {"except", "raise", "exception", "raises"}
    assert module_0.RETURNS_KEYWORDS == {"returns", "return"}
    assert module_0.YIELDS_KEYWORDS == {"yield", "yields"}
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
def test_case_6():
    str_0 = ".\x0b68Ma>9"
    docstring_0 = module_0.parse(str_0)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description == ".\x0b68Ma>9"
    assert docstring_0.long_description is None
    assert docstring_0.blank_after_short_description is False
    assert docstring_0.blank_after_long_description is False
    assert docstring_0.meta == []
    assert docstring_0.style == module_1.DocstringStyle.REST
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.PARAM_KEYWORDS == {
        "keyword",
        "argument",
        "attribute",
        "param",
        "arg",
        "key",
        "parameter",
    }
    assert module_0.RAISES_KEYWORDS == {"except", "raise", "exception", "raises"}
    assert module_0.RETURNS_KEYWORDS == {"returns", "return"}
    assert module_0.YIELDS_KEYWORDS == {"yield", "yields"}
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
    assert docstring_1.short_description == ".\x0b68Ma>9"
    assert docstring_1.long_description is None
    assert docstring_1.blank_after_short_description is False
    assert docstring_1.blank_after_long_description is False
    assert docstring_1.meta == []
    assert docstring_1.style == module_1.DocstringStyle.REST
    assert module_1.PARAM_KEYWORDS == {
        "keyword",
        "argument",
        "attribute",
        "param",
        "arg",
        "key",
        "parameter",
    }
    assert module_1.RAISES_KEYWORDS == {"except", "raise", "exception", "raises"}
    assert module_1.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_1.RETURNS_KEYWORDS == {"returns", "return"}
    assert module_1.YIELDS_KEYWORDS == {"yield", "yields"}
    assert module_1.EXAMPLES_KEYWORDS == {"example", "examples"}
    str_1 = "]Lt|kcp<yU>PhFt\x0c6U\n\r"
    docstring_2 = module_0.parse(str_1)
    assert (
        f"{type(docstring_2).__module__}.{type(docstring_2).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_2.short_description == "]Lt|kcp<yU>PhFt\x0c6U"
    assert docstring_2.long_description is None
    assert docstring_2.blank_after_short_description is False
    assert docstring_2.blank_after_long_description is False
    assert docstring_2.meta == []
    assert docstring_2.style == module_1.DocstringStyle.REST
    str_2 = "@E\n\x0c9C"
    docstring_3 = module_0.parse(str_2)
    assert (
        f"{type(docstring_3).__module__}.{type(docstring_3).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_3.short_description == "@E"
    assert docstring_3.long_description == "9C"
    assert docstring_3.blank_after_short_description is False
    assert docstring_3.blank_after_long_description is False
    assert docstring_3.meta == []
    assert docstring_3.style == module_1.DocstringStyle.REST
    module_0.compose(str_2, indent=str_0)
