# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import comments as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    none_type_0 = None
    str_0 = module_0.add_to_line(none_type_0)
    assert str_0 == ""
    str_1 = module_0.add_to_line(none_type_0, none_type_0)
    str_2 = "z<;$ Z`E\x0b#JU"
    tuple_0 = module_0.parse(str_2)
    module_0.parse(none_type_0)


def test_case_1():
    str_0 = "|6v(dT|RFrX^wkJMdU"
    tuple_0 = module_0.parse(str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    set_0 = set()
    str_0 = "gbc~4Z|]e?~rLsN.\x0b"
    list_0 = []
    tuple_0 = module_0.parse(str_0)
    str_1 = module_0.add_to_line(tuple_0, comment_prefix=list_0)
    assert str_1 == "[] gbc~4Z|]e?~rLsN.\x0b; "
    str_2 = module_0.add_to_line(tuple_0)
    assert str_2 == " gbc~4Z|]e?~rLsN.\x0b; "
    bool_0 = True
    str_3 = module_0.add_to_line(list_0, removed=bool_0)
    assert str_3 == ""
    list_1 = [str_0, str_0, str_0]
    none_type_0 = None
    str_4 = module_0.add_to_line(none_type_0, removed=str_0)
    assert str_4 == ""
    str_5 = module_0.add_to_line(list_1)
    assert str_5 == " gbc~4Z|]e?~rLsN.\x0b"
    str_6 = "Z=}[%UZ j!-9PlfR~c1o"
    str_7 = module_0.add_to_line(set_0, comment_prefix=str_6)
    assert str_7 == ""
    str_8 = module_0.add_to_line(set_0, str_0, list_1)
    assert str_8 == "gbc~4Z|]e?~rLsN.\x0b"
    str_9 = "?\nV+Mt"
    tuple_1 = module_0.parse(str_9)
    none_type_1 = None
    str_10 = "K Zu~Upptj"
    module_0.add_to_line(list_1, none_type_1, comment_prefix=str_10)


def test_case_3():
    none_type_0 = None
    str_0 = module_0.add_to_line(none_type_0, comment_prefix=none_type_0)
    assert str_0 == ""


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = " aqVyLMWxO|~,n$"
    str_1 = "9k nyLt[ )++8%AYI:0"
    list_0 = [str_0, str_1, str_0]
    float_0 = 809.7731
    dict_0 = {float_0: float_0, str_1: float_0, float_0: float_0}
    module_0.add_to_line(list_0, dict_0)