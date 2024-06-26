# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import epydoc as module_0
import common as module_1


def test_case_0():
    str_0 = ")OO"
    docstring_0 = module_0.parse(str_0)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description == ")OO"
    assert docstring_0.long_description is None
    assert docstring_0.blank_after_short_description is False
    assert docstring_0.blank_after_long_description is False
    assert docstring_0.meta == []
    assert docstring_0.style == module_1.DocstringStyle.EPYDOC
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
    assert docstring_0.style == module_1.DocstringStyle.EPYDOC
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
    assert docstring_0.style == module_1.DocstringStyle.EPYDOC
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
    assert module_1.PARAM_KEYWORDS == {
        "parameter",
        "keyword",
        "key",
        "argument",
        "param",
        "attribute",
        "arg",
    }
    assert module_1.RAISES_KEYWORDS == {"except", "exception", "raise", "raises"}
    assert module_1.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_1.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_1.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_1.EXAMPLES_KEYWORDS == {"example", "examples"}


def test_case_3():
    str_0 = ")OO"
    docstring_0 = module_0.parse(str_0)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description == ")OO"
    assert docstring_0.long_description is None
    assert docstring_0.blank_after_short_description is False
    assert docstring_0.blank_after_long_description is False
    assert docstring_0.meta == []
    assert docstring_0.style == module_1.DocstringStyle.EPYDOC
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
    assert str_1 == ")OO"
    assert module_1.PARAM_KEYWORDS == {
        "parameter",
        "keyword",
        "key",
        "argument",
        "param",
        "attribute",
        "arg",
    }
    assert module_1.RAISES_KEYWORDS == {"except", "exception", "raise", "raises"}
    assert module_1.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_1.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_1.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_1.EXAMPLES_KEYWORDS == {"example", "examples"}


def test_case_4():
    str_0 = "\\"
    str_1 = ""
    docstring_0 = module_0.parse(str_1)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description is None
    assert docstring_0.long_description is None
    assert docstring_0.blank_after_short_description is False
    assert docstring_0.blank_after_long_description is False
    assert docstring_0.meta == []
    assert docstring_0.style == module_1.DocstringStyle.EPYDOC
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
    assert docstring_1.short_description == "\\"
    assert docstring_1.long_description is None
    assert docstring_1.blank_after_short_description is False
    assert docstring_1.blank_after_long_description is False
    assert docstring_1.meta == []
    assert docstring_1.style == module_1.DocstringStyle.EPYDOC
    assert module_1.PARAM_KEYWORDS == {
        "parameter",
        "keyword",
        "key",
        "argument",
        "param",
        "attribute",
        "arg",
    }
    assert module_1.RAISES_KEYWORDS == {"except", "exception", "raise", "raises"}
    assert module_1.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_1.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_1.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_1.EXAMPLES_KEYWORDS == {"example", "examples"}
    str_2 = "Gj\nY`[/zkaR5ByAPN"
    docstring_2 = module_0.parse(str_2)
    assert (
        f"{type(docstring_2).__module__}.{type(docstring_2).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_2.short_description == "Gj"
    assert docstring_2.long_description == "Y`[/zkaR5ByAPN"
    assert docstring_2.blank_after_short_description is False
    assert docstring_2.blank_after_long_description is False
    assert docstring_2.meta == []
    assert docstring_2.style == module_1.DocstringStyle.EPYDOC


def test_case_5():
    str_0 = "@y)E"
    with pytest.raises(module_1.ParseError):
        module_0.parse(str_0)


def test_case_6():
    str_0 = "OuS/rzrx'0Ptc.C@3X9"
    docstring_0 = module_0.parse(str_0)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description == "OuS/rzrx'0Ptc.C@3X9"
    assert docstring_0.long_description is None
    assert docstring_0.blank_after_short_description is False
    assert docstring_0.blank_after_long_description is False
    assert docstring_0.meta == []
    assert docstring_0.style == module_1.DocstringStyle.EPYDOC
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
    str_1 = '!Lz?"@_]SN9&ocPu\n@]d'
    with pytest.raises(module_1.ParseError):
        module_0.parse(str_1)


def test_case_7():
    str_0 = "/:\n "
    docstring_0 = module_0.parse(str_0)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description == "/:"
    assert docstring_0.long_description is None
    assert docstring_0.blank_after_short_description is False
    assert docstring_0.blank_after_long_description is False
    assert docstring_0.meta == []
    assert docstring_0.style == module_1.DocstringStyle.EPYDOC
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
    str_1 = "@s"
    with pytest.raises(module_1.ParseError):
        module_0.parse(str_1)


def test_case_8():
    str_0 = "^m)j\n42HxC}Dp\\&"
    docstring_0 = module_0.parse(str_0)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description == "^m)j"
    assert docstring_0.long_description == "42HxC}Dp\\&"
    assert docstring_0.blank_after_short_description is False
    assert docstring_0.blank_after_long_description is False
    assert docstring_0.meta == []
    assert docstring_0.style == module_1.DocstringStyle.EPYDOC
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
    assert str_1 == "^m)j\n42HxC}Dp\\&"
    assert module_1.PARAM_KEYWORDS == {
        "parameter",
        "keyword",
        "key",
        "argument",
        "param",
        "attribute",
        "arg",
    }
    assert module_1.RAISES_KEYWORDS == {"except", "exception", "raise", "raises"}
    assert module_1.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_1.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_1.YIELDS_KEYWORDS == {"yields", "yield"}
    assert module_1.EXAMPLES_KEYWORDS == {"example", "examples"}
    str_2 = module_0.compose(docstring_0)
    assert str_2 == "^m)j\n42HxC}Dp\\&"
    str_3 = "@"
    with pytest.raises(module_1.ParseError):
        module_0.parse(str_3)
