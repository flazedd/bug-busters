# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import comments as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "&P2#g^EJG0=0</UR@_"
    tuple_0 = module_0.parse(str_0)
    tuple_1 = module_0.parse(str_0)
    str_1 = ">SW,v}eW$T'Rs"
    tuple_2 = module_0.parse(str_1)
    none_type_0 = None
    str_2 = module_0.add_to_line(none_type_0, none_type_0, none_type_0)
    str_3 = "]?&ojFl$"
    list_0 = [str_1, str_1, str_3, str_1]
    tuple_3 = module_0.parse(str_1)
    str_4 = module_0.add_to_line(list_0)
    assert str_4 == " >SW,v}eW$T'Rs; ]?&ojFl$"
    str_5 = "2Wz]T-"
    str_6 = module_0.add_to_line(str_1, str_5)
    assert str_6 == "2Wz]T- >; S; W; ,; v; }; e; $; T; '; R; s"
    none_type_1 = None
    module_0.parse(none_type_1)


def test_case_1():
    none_type_0 = None
    str_0 = module_0.add_to_line(none_type_0)
    assert str_0 == ""
    str_1 = "yojP-WSR5AUaeklZ"
    tuple_0 = module_0.parse(str_1)


def test_case_2():
    str_0 = " @yC]&z\rk?{-?G"
    str_1 = ">`yYqhSo"
    tuple_0 = (str_0, str_1)
    dict_0 = {tuple_0: str_0}
    str_2 = 'XZ"|\\b:+5H'
    str_3 = module_0.add_to_line(tuple_0, removed=dict_0, comment_prefix=str_2)
    assert str_3 == ""


def test_case_3():
    none_type_0 = None
    str_0 = module_0.add_to_line(none_type_0)
    assert str_0 == ""


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    module_0.parse(bool_0)


def test_case_5():
    str_0 = "3la"
    tuple_0 = module_0.parse(str_0)
    list_0 = []
    str_1 = module_0.add_to_line(list_0)
    assert str_1 == ""
    str_2 = "~%IdZ\x0b)c{CRw3L"
    str_3 = module_0.add_to_line(str_2)
    assert str_3 == " ~; %; I; d; Z; \x0b; ); c; {; C; R; w; 3; L"


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = '8df<|G"[q'
    tuple_0 = module_0.parse(str_0)
    tuple_1 = module_0.parse(str_0)
    str_1 = "ICHR=9"
    str_2 = "4aH"
    list_0 = [str_0, str_1, str_0, str_2]
    str_3 = module_0.add_to_line(list_0, str_0)
    assert str_3 == '8df<|G"[q 8df<|G"[q; ICHR=9; 4aH'
    module_0.parse(tuple_0)
