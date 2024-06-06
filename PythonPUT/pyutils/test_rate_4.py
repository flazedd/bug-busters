# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import rate as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = 626.95782
    str_0 = "p,_~h}4:z0\nJ\\!&r"
    rate_0 = module_0.Rate(percentage=float_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier == pytest.approx(6.2695782, abs=0.01, rel=0.01)
    var_0 = rate_0.__repr__()
    assert var_0 == "+626.958%"
    rate_0.__add__(str_0)


def test_case_1():
    none_type_0 = None
    with pytest.raises(ValueError):
        module_0.Rate(percent_change=none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    rate_0 = module_0.Rate(percent_change=bool_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier == pytest.approx(1.0, abs=0.01, rel=0.01)
    var_0 = rate_0.__repr__(relative=bool_0)
    assert var_0 == "+100.000%"
    rate_0.__lt__(var_0)


def test_case_3():
    bool_0 = False
    bool_1 = True
    rate_0 = module_0.Rate(bool_1)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier is True
    var_0 = bool_0.__mul__(bool_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    bool_1 = True
    rate_0 = module_0.Rate(bool_1)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier is True
    var_0 = rate_0.__repr__()
    assert var_0 == "+100.000%"
    none_type_0 = None
    var_1 = rate_0.__lt__(bool_0)
    assert var_1 is False
    var_2 = rate_0.__float__()
    assert var_2 is True
    var_3 = rate_0.__lt__(var_2)
    assert var_3 is False
    rate_0.apply_to(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    bool_0 = False
    str_0 = "p,_~h}4:z0\nJ\\!&r"
    rate_0 = module_0.Rate(bool_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier is False
    rate_0.of(str_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    bool_0 = True
    rate_0 = module_0.Rate(bool_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier is True
    var_0 = rate_0.__lt__(bool_0)
    assert var_0 is False
    rate_0.__lt__(rate_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    bool_0 = False
    rate_0 = module_0.Rate(percent_change=bool_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier == pytest.approx(1.0, abs=0.01, rel=0.01)
    var_0 = rate_0.__repr__(relative=bool_0)
    assert var_0 == "+100.000%"
    rate_0.__truediv__(var_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    float_0 = 626.95782
    bool_0 = True
    rate_0 = module_0.Rate(bool_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier is True
    var_0 = rate_0.__lt__(bool_0)
    assert var_0 is False
    var_1 = rate_0.__ge__(float_0)
    assert var_1 is False
    var_2 = var_0.__eq__(float_0)
    var_3 = rate_0.__sub__(var_1)
    assert var_3 == pytest.approx(1.0, abs=0.01, rel=0.01)
    float_1 = 5126.0
    var_0.of(float_1)


@pytest.mark.xfail(strict=True)
def test_case_9():
    bool_0 = False
    bool_1 = True
    rate_0 = module_0.Rate(bool_1)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier is True
    var_0 = rate_0.__lt__(bool_0)
    assert var_0 is False
    var_1 = rate_0.__le__(var_0)
    assert var_1 is False
    var_1.of(bool_1)


@pytest.mark.xfail(strict=True)
def test_case_10():
    bool_0 = True
    rate_0 = module_0.Rate(bool_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier is True
    var_0 = rate_0.__repr__()
    assert var_0 == "+100.000%"
    var_1 = var_0.__lt__(rate_0)
    var_2 = var_1.__lt__(bool_0)
    rate_0.__ne__(var_2)


@pytest.mark.xfail(strict=True)
def test_case_11():
    float_0 = 626.95782
    bool_0 = True
    rate_0 = module_0.Rate(bool_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier is True
    none_type_0 = None
    var_0 = rate_0.__hash__()
    assert var_0 is True
    var_1 = rate_0.__lt__(bool_0)
    assert var_1 is False
    var_2 = rate_0.__ge__(float_0)
    assert var_2 is False
    rate_0.of(none_type_0)


def test_case_12():
    str_0 = "p,_~h}4:z0\nJ\\!&r"
    with pytest.raises(ValueError):
        module_0.Rate(str_0)


@pytest.mark.xfail(strict=True)
def test_case_13():
    float_0 = 626.95782
    bool_0 = True
    rate_0 = module_0.Rate(bool_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier is True
    none_type_0 = None
    var_0 = rate_0.__lt__(bool_0)
    assert var_0 is False
    var_1 = rate_0.__ge__(float_0)
    assert var_1 is False
    none_type_0.__sub__(rate_0)


@pytest.mark.xfail(strict=True)
def test_case_14():
    bool_0 = True
    rate_0 = module_0.Rate(percent_change=bool_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier == pytest.approx(1.01, abs=0.01, rel=0.01)
    var_0 = rate_0.__repr__(relative=bool_0)
    assert var_0 == "+1.000%"
    rate_0.__lt__(var_0)


@pytest.mark.xfail(strict=True)
def test_case_15():
    float_0 = 626.95782
    bool_0 = True
    rate_0 = module_0.Rate(bool_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier is True
    var_0 = rate_0.__lt__(bool_0)
    assert var_0 is False
    var_1 = float_0.__lt__(var_0)
    assert var_1 is False
    var_2 = rate_0.__ge__(var_0)
    assert var_2 is True
    var_1.of(var_1)


@pytest.mark.xfail(strict=True)
def test_case_16():
    float_0 = 626.95782
    bool_0 = False
    rate_0 = module_0.Rate(percentage=bool_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier == pytest.approx(0.0, abs=0.01, rel=0.01)
    var_0 = rate_0.__lt__(float_0)
    assert var_0 is True
    var_1 = var_0.__truediv__(var_0)
    assert var_1 == pytest.approx(1.0, abs=0.01, rel=0.01)
    var_2 = rate_0.__le__(var_1)
    assert var_2 is True
    var_3 = var_1.__ge__(float_0)
    assert var_3 is False
    var_3.of(var_1)