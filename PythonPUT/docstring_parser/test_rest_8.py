# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import rest as module_0
import common as module_1


def test_case_0():
    str_0 = "#[ FY"
    docstring_0 = module_0.parse(str_0)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description == "#[ FY"
    assert docstring_0.long_description is None
    assert docstring_0.blank_after_short_description is False
    assert docstring_0.blank_after_long_description is False
    assert docstring_0.meta == []
    assert docstring_0.style == module_1.DocstringStyle.REST
    assert module_0.DEPRECATION_KEYWORDS == {"deprecation", "deprecated"}
    assert module_0.PARAM_KEYWORDS == {
        "arg",
        "param",
        "key",
        "keyword",
        "parameter",
        "argument",
        "attribute",
    }
    assert module_0.RAISES_KEYWORDS == {"raises", "except", "raise", "exception"}
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
    assert docstring_0.style == module_1.DocstringStyle.REST
    assert module_0.DEPRECATION_KEYWORDS == {"deprecation", "deprecated"}
    assert module_0.PARAM_KEYWORDS == {
        "arg",
        "param",
        "key",
        "keyword",
        "parameter",
        "argument",
        "attribute",
    }
    assert module_0.RAISES_KEYWORDS == {"raises", "except", "raise", "exception"}
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
    str_0 = "53jW;<#f~\x0cr\\}{u"
    docstring_0 = module_0.parse(str_0)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description == "53jW;<#f~\x0cr\\}{u"
    assert docstring_0.long_description is None
    assert docstring_0.blank_after_short_description is False
    assert docstring_0.blank_after_long_description is False
    assert docstring_0.meta == []
    assert docstring_0.style == module_1.DocstringStyle.REST
    assert module_0.DEPRECATION_KEYWORDS == {"deprecation", "deprecated"}
    assert module_0.PARAM_KEYWORDS == {
        "arg",
        "param",
        "key",
        "keyword",
        "parameter",
        "argument",
        "attribute",
    }
    assert module_0.RAISES_KEYWORDS == {"raises", "except", "raise", "exception"}
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
    str_1 = module_0.compose(docstring_0)
    assert str_1 == "53jW;<#f~\x0cr\\}{u"
    assert module_1.PARAM_KEYWORDS == {
        "arg",
        "param",
        "key",
        "keyword",
        "parameter",
        "argument",
        "attribute",
    }
    assert module_1.RAISES_KEYWORDS == {"raises", "except", "raise", "exception"}
    assert module_1.DEPRECATION_KEYWORDS == {"deprecation", "deprecated"}
    assert module_1.RETURNS_KEYWORDS == {"returns", "return"}
    assert module_1.YIELDS_KEYWORDS == {"yield", "yields"}
    assert module_1.EXAMPLES_KEYWORDS == {"examples", "example"}


def test_case_3():
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
    assert docstring_0.style == module_1.DocstringStyle.REST
    assert module_0.DEPRECATION_KEYWORDS == {"deprecation", "deprecated"}
    assert module_0.PARAM_KEYWORDS == {
        "arg",
        "param",
        "key",
        "keyword",
        "parameter",
        "argument",
        "attribute",
    }
    assert module_0.RAISES_KEYWORDS == {"raises", "except", "raise", "exception"}
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
    str_0 = module_0.compose(docstring_0, docstring_0)
    assert str_0 == ""
    assert module_1.PARAM_KEYWORDS == {
        "arg",
        "param",
        "key",
        "keyword",
        "parameter",
        "argument",
        "attribute",
    }
    assert module_1.RAISES_KEYWORDS == {"raises", "except", "raise", "exception"}
    assert module_1.DEPRECATION_KEYWORDS == {"deprecation", "deprecated"}
    assert module_1.RETURNS_KEYWORDS == {"returns", "return"}
    assert module_1.YIELDS_KEYWORDS == {"yield", "yields"}
    assert module_1.EXAMPLES_KEYWORDS == {"examples", "example"}


def test_case_4():
    str_0 = ">4GbQB2+jG}S-\n1"
    docstring_0 = module_0.parse(str_0)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description == ">4GbQB2+jG}S-"
    assert docstring_0.long_description == "1"
    assert docstring_0.blank_after_short_description is False
    assert docstring_0.blank_after_long_description is False
    assert docstring_0.meta == []
    assert docstring_0.style == module_1.DocstringStyle.REST
    assert module_0.DEPRECATION_KEYWORDS == {"deprecation", "deprecated"}
    assert module_0.PARAM_KEYWORDS == {
        "arg",
        "param",
        "key",
        "keyword",
        "parameter",
        "argument",
        "attribute",
    }
    assert module_0.RAISES_KEYWORDS == {"raises", "except", "raise", "exception"}
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
    str_1 = module_0.compose(docstring_0)
    assert str_1 == ">4GbQB2+jG}S-\n1"
    assert module_1.PARAM_KEYWORDS == {
        "arg",
        "param",
        "key",
        "keyword",
        "parameter",
        "argument",
        "attribute",
    }
    assert module_1.RAISES_KEYWORDS == {"raises", "except", "raise", "exception"}
    assert module_1.DEPRECATION_KEYWORDS == {"deprecation", "deprecated"}
    assert module_1.RETURNS_KEYWORDS == {"returns", "return"}
    assert module_1.YIELDS_KEYWORDS == {"yield", "yields"}
    assert module_1.EXAMPLES_KEYWORDS == {"examples", "example"}
    docstring_1 = module_0.parse(str_0)
    assert (
        f"{type(docstring_1).__module__}.{type(docstring_1).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_1.short_description == ">4GbQB2+jG}S-"
    assert docstring_1.long_description == "1"
    assert docstring_1.blank_after_short_description is False
    assert docstring_1.blank_after_long_description is False
    assert docstring_1.meta == []
    assert docstring_1.style == module_1.DocstringStyle.REST


def test_case_5():
    str_0 = ":dnQE"
    with pytest.raises(module_1.ParseError):
        module_0.parse(str_0)
