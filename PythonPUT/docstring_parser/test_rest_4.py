# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import rest as module_0
import common as module_1
import ast as module_2


def test_case_0():
    str_0 = "{T{u~ a\\"
    docstring_0 = module_0.parse(str_0)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description == "{T{u~ a\\"
    assert docstring_0.long_description is None
    assert docstring_0.blank_after_short_description is False
    assert docstring_0.blank_after_long_description is False
    assert docstring_0.meta == []
    assert docstring_0.style == module_1.DocstringStyle.REST
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.PARAM_KEYWORDS == {
        "argument",
        "key",
        "parameter",
        "param",
        "attribute",
        "arg",
        "keyword",
    }
    assert module_0.RAISES_KEYWORDS == {"raise", "except", "raises", "exception"}
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
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.PARAM_KEYWORDS == {
        "argument",
        "key",
        "parameter",
        "param",
        "attribute",
        "arg",
        "keyword",
    }
    assert module_0.RAISES_KEYWORDS == {"raise", "except", "raises", "exception"}
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
    str_0 = "J?v|b"
    docstring_0 = module_0.parse(str_0)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description == "J?v|b"
    assert docstring_0.long_description is None
    assert docstring_0.blank_after_short_description is False
    assert docstring_0.blank_after_long_description is False
    assert docstring_0.meta == []
    assert docstring_0.style == module_1.DocstringStyle.REST
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.PARAM_KEYWORDS == {
        "argument",
        "key",
        "parameter",
        "param",
        "attribute",
        "arg",
        "keyword",
    }
    assert module_0.RAISES_KEYWORDS == {"raise", "except", "raises", "exception"}
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
    assert str_1 == "J?v|b"
    assert module_1.PARAM_KEYWORDS == {
        "argument",
        "key",
        "parameter",
        "param",
        "attribute",
        "arg",
        "keyword",
    }
    assert module_1.RAISES_KEYWORDS == {"raise", "except", "raises", "exception"}
    assert module_1.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_1.RETURNS_KEYWORDS == {"returns", "return"}
    assert module_1.YIELDS_KEYWORDS == {"yield", "yields"}
    assert module_1.EXAMPLES_KEYWORDS == {"example", "examples"}


@pytest.mark.xfail(strict=True)
def test_case_3():
    none_type_0 = None
    str_0 = "U~#evB~iQb!@]LaJ"
    docstring_0 = module_0.parse(str_0)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description == "U~#evB~iQb!@]LaJ"
    assert docstring_0.long_description is None
    assert docstring_0.blank_after_short_description is False
    assert docstring_0.blank_after_long_description is False
    assert docstring_0.meta == []
    assert docstring_0.style == module_1.DocstringStyle.REST
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.PARAM_KEYWORDS == {
        "argument",
        "key",
        "parameter",
        "param",
        "attribute",
        "arg",
        "keyword",
    }
    assert module_0.RAISES_KEYWORDS == {"raise", "except", "raises", "exception"}
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
    str_1 = "*BHVw_"
    docstring_1 = module_0.parse(str_0)
    assert (
        f"{type(docstring_1).__module__}.{type(docstring_1).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_1.short_description == "U~#evB~iQb!@]LaJ"
    assert docstring_1.long_description is None
    assert docstring_1.blank_after_short_description is False
    assert docstring_1.blank_after_long_description is False
    assert docstring_1.meta == []
    assert docstring_1.style == module_1.DocstringStyle.REST
    assert module_1.PARAM_KEYWORDS == {
        "argument",
        "key",
        "parameter",
        "param",
        "attribute",
        "arg",
        "keyword",
    }
    assert module_1.RAISES_KEYWORDS == {"raise", "except", "raises", "exception"}
    assert module_1.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_1.RETURNS_KEYWORDS == {"returns", "return"}
    assert module_1.YIELDS_KEYWORDS == {"yield", "yields"}
    assert module_1.EXAMPLES_KEYWORDS == {"example", "examples"}
    docstring_2 = module_0.parse(none_type_0)
    assert (
        f"{type(docstring_2).__module__}.{type(docstring_2).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_2.short_description is None
    assert docstring_2.long_description is None
    assert docstring_2.blank_after_short_description is False
    assert docstring_2.blank_after_long_description is False
    assert docstring_2.meta == []
    assert docstring_2.style == module_1.DocstringStyle.REST
    str_2 = "ZX\x0cSZxhT7*"
    docstring_3 = module_0.parse(str_2)
    assert (
        f"{type(docstring_3).__module__}.{type(docstring_3).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_3.short_description == "ZX\x0cSZxhT7*"
    assert docstring_3.long_description is None
    assert docstring_3.blank_after_short_description is False
    assert docstring_3.blank_after_long_description is False
    assert docstring_3.meta == []
    assert docstring_3.style == module_1.DocstringStyle.REST
    str_3 = "^Q2i|[RkL"
    docstring_4 = module_0.parse(str_3)
    assert (
        f"{type(docstring_4).__module__}.{type(docstring_4).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_4.short_description == "^Q2i|[RkL"
    assert docstring_4.long_description is None
    assert docstring_4.blank_after_short_description is False
    assert docstring_4.blank_after_long_description is False
    assert docstring_4.meta == []
    assert docstring_4.style == module_1.DocstringStyle.REST
    str_4 = module_0.compose(docstring_2)
    assert str_4 == ""
    module_0.compose(none_type_0, indent=str_1)


def test_case_4():
    str_0 = "DfVe$iLW3^+Mh\n~Fw:k"
    docstring_0 = module_0.parse(str_0)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description == "DfVe$iLW3^+Mh"
    assert docstring_0.long_description == "~Fw:k"
    assert docstring_0.blank_after_short_description is False
    assert docstring_0.blank_after_long_description is False
    assert docstring_0.meta == []
    assert docstring_0.style == module_1.DocstringStyle.REST
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.PARAM_KEYWORDS == {
        "argument",
        "key",
        "parameter",
        "param",
        "attribute",
        "arg",
        "keyword",
    }
    assert module_0.RAISES_KEYWORDS == {"raise", "except", "raises", "exception"}
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
    assert str_1 == "DfVe$iLW3^+Mh\n~Fw:k"
    assert module_1.PARAM_KEYWORDS == {
        "argument",
        "key",
        "parameter",
        "param",
        "attribute",
        "arg",
        "keyword",
    }
    assert module_1.RAISES_KEYWORDS == {"raise", "except", "raises", "exception"}
    assert module_1.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_1.RETURNS_KEYWORDS == {"returns", "return"}
    assert module_1.YIELDS_KEYWORDS == {"yield", "yields"}
    assert module_1.EXAMPLES_KEYWORDS == {"example", "examples"}
    str_2 = "G\x0b4;y\x0b4"
    docstring_1 = module_0.parse(str_2)
    assert (
        f"{type(docstring_1).__module__}.{type(docstring_1).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_1.short_description == "G\x0b4;y\x0b4"
    assert docstring_1.long_description is None
    assert docstring_1.blank_after_short_description is False
    assert docstring_1.blank_after_long_description is False
    assert docstring_1.meta == []
    assert docstring_1.style == module_1.DocstringStyle.REST
    str_3 = module_0.compose(docstring_0, indent=str_0)
    assert str_3 == "DfVe$iLW3^+Mh\n~Fw:k"


def test_case_5():
    str_0 = "ZGl=\nOCnmzFU&UK<dE"
    docstring_0 = module_0.parse(str_0)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description == "ZGl="
    assert docstring_0.long_description == "OCnmzFU&UK<dE"
    assert docstring_0.blank_after_short_description is False
    assert docstring_0.blank_after_long_description is False
    assert docstring_0.meta == []
    assert docstring_0.style == module_1.DocstringStyle.REST
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.PARAM_KEYWORDS == {
        "argument",
        "key",
        "parameter",
        "param",
        "attribute",
        "arg",
        "keyword",
    }
    assert module_0.RAISES_KEYWORDS == {"raise", "except", "raises", "exception"}
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


def test_case_6():
    str_0 = ":"
    with pytest.raises(module_1.ParseError):
        module_0.parse(str_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "BT\n\nqY{L"
    docstring_0 = module_0.parse(str_0)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description == "BT"
    assert docstring_0.long_description == "qY{L"
    assert docstring_0.blank_after_short_description is True
    assert docstring_0.blank_after_long_description is False
    assert docstring_0.meta == []
    assert docstring_0.style == module_1.DocstringStyle.REST
    assert module_0.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_0.PARAM_KEYWORDS == {
        "argument",
        "key",
        "parameter",
        "param",
        "attribute",
        "arg",
        "keyword",
    }
    assert module_0.RAISES_KEYWORDS == {"raise", "except", "raises", "exception"}
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
    assert str_1 == "BT\n\nqY{L"
    assert module_1.PARAM_KEYWORDS == {
        "argument",
        "key",
        "parameter",
        "param",
        "attribute",
        "arg",
        "keyword",
    }
    assert module_1.RAISES_KEYWORDS == {"raise", "except", "raises", "exception"}
    assert module_1.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_1.RETURNS_KEYWORDS == {"returns", "return"}
    assert module_1.YIELDS_KEYWORDS == {"yield", "yields"}
    assert module_1.EXAMPLES_KEYWORDS == {"example", "examples"}
    var_0 = module_2.walk(str_1)
    assert module_2.PyCF_ALLOW_TOP_LEVEL_AWAIT == 8192
    assert module_2.PyCF_ONLY_AST == 1024
    assert module_2.PyCF_TYPE_COMMENTS == 4096
    module_0.compose(var_0)
