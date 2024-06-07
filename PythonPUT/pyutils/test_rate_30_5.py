# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import rate as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    set_0 = {bool_0, bool_0, bool_0, bool_0}
    list_0 = [set_0, bool_0, bool_0, bool_0]
    bool_1 = False
    rate_0 = module_0.Rate(percentage=bool_1)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier == pytest.approx(0.0, abs=0.01, rel=0.01)
    rate_0.__mul__(list_0)


def test_case_1():
    with pytest.raises(ValueError):
        module_0.Rate()


def test_case_2():
    bool_0 = True
    bool_1 = True
    rate_0 = module_0.Rate(percent_change=bool_1)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier == pytest.approx(1.01, abs=0.01, rel=0.01)
    var_0 = rate_0.__sub__(bool_0)
    assert var_0 == pytest.approx(0.010000000000000009, abs=0.01, rel=0.01)


def test_case_3():
    bool_0 = False
    rate_0 = module_0.Rate(bool_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier is False


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    rate_0 = module_0.Rate(percent_change=bool_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier == pytest.approx(1.0, abs=0.01, rel=0.01)
    var_0 = rate_0.__repr__()
    assert var_0 == "+100.000%"
    var_1 = var_0.__eq__(var_0)
    assert var_1 is True
    var_1.apply_to(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"32\xa2u;\xa3\x03<\xf5N\xc6\xaf+-\x97\xcc\xff\x8dg"
    bool_0 = True
    rate_0 = module_0.Rate(bool_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier is True
    rate_0.apply_to(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    list_0 = []
    rate_0 = module_0.Rate(list_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier == []
    rate_0.__sub__(rate_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    bool_0 = False
    rate_0 = module_0.Rate(bool_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier is False
    rate_0.__truediv__(bool_0)


def test_case_8():
    bool_0 = True
    rate_0 = module_0.Rate(percentage=bool_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier == pytest.approx(0.01, abs=0.01, rel=0.01)
    var_0 = rate_0.__le__(bool_0)
    assert var_0 is True
    var_1 = var_0.__gt__(bool_0)
    assert var_1 is False
    var_2 = var_1.__mul__(bool_0)
    assert var_2 == 0
    var_3 = var_2.__truediv__(bool_0)
    assert var_3 == pytest.approx(0.0, abs=0.01, rel=0.01)
    var_4 = var_3.__gt__(bool_0)
    assert var_4 is False
    rate_1 = module_0.Rate(bool_0)
    assert f"{type(rate_1).__module__}.{type(rate_1).__qualname__}" == "rate.Rate"
    assert rate_1.multiplier is True
    var_5 = rate_1.__add__(bool_0)
    assert var_5 == pytest.approx(2.0, abs=0.01, rel=0.01)
    var_6 = var_5.__ne__(bool_0)
    assert var_6 is True
    var_7 = var_6.__gt__(bool_0)
    assert var_7 is False
    var_8 = var_7.__lt__(bool_0)
    assert var_8 is True
    bool_1 = False
    bool_2 = False
    rate_2 = module_0.Rate(bool_2)
    assert f"{type(rate_2).__module__}.{type(rate_2).__qualname__}" == "rate.Rate"
    assert rate_2.multiplier is False
    var_9 = rate_2.__ne__(bool_1)
    assert var_9 is False
    var_10 = var_9.__truediv__(bool_0)
    assert var_10 == pytest.approx(0.0, abs=0.01, rel=0.01)


@pytest.mark.xfail(strict=True)
def test_case_9():
    complex_0 = -2973.62485 + 393j
    bytes_0 = b"\x80"
    rate_0 = module_0.Rate(percentage=complex_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier == (-29.736248500000002 + 3.93j)
    rate_0.of(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_10():
    none_type_0 = None
    int_0 = -1398
    rate_0 = module_0.Rate(int_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier == -1398
    var_0 = rate_0.__float__()
    assert var_0 == -1398
    var_1 = var_0.__ne__(none_type_0)
    rate_0.__add__(var_1)


@pytest.mark.xfail(strict=True)
def test_case_11():
    bool_0 = False
    none_type_0 = None
    rate_0 = module_0.Rate(bool_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier is False
    rate_0.__le__(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_12():
    float_0 = 3191.3175
    none_type_0 = None
    rate_0 = module_0.Rate(float_0, percentage=none_type_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier == pytest.approx(3191.3175, abs=0.01, rel=0.01)
    var_0 = rate_0.__ge__(rate_0)
    assert var_0 is True
    var_1 = var_0.__truediv__(var_0)
    assert var_1 == pytest.approx(1.0, abs=0.01, rel=0.01)
    var_2 = rate_0.__repr__(relative=var_0)
    assert var_2 == "+319031.750%"
    var_3 = var_2.__ge__(rate_0)
    var_4 = var_3.__le__(var_0)
    rate_0.__le__(var_4)


@pytest.mark.xfail(strict=True)
def test_case_13():
    dict_0 = {}
    none_type_0 = None
    rate_0 = module_0.Rate(dict_0, percent_change=none_type_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier == {}
    var_0 = rate_0.__hash__()
    rate_0.__repr__()


@pytest.mark.xfail(strict=True)
def test_case_14():
    float_0 = 3191.3175
    none_type_0 = None
    rate_0 = module_0.Rate(float_0, percentage=none_type_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier == pytest.approx(3191.3175, abs=0.01, rel=0.01)
    var_0 = rate_0.__ge__(rate_0)
    assert var_0 is True
    bool_0 = False
    var_0.__truediv__(bool_0)


def test_case_15():
    bool_0 = True
    rate_0 = module_0.Rate(percentage=bool_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier == pytest.approx(0.01, abs=0.01, rel=0.01)
    var_0 = rate_0.__le__(bool_0)
    assert var_0 is True
    var_1 = var_0.__gt__(bool_0)
    assert var_1 is False
    var_2 = var_1.__mul__(bool_0)
    assert var_2 == 0
    var_3 = var_2.__truediv__(bool_0)
    assert var_3 == pytest.approx(0.0, abs=0.01, rel=0.01)
    var_4 = var_3.__gt__(bool_0)
    assert var_4 is False
    rate_1 = module_0.Rate(bool_0)
    assert f"{type(rate_1).__module__}.{type(rate_1).__qualname__}" == "rate.Rate"
    assert rate_1.multiplier is True
    var_5 = rate_1.__add__(bool_0)
    assert var_5 == pytest.approx(2.0, abs=0.01, rel=0.01)
    var_6 = var_5.__ne__(bool_0)
    assert var_6 is True
    var_7 = var_6.__gt__(bool_0)
    assert var_7 is False
    var_8 = var_7.__lt__(bool_0)
    assert var_8 is True
    rate_2 = module_0.Rate(percentage=var_4)
    assert f"{type(rate_2).__module__}.{type(rate_2).__qualname__}" == "rate.Rate"
    assert rate_2.multiplier == pytest.approx(0.0, abs=0.01, rel=0.01)
    var_9 = var_7.__eq__(var_7)
    assert var_9 is True
    var_10 = var_1.__eq__(rate_2)
    var_11 = rate_1.__add__(var_5)
    assert var_11 == pytest.approx(3.0, abs=0.01, rel=0.01)
    var_12 = var_9.__float__()
    assert var_12 == pytest.approx(1.0, abs=0.01, rel=0.01)
    var_13 = rate_1.__ge__(var_4)
    assert var_13 is True
    var_14 = var_0.__add__(var_8)
    assert var_14 == 2


def test_case_16():
    none_type_0 = None
    str_0 = "T!%0_Zkr"
    with pytest.raises(ValueError):
        module_0.Rate(str_0, percent_change=none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_17():
    bool_0 = True
    rate_0 = module_0.Rate(percentage=bool_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier == pytest.approx(0.01, abs=0.01, rel=0.01)
    var_0 = rate_0.__le__(bool_0)
    assert var_0 is True
    var_1 = rate_0.__ge__(var_0)
    assert var_1 is False
    var_2 = var_1.__mul__(bool_0)
    assert var_2 == 0
    var_3 = var_2.__hash__()
    assert var_3 == 0
    var_4 = var_3.__gt__(bool_0)
    assert var_4 is False
    rate_1 = var_2.__gt__(var_3)
    assert rate_1 is False
    bool_1 = True
    var_5 = var_0.__ne__(bool_1)
    assert var_5 is False
    var_6 = var_5.__ge__(var_1)
    assert var_6 is True
    var_7 = var_3.__le__(var_3)
    assert var_7 is True
    int_0 = -502
    var_8 = var_1.__le__(int_0)
    assert var_8 is False
    var_9 = var_8.__sub__(var_6)
    assert var_9 == -1
    var_10 = rate_0.__sub__(rate_1)
    assert var_10 == pytest.approx(0.01, abs=0.01, rel=0.01)
    var_11 = var_10.__gt__(var_4)
    assert var_11 is True
    var_12 = var_3.__sub__(var_2)
    assert var_12 == 0
    var_13 = var_3.__sub__(var_4)
    assert var_13 == 0
    var_14 = var_8.__sub__(var_1)
    assert var_14 == 0
    var_15 = var_9.__eq__(bool_0)
    assert var_15 is False
    var_16 = rate_0.__le__(var_12)
    assert var_16 is False
    var_16.__repr__(places=rate_0)