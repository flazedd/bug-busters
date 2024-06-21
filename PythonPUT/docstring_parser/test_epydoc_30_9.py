# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import epydoc as module_0
import common as module_1
import token as module_2


def test_case_0():
    str_0 = "2FAz^RpVj5VR=x"
    docstring_0 = module_0.parse(str_0)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description == "2FAz^RpVj5VR=x"
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
    str_0 = module_0.compose(docstring_0, none_type_0)
    assert str_0 == ""
    assert module_1.PARAM_KEYWORDS == {
        "param",
        "attribute",
        "argument",
        "arg",
        "keyword",
        "key",
        "parameter",
    }
    assert module_1.RAISES_KEYWORDS == {"except", "exception", "raise", "raises"}
    assert module_1.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_1.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_1.YIELDS_KEYWORDS == {"yield", "yields"}
    assert module_1.EXAMPLES_KEYWORDS == {"example", "examples"}


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "sBdbyZ.@\x0b"
    docstring_0 = module_0.parse(str_0)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description == "sBdbyZ.@\x0b"
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
    str_1 = "c"
    str_2 = module_0.compose(docstring_0, docstring_0, str_1)
    assert str_2 == "sBdbyZ.@\x0b"
    assert module_1.PARAM_KEYWORDS == {
        "param",
        "attribute",
        "argument",
        "arg",
        "keyword",
        "key",
        "parameter",
    }
    assert module_1.RAISES_KEYWORDS == {"except", "exception", "raise", "raises"}
    assert module_1.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_1.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_1.YIELDS_KEYWORDS == {"yield", "yields"}
    assert module_1.EXAMPLES_KEYWORDS == {"example", "examples"}
    str_3 = "Fl?u'\teF"
    module_0.compose(str_3)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "^: ]7Z$Bsw%&\x0cQ+SHgp"
    docstring_0 = module_0.parse(str_0)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description == "^: ]7Z$Bsw%&\x0cQ+SHgp"
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
    str_1 = "bqc}\rF>,hJSxz\n'p)<"
    docstring_1 = module_0.parse(str_1)
    assert (
        f"{type(docstring_1).__module__}.{type(docstring_1).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_1.short_description == "bqc}\rF>,hJSxz"
    assert docstring_1.long_description == "'p)<"
    assert docstring_1.blank_after_short_description is False
    assert docstring_1.blank_after_long_description is False
    assert docstring_1.meta == []
    assert docstring_1.style == module_1.DocstringStyle.EPYDOC
    assert module_1.PARAM_KEYWORDS == {
        "param",
        "attribute",
        "argument",
        "arg",
        "keyword",
        "key",
        "parameter",
    }
    assert module_1.RAISES_KEYWORDS == {"except", "exception", "raise", "raises"}
    assert module_1.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_1.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_1.YIELDS_KEYWORDS == {"yield", "yields"}
    assert module_1.EXAMPLES_KEYWORDS == {"example", "examples"}
    docstring_2 = module_0.parse(str_0)
    assert (
        f"{type(docstring_2).__module__}.{type(docstring_2).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_2.short_description == "^: ]7Z$Bsw%&\x0cQ+SHgp"
    assert docstring_2.long_description is None
    assert docstring_2.blank_after_short_description is False
    assert docstring_2.blank_after_long_description is False
    assert docstring_2.meta == []
    assert docstring_2.style == module_1.DocstringStyle.EPYDOC
    str_2 = module_0.compose(docstring_0, docstring_0)
    assert str_2 == "^: ]7Z$Bsw%&\x0cQ+SHgp"
    str_3 = "+"
    docstring_3 = module_0.parse(str_3)
    assert (
        f"{type(docstring_3).__module__}.{type(docstring_3).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_3.short_description == "+"
    assert docstring_3.long_description is None
    assert docstring_3.blank_after_short_description is False
    assert docstring_3.blank_after_long_description is False
    assert docstring_3.meta == []
    assert docstring_3.style == module_1.DocstringStyle.EPYDOC
    var_0 = module_2.ISEOF(str_0)
    assert var_0 is False
    assert module_2.ENDMARKER == 0
    assert module_2.NAME == 1
    assert module_2.NUMBER == 2
    assert module_2.STRING == 3
    assert module_2.NEWLINE == 4
    assert module_2.INDENT == 5
    assert module_2.DEDENT == 6
    assert module_2.LPAR == 7
    assert module_2.RPAR == 8
    assert module_2.LSQB == 9
    assert module_2.RSQB == 10
    assert module_2.COLON == 11
    assert module_2.COMMA == 12
    assert module_2.SEMI == 13
    assert module_2.PLUS == 14
    assert module_2.MINUS == 15
    assert module_2.STAR == 16
    assert module_2.SLASH == 17
    assert module_2.VBAR == 18
    assert module_2.AMPER == 19
    assert module_2.LESS == 20
    assert module_2.GREATER == 21
    assert module_2.EQUAL == 22
    assert module_2.DOT == 23
    assert module_2.PERCENT == 24
    assert module_2.LBRACE == 25
    assert module_2.RBRACE == 26
    assert module_2.EQEQUAL == 27
    assert module_2.NOTEQUAL == 28
    assert module_2.LESSEQUAL == 29
    assert module_2.GREATEREQUAL == 30
    assert module_2.TILDE == 31
    assert module_2.CIRCUMFLEX == 32
    assert module_2.LEFTSHIFT == 33
    assert module_2.RIGHTSHIFT == 34
    assert module_2.DOUBLESTAR == 35
    assert module_2.PLUSEQUAL == 36
    assert module_2.MINEQUAL == 37
    assert module_2.STAREQUAL == 38
    assert module_2.SLASHEQUAL == 39
    assert module_2.PERCENTEQUAL == 40
    assert module_2.AMPEREQUAL == 41
    assert module_2.VBAREQUAL == 42
    assert module_2.CIRCUMFLEXEQUAL == 43
    assert module_2.LEFTSHIFTEQUAL == 44
    assert module_2.RIGHTSHIFTEQUAL == 45
    assert module_2.DOUBLESTAREQUAL == 46
    assert module_2.DOUBLESLASH == 47
    assert module_2.DOUBLESLASHEQUAL == 48
    assert module_2.AT == 49
    assert module_2.ATEQUAL == 50
    assert module_2.RARROW == 51
    assert module_2.ELLIPSIS == 52
    assert module_2.COLONEQUAL == 53
    assert module_2.OP == 54
    assert module_2.AWAIT == 55
    assert module_2.ASYNC == 56
    assert module_2.TYPE_IGNORE == 57
    assert module_2.TYPE_COMMENT == 58
    assert module_2.SOFT_KEYWORD == 59
    assert module_2.ERRORTOKEN == 60
    assert module_2.COMMENT == 61
    assert module_2.NL == 62
    assert module_2.ENCODING == 63
    assert module_2.N_TOKENS == 64
    assert module_2.NT_OFFSET == 256
    assert module_2.tok_name == {
        0: "ENDMARKER",
        1: "NAME",
        2: "NUMBER",
        3: "STRING",
        4: "NEWLINE",
        5: "INDENT",
        6: "DEDENT",
        7: "LPAR",
        8: "RPAR",
        9: "LSQB",
        10: "RSQB",
        11: "COLON",
        12: "COMMA",
        13: "SEMI",
        14: "PLUS",
        15: "MINUS",
        16: "STAR",
        17: "SLASH",
        18: "VBAR",
        19: "AMPER",
        20: "LESS",
        21: "GREATER",
        22: "EQUAL",
        23: "DOT",
        24: "PERCENT",
        25: "LBRACE",
        26: "RBRACE",
        27: "EQEQUAL",
        28: "NOTEQUAL",
        29: "LESSEQUAL",
        30: "GREATEREQUAL",
        31: "TILDE",
        32: "CIRCUMFLEX",
        33: "LEFTSHIFT",
        34: "RIGHTSHIFT",
        35: "DOUBLESTAR",
        36: "PLUSEQUAL",
        37: "MINEQUAL",
        38: "STAREQUAL",
        39: "SLASHEQUAL",
        40: "PERCENTEQUAL",
        41: "AMPEREQUAL",
        42: "VBAREQUAL",
        43: "CIRCUMFLEXEQUAL",
        44: "LEFTSHIFTEQUAL",
        45: "RIGHTSHIFTEQUAL",
        46: "DOUBLESTAREQUAL",
        47: "DOUBLESLASH",
        48: "DOUBLESLASHEQUAL",
        49: "AT",
        50: "ATEQUAL",
        51: "RARROW",
        52: "ELLIPSIS",
        53: "COLONEQUAL",
        54: "OP",
        55: "AWAIT",
        56: "ASYNC",
        57: "TYPE_IGNORE",
        58: "TYPE_COMMENT",
        59: "SOFT_KEYWORD",
        60: "ERRORTOKEN",
        61: "COMMENT",
        62: "NL",
        63: "ENCODING",
        64: "N_TOKENS",
        256: "NT_OFFSET",
    }
    assert module_2.EXACT_TOKEN_TYPES == {
        "!=": 28,
        "%": 24,
        "%=": 40,
        "&": 19,
        "&=": 41,
        "(": 7,
        ")": 8,
        "*": 16,
        "**": 35,
        "**=": 46,
        "*=": 38,
        "+": 14,
        "+=": 36,
        ",": 12,
        "-": 15,
        "-=": 37,
        "->": 51,
        ".": 23,
        "...": 52,
        "/": 17,
        "//": 47,
        "//=": 48,
        "/=": 39,
        ":": 11,
        ":=": 53,
        ";": 13,
        "<": 20,
        "<<": 33,
        "<<=": 44,
        "<=": 29,
        "=": 22,
        "==": 27,
        ">": 21,
        ">=": 30,
        ">>": 34,
        ">>=": 45,
        "@": 49,
        "@=": 50,
        "[": 9,
        "]": 10,
        "^": 32,
        "^=": 43,
        "{": 25,
        "|": 18,
        "|=": 42,
        "}": 26,
        "~": 31,
    }
    module_0.parse(docstring_2)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "^: ]7Z$Bsw%&\x0cQ+SHgp"
    none_type_0 = None
    str_1 = "bqc}\rF>,hJSxz\n'p)<"
    docstring_0 = module_0.parse(str_1)
    assert (
        f"{type(docstring_0).__module__}.{type(docstring_0).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_0.short_description == "bqc}\rF>,hJSxz"
    assert docstring_0.long_description == "'p)<"
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
    docstring_1 = module_0.parse(none_type_0)
    assert (
        f"{type(docstring_1).__module__}.{type(docstring_1).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_1.short_description is None
    assert docstring_1.long_description is None
    assert docstring_1.blank_after_short_description is False
    assert docstring_1.blank_after_long_description is False
    assert docstring_1.meta == []
    assert docstring_1.style == module_1.DocstringStyle.EPYDOC
    assert module_1.PARAM_KEYWORDS == {
        "param",
        "attribute",
        "argument",
        "arg",
        "keyword",
        "key",
        "parameter",
    }
    assert module_1.RAISES_KEYWORDS == {"except", "exception", "raise", "raises"}
    assert module_1.DEPRECATION_KEYWORDS == {"deprecated", "deprecation"}
    assert module_1.RETURNS_KEYWORDS == {"return", "returns"}
    assert module_1.YIELDS_KEYWORDS == {"yield", "yields"}
    assert module_1.EXAMPLES_KEYWORDS == {"example", "examples"}
    str_2 = module_0.compose(docstring_0, docstring_0)
    assert str_2 == "bqc}\rF>,hJSxz\n'p)<"
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
    assert docstring_2.style == module_1.DocstringStyle.EPYDOC
    str_3 = module_0.compose(docstring_1, docstring_2)
    assert str_3 == ""
    docstring_3 = module_0.parse(str_2)
    assert (
        f"{type(docstring_3).__module__}.{type(docstring_3).__qualname__}"
        == "common.Docstring"
    )
    assert docstring_3.short_description == "bqc}\rF>,hJSxz"
    assert docstring_3.long_description == "'p)<"
    assert docstring_3.blank_after_short_description is False
    assert docstring_3.blank_after_long_description is False
    assert docstring_3.meta == []
    assert docstring_3.style == module_1.DocstringStyle.EPYDOC
    var_0 = module_2.ISEOF(str_0)
    assert var_0 is False
    assert module_2.ENDMARKER == 0
    assert module_2.NAME == 1
    assert module_2.NUMBER == 2
    assert module_2.STRING == 3
    assert module_2.NEWLINE == 4
    assert module_2.INDENT == 5
    assert module_2.DEDENT == 6
    assert module_2.LPAR == 7
    assert module_2.RPAR == 8
    assert module_2.LSQB == 9
    assert module_2.RSQB == 10
    assert module_2.COLON == 11
    assert module_2.COMMA == 12
    assert module_2.SEMI == 13
    assert module_2.PLUS == 14
    assert module_2.MINUS == 15
    assert module_2.STAR == 16
    assert module_2.SLASH == 17
    assert module_2.VBAR == 18
    assert module_2.AMPER == 19
    assert module_2.LESS == 20
    assert module_2.GREATER == 21
    assert module_2.EQUAL == 22
    assert module_2.DOT == 23
    assert module_2.PERCENT == 24
    assert module_2.LBRACE == 25
    assert module_2.RBRACE == 26
    assert module_2.EQEQUAL == 27
    assert module_2.NOTEQUAL == 28
    assert module_2.LESSEQUAL == 29
    assert module_2.GREATEREQUAL == 30
    assert module_2.TILDE == 31
    assert module_2.CIRCUMFLEX == 32
    assert module_2.LEFTSHIFT == 33
    assert module_2.RIGHTSHIFT == 34
    assert module_2.DOUBLESTAR == 35
    assert module_2.PLUSEQUAL == 36
    assert module_2.MINEQUAL == 37
    assert module_2.STAREQUAL == 38
    assert module_2.SLASHEQUAL == 39
    assert module_2.PERCENTEQUAL == 40
    assert module_2.AMPEREQUAL == 41
    assert module_2.VBAREQUAL == 42
    assert module_2.CIRCUMFLEXEQUAL == 43
    assert module_2.LEFTSHIFTEQUAL == 44
    assert module_2.RIGHTSHIFTEQUAL == 45
    assert module_2.DOUBLESTAREQUAL == 46
    assert module_2.DOUBLESLASH == 47
    assert module_2.DOUBLESLASHEQUAL == 48
    assert module_2.AT == 49
    assert module_2.ATEQUAL == 50
    assert module_2.RARROW == 51
    assert module_2.ELLIPSIS == 52
    assert module_2.COLONEQUAL == 53
    assert module_2.OP == 54
    assert module_2.AWAIT == 55
    assert module_2.ASYNC == 56
    assert module_2.TYPE_IGNORE == 57
    assert module_2.TYPE_COMMENT == 58
    assert module_2.SOFT_KEYWORD == 59
    assert module_2.ERRORTOKEN == 60
    assert module_2.COMMENT == 61
    assert module_2.NL == 62
    assert module_2.ENCODING == 63
    assert module_2.N_TOKENS == 64
    assert module_2.NT_OFFSET == 256
    assert module_2.tok_name == {
        0: "ENDMARKER",
        1: "NAME",
        2: "NUMBER",
        3: "STRING",
        4: "NEWLINE",
        5: "INDENT",
        6: "DEDENT",
        7: "LPAR",
        8: "RPAR",
        9: "LSQB",
        10: "RSQB",
        11: "COLON",
        12: "COMMA",
        13: "SEMI",
        14: "PLUS",
        15: "MINUS",
        16: "STAR",
        17: "SLASH",
        18: "VBAR",
        19: "AMPER",
        20: "LESS",
        21: "GREATER",
        22: "EQUAL",
        23: "DOT",
        24: "PERCENT",
        25: "LBRACE",
        26: "RBRACE",
        27: "EQEQUAL",
        28: "NOTEQUAL",
        29: "LESSEQUAL",
        30: "GREATEREQUAL",
        31: "TILDE",
        32: "CIRCUMFLEX",
        33: "LEFTSHIFT",
        34: "RIGHTSHIFT",
        35: "DOUBLESTAR",
        36: "PLUSEQUAL",
        37: "MINEQUAL",
        38: "STAREQUAL",
        39: "SLASHEQUAL",
        40: "PERCENTEQUAL",
        41: "AMPEREQUAL",
        42: "VBAREQUAL",
        43: "CIRCUMFLEXEQUAL",
        44: "LEFTSHIFTEQUAL",
        45: "RIGHTSHIFTEQUAL",
        46: "DOUBLESTAREQUAL",
        47: "DOUBLESLASH",
        48: "DOUBLESLASHEQUAL",
        49: "AT",
        50: "ATEQUAL",
        51: "RARROW",
        52: "ELLIPSIS",
        53: "COLONEQUAL",
        54: "OP",
        55: "AWAIT",
        56: "ASYNC",
        57: "TYPE_IGNORE",
        58: "TYPE_COMMENT",
        59: "SOFT_KEYWORD",
        60: "ERRORTOKEN",
        61: "COMMENT",
        62: "NL",
        63: "ENCODING",
        64: "N_TOKENS",
        256: "NT_OFFSET",
    }
    assert module_2.EXACT_TOKEN_TYPES == {
        "!=": 28,
        "%": 24,
        "%=": 40,
        "&": 19,
        "&=": 41,
        "(": 7,
        ")": 8,
        "*": 16,
        "**": 35,
        "**=": 46,
        "*=": 38,
        "+": 14,
        "+=": 36,
        ",": 12,
        "-": 15,
        "-=": 37,
        "->": 51,
        ".": 23,
        "...": 52,
        "/": 17,
        "//": 47,
        "//=": 48,
        "/=": 39,
        ":": 11,
        ":=": 53,
        ";": 13,
        "<": 20,
        "<<": 33,
        "<<=": 44,
        "<=": 29,
        "=": 22,
        "==": 27,
        ">": 21,
        ">=": 30,
        ">>": 34,
        ">>=": 45,
        "@": 49,
        "@=": 50,
        "[": 9,
        "]": 10,
        "^": 32,
        "^=": 43,
        "{": 25,
        "|": 18,
        "|=": 42,
        "}": 26,
        "~": 31,
    }
    module_0.parse(docstring_1)


def test_case_5():
    str_0 = "@.8"
    with pytest.raises(module_1.ParseError):
        module_0.parse(str_0)