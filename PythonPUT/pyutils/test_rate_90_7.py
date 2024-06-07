# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import rate as module_0


def test_case_0():
    bool_0 = True
    rate_0 = module_0.Rate(bool_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier is True
    var_0 = rate_0.__ge__(bool_0)
    assert var_0 is True
    var_1 = rate_0.__lt__(var_0)
    assert var_1 is False
    with pytest.raises(ValueError):
        module_0.Rate(var_0, percentage=var_0)


def test_case_1():
    int_0 = 56
    rate_0 = module_0.Rate(int_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier == 56


def test_case_2():
    bool_0 = True
    with pytest.raises(ValueError):
        module_0.Rate(bool_0, percent_change=bool_0)


def test_case_3():
    with pytest.raises(ValueError):
        module_0.Rate()


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = -3449
    rate_0 = module_0.Rate(int_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier == -3449
    var_0 = rate_0.__hash__()
    assert var_0 == -3449
    var_1 = rate_0.__float__()
    assert var_1 == -3449
    rate_0.__repr__(places=var_1)


@pytest.mark.xfail(strict=True)
def test_case_5():
    int_0 = -3449
    rate_0 = module_0.Rate(int_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier == -3449
    var_0 = rate_0.__sub__(int_0)
    assert var_0 == pytest.approx(0.0, abs=0.01, rel=0.01)
    rate_0.of(rate_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    bool_0 = True
    rate_0 = module_0.Rate(bool_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier is True
    rate_0.__ge__(rate_0)


def test_case_7():
    int_0 = -3449
    rate_0 = module_0.Rate(int_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier == -3449
    var_0 = rate_0.__float__()
    assert var_0 == -3449
    var_1 = var_0.__repr__()
    assert var_1 == "-3449"
    var_2 = rate_0.__mul__(var_1)
    assert var_2 == pytest.approx(11895601.0, abs=0.01, rel=0.01)
    with pytest.raises(ValueError):
        module_0.Rate()


@pytest.mark.xfail(strict=True)
def test_case_8():
    int_0 = -3449
    none_type_0 = None
    rate_0 = module_0.Rate(int_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier == -3449
    var_0 = rate_0.__le__(int_0)
    assert var_0 is True
    var_1 = rate_0.__sub__(var_0)
    assert var_1 == pytest.approx(-3450.0, abs=0.01, rel=0.01)
    none_type_0.__mul__(int_0)


def test_case_9():
    bool_0 = True
    rate_0 = module_0.Rate(bool_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier is True
    var_0 = rate_0.__ge__(bool_0)
    assert var_0 is True
    var_1 = rate_0.__ne__(var_0)
    assert var_1 is False


@pytest.mark.xfail(strict=True)
def test_case_10():
    int_0 = -3449
    rate_0 = module_0.Rate(int_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier == -3449
    var_0 = rate_0.__le__(int_0)
    assert var_0 is True
    var_1 = rate_0.__repr__(relative=rate_0)
    assert var_1 == "-345000.000%"
    rate_0.__repr__(places=var_1)


@pytest.mark.xfail(strict=True)
def test_case_11():
    none_type_0 = None
    float_0 = 1571.74
    rate_0 = module_0.Rate(float_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier == pytest.approx(1571.74, abs=0.01, rel=0.01)
    rate_0.apply_to(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_12():
    dict_0 = {}
    tuple_0 = (dict_0,)
    bool_0 = False
    bool_1 = True
    rate_0 = module_0.Rate(percent_change=bool_1)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier == pytest.approx(1.01, abs=0.01, rel=0.01)
    var_0 = rate_0.__hash__()
    assert var_0 == pytest.approx(1.01, abs=0.01, rel=0.01)
    rate_1 = module_0.Rate(percent_change=var_0)
    assert f"{type(rate_1).__module__}.{type(rate_1).__qualname__}" == "rate.Rate"
    assert rate_1.multiplier == pytest.approx(1.0101, abs=0.01, rel=0.01)
    var_1 = rate_1.__truediv__(rate_0)
    assert var_1 == pytest.approx(1.00009900990099, abs=0.01, rel=0.01)
    var_2 = var_1.__eq__(rate_0)
    var_3 = var_2.__gt__(bool_0)
    rate_0.of(tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_13():
    int_0 = -3458
    rate_0 = module_0.Rate(int_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier == -3458
    rate_0.__add__(rate_0)


@pytest.mark.xfail(strict=True)
def test_case_14():
    int_0 = -3449
    rate_0 = module_0.Rate(int_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier == -3449
    var_0 = rate_0.__ge__(int_0)
    assert var_0 is True
    var_1 = rate_0.__le__(int_0)
    assert var_1 is True
    var_2 = rate_0.__float__()
    assert var_2 == -3449
    var_3 = var_0.__ge__(var_1)
    assert var_3 is True
    var_4 = rate_0.__le__(var_0)
    assert var_4 is True
    var_3.apply_to(var_3)


def test_case_15():
    str_0 = "C{'Wl\"Q <W}@<{"
    with pytest.raises(ValueError):
        module_0.Rate(str_0)


@pytest.mark.xfail(strict=True)
def test_case_16():
    int_0 = -3449
    float_0 = 1833.79075
    rate_0 = module_0.Rate(percent_change=float_0)
    assert f"{type(rate_0).__module__}.{type(rate_0).__qualname__}" == "rate.Rate"
    assert rate_0.multiplier == pytest.approx(19.3379075, abs=0.01, rel=0.01)
    var_0 = rate_0.__ge__(int_0)
    assert var_0 is True
    none_type_0 = None
    rate_1 = module_0.Rate(float_0, percentage=none_type_0)
    assert f"{type(rate_1).__module__}.{type(rate_1).__qualname__}" == "rate.Rate"
    assert rate_1.multiplier == pytest.approx(1833.79075, abs=0.01, rel=0.01)
    var_1 = int_0.__ge__(rate_0)
    var_2 = var_1.__le__(var_1)
    var_2.__float__()
