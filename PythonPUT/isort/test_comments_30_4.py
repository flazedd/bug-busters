# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import comments as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = ">;xyIq"
    tuple_0 = module_0.parse(str_0)
    str_1 = "ck/#otIf*d6n[`!=h3bx"
    tuple_1 = module_0.parse(str_1)
    none_type_0 = None
    module_0.parse(none_type_0)


def test_case_1():
    str_0 = 'withu2fG"Cp"'
    tuple_0 = module_0.parse(str_0)


def test_case_2():
    none_type_0 = None
    bool_0 = True
    str_0 = module_0.add_to_line(none_type_0, removed=bool_0)
    assert str_0 == ""


def test_case_3():
    str_0 = "EGJ/kVmgP[wVc+M(g5R"
    list_0 = [str_0]
    str_1 = module_0.add_to_line(list_0, comment_prefix=list_0)
    assert str_1 == "['EGJ/kVmgP[wVc+M(g5R'] EGJ/kVmgP[wVc+M(g5R"


@pytest.mark.xfail(strict=True)
def test_case_4():
    none_type_0 = None
    str_0 = module_0.add_to_line(none_type_0)
    assert str_0 == ""
    tuple_0 = module_0.parse(str_0)
    str_1 = module_0.add_to_line(none_type_0)
    assert str_1 == ""
    tuple_1 = module_0.parse(str_0)
    module_0.parse(none_type_0)


def test_case_5():
    none_type_0 = None
    str_0 = module_0.add_to_line(none_type_0)
    assert str_0 == ""
    str_1 = ""
    str_2 = "9aZ7"
    list_0 = [str_2, str_2, str_1]
    str_3 = module_0.add_to_line(str_2)
    assert str_3 == " 9; a; Z; 7"
    str_4 = "AGcOd"
    str_5 = module_0.add_to_line(list_0, str_4, str_4, str_4)
    assert str_5 == "AGcOd"
    tuple_0 = module_0.parse(str_1)
    str_6 = "K6pN-}&u<"
    str_7 = module_0.add_to_line(list_0, str_6)
    assert str_7 == "K6pN-}&u< 9aZ7; "
