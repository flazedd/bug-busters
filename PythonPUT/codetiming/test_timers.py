# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import timers as module_0


def test_case_0():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False


@pytest.mark.xfail(strict=True)
def test_case_1():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "`N|\\5xp30rEh\t5r"
    timers_0.max(str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    timers_1 = module_0.Timers()
    assert (
        f"{type(timers_1).__module__}.{type(timers_1).__qualname__}" == "timers.Timers"
    )
    assert len(timers_1) == 0
    none_type_0 = None
    str_0 = "\\a$G\\a\\LjnxczmozF"
    bool_0 = True
    none_type_1 = timers_0.add(str_0, bool_0)
    assert len(timers_0) == 1
    timers_1.__setitem__(none_type_0, timers_1)


@pytest.mark.xfail(strict=True)
def test_case_3():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    none_type_0 = timers_0.clear()
    str_0 = "bu@{UntkTU|^"
    timers_0.median(str_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "z6+Q%v\t4|I6q}~Z\n4."
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    module_0.Timers(**dict_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "'qpwhe"
    bool_0 = True
    none_type_0 = timers_0.add(bool_0, bool_0)
    assert len(timers_0) == 1
    none_type_1 = timers_0.add(str_0, bool_0)
    assert len(timers_0) == 2
    float_0 = timers_0.mean(str_0)
    assert float_0 == 1
    float_1 = timers_0.min(str_0)
    assert float_1 is True
    timers_1 = module_0.Timers()
    assert (
        f"{type(timers_1).__module__}.{type(timers_1).__qualname__}" == "timers.Timers"
    )
    assert len(timers_1) == 0
    float_2 = timers_0.median(float_1)
    assert float_2 is True
    str_1 = ")9{8TS94Ep\rD6v"
    timers_1.count(str_1)


@pytest.mark.xfail(strict=True)
def test_case_6():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    timers_0.max(timers_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    var_0 = timers_0.items()
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "collections.abc.ItemsView"
    )
    assert len(var_0) == 0
    str_0 = "`N|\\5xp30rEh\t5r"
    timers_0.median(str_0)


def test_case_8():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "'qpwhe"
    bool_0 = True
    none_type_0 = timers_0.add(bool_0, bool_0)
    assert len(timers_0) == 1
    none_type_1 = timers_0.add(str_0, bool_0)
    assert len(timers_0) == 2
    var_0 = timers_0.popitem()
    assert len(timers_0) == 1
    float_0 = timers_0.mean(str_0)
    assert float_0 == 1
    float_1 = timers_0.stdev(str_0)
    float_2 = timers_0.min(str_0)
    assert float_2 is True
    float_3 = timers_0.max(float_0)
    assert float_3 is True


@pytest.mark.xfail(strict=True)
def test_case_9():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    timers_0.total(timers_0)


def test_case_10():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "'qpwhe"
    bool_0 = True
    none_type_0 = timers_0.add(str_0, bool_0)
    assert len(timers_0) == 1
    float_0 = timers_0.stdev(str_0)
    float_1 = timers_0.min(str_0)
    assert float_1 is True


def test_case_11():
    str_0 = "MGEq9,qw`FzD"
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    with pytest.raises(KeyError):
        timers_0.stdev(str_0)


def test_case_12():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "'qpwhe"
    float_0 = 1262.63897
    none_type_0 = timers_0.add(str_0, float_0)
    assert len(timers_0) == 1
    bool_0 = True
    none_type_1 = timers_0.add(str_0, bool_0)
    float_1 = timers_0.stdev(str_0)
    assert float_1 == pytest.approx(892.1134710962111, abs=0.01, rel=0.01)
    float_2 = timers_0.min(str_0)
    assert float_2 is True
    str_1 = "jm~i]m]S8I{^I8*qkZz"
    with pytest.raises(TypeError):
        timers_0.__setitem__(str_1, str_0)
