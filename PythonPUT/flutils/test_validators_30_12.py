# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import validators as module_0
import collections as module_1


def test_case_0():
    bool_0 = False
    with pytest.raises(TypeError):
        module_0.validate_identifier(bool_0)


def test_case_1():
    str_0 = 'tF$>v9 K\rL>~\n"<?f'
    with pytest.raises(SyntaxError):
        module_0.validate_identifier(str_0, str_0)


def test_case_2():
    str_0 = ""
    with pytest.raises(SyntaxError):
        module_0.validate_identifier(str_0)


def test_case_3():
    str_0 = "0hM6=LC?IT9iY#m`K_"
    with pytest.raises(SyntaxError):
        module_0.validate_identifier(str_0)


def test_case_4():
    str_0 = "utf8"
    none_type_0 = module_0.validate_identifier(str_0)


def test_case_5():
    str_0 = "b64"
    none_type_0 = module_0.validate_identifier(str_0, str_0)
    none_type_1 = module_0.validate_identifier(str_0)
    none_type_2 = module_0.validate_identifier(str_0)
    none_type_3 = module_0.validate_identifier(str_0)
    user_string_0 = module_1.UserString(none_type_2)
    assert (
        f"{type(user_string_0).__module__}.{type(user_string_0).__qualname__}"
        == "collections.UserString"
    )
    assert len(user_string_0) == 4
    with pytest.raises(SyntaxError):
        module_0.validate_identifier(user_string_0)


def test_case_6():
    str_0 = "T"
    bool_0 = False
    none_type_0 = module_0.validate_identifier(str_0, bool_0)
    str_1 = "9"
    with pytest.raises(SyntaxError):
        module_0.validate_identifier(str_1, str_1)


def test_case_7():
    str_0 = "T"
    none_type_0 = module_0.validate_identifier(str_0)
    none_type_1 = module_0.validate_identifier(str_0)
    bool_0 = False
    str_1 = "strit"
    none_type_2 = module_0.validate_identifier(str_1)
    none_type_3 = module_0.validate_identifier(str_0, bool_0)
    none_type_4 = module_0.validate_identifier(str_1)
    none_type_5 = module_0.validate_identifier(str_0, none_type_1)
    str_2 = "\r_7G.[.8s"
    with pytest.raises(SyntaxError):
        module_0.validate_identifier(str_2, bool_0)