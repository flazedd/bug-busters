# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import validators as module_0
import collections as module_1


def test_case_0():
    str_0 = 'X&9hBEH=,"rAyr'
    with pytest.raises(SyntaxError):
        module_0.validate_identifier(str_0)


def test_case_1():
    str_0 = ""
    bool_0 = False
    tuple_0 = (str_0, bool_0)
    user_string_0 = module_1.UserString(tuple_0)
    assert (
        f"{type(user_string_0).__module__}.{type(user_string_0).__qualname__}"
        == "collections.UserString"
    )
    assert len(user_string_0) == 11
    with pytest.raises(SyntaxError):
        module_0.validate_identifier(user_string_0)


def test_case_2():
    none_type_0 = None
    with pytest.raises(TypeError):
        module_0.validate_identifier(none_type_0)


def test_case_3():
    str_0 = ""
    with pytest.raises(SyntaxError):
        module_0.validate_identifier(str_0)


def test_case_4():
    str_0 = "K"
    bool_0 = False
    none_type_0 = module_0.validate_identifier(str_0, bool_0)


def test_case_5():
    str_0 = "09({!l"
    with pytest.raises(SyntaxError):
        module_0.validate_identifier(str_0)


def test_case_6():
    str_0 = "eutf8h"
    none_type_0 = module_0.validate_identifier(str_0)
    none_type_1 = module_0.validate_identifier(str_0)


def test_case_7():
    none_type_0 = None
    user_string_0 = module_1.UserString(none_type_0)
    assert (
        f"{type(user_string_0).__module__}.{type(user_string_0).__qualname__}"
        == "collections.UserString"
    )
    assert len(user_string_0) == 4
    with pytest.raises(SyntaxError):
        module_0.validate_identifier(user_string_0)


def test_case_8():
    str_0 = "_"
    bool_0 = False
    with pytest.raises(SyntaxError):
        module_0.validate_identifier(str_0, bool_0)
