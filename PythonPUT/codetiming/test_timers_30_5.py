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
    none_type_0 = None
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    timers_0.total(none_type_0)


def test_case_2():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "l?B>\rV3R1G~"
    with pytest.raises(KeyError):
        timers_0.stdev(str_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = ">k?fW\x0bll)ws"
    timers_0.add(str_0, timers_0)


def test_case_4():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    none_type_0 = timers_0.clear()


def test_case_5():
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
    with pytest.raises(TypeError):
        timers_1.__setitem__(timers_0, timers_1)


@pytest.mark.xfail(strict=True)
def test_case_6():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "gn_eJ'Ph=8\")2U`!+"
    timers_0.count(str_0)


def test_case_7():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    timers_1 = module_0.Timers(*timers_0)
    assert (
        f"{type(timers_1).__module__}.{type(timers_1).__qualname__}" == "timers.Timers"
    )
    assert len(timers_1) == 0
    str_0 = "gn_eJ'Ph=)\")2U`!+"
    int_0 = 1722
    none_type_0 = timers_0.add(str_0, int_0)
    assert len(timers_0) == 1
    float_0 = timers_0.stdev(str_0)
    float_1 = timers_0.max(str_0)
    assert float_1 == 1722


@pytest.mark.xfail(strict=True)
def test_case_8():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "PlKX["
    timers_0.mean(str_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    timers_1 = module_0.Timers(*timers_0)
    assert (
        f"{type(timers_1).__module__}.{type(timers_1).__qualname__}" == "timers.Timers"
    )
    assert len(timers_1) == 0
    var_0 = timers_0.items()
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "collections.abc.ItemsView"
    )
    assert len(var_0) == 0
    str_0 = "7$Bb2R'(3lMjhSFgPb&B"
    int_0 = 1718
    none_type_0 = timers_0.add(str_0, int_0)
    assert len(timers_0) == 1
    assert len(var_0) == 1
    float_0 = timers_0.median(str_0)
    assert float_0 == 1718
    timers_1.median(none_type_0)


def test_case_10():
    str_0 = "\nwk"
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    int_0 = 1722
    none_type_0 = timers_0.add(str_0, int_0)
    assert len(timers_0) == 1
    float_0 = timers_0.min(str_0)
    assert float_0 == 1722


def test_case_11():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    timers_1 = module_0.Timers(*timers_0)
    assert (
        f"{type(timers_1).__module__}.{type(timers_1).__qualname__}" == "timers.Timers"
    )
    assert len(timers_1) == 0
    str_0 = "gn_eJ'Ph=)\")2U`!+"
    int_0 = 1722
    none_type_0 = timers_0.add(str_0, int_0)
    assert len(timers_0) == 1
    float_0 = timers_0.stdev(str_0)
    var_0 = timers_0.get(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_12():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    none_type_0 = timers_0.clear()
    str_0 = "gn_eJ'Ph=)\")2U`!+"
    int_0 = 1722
    none_type_1 = timers_0.add(str_0, int_0)
    assert len(timers_0) == 1
    int_1 = -2677
    none_type_2 = timers_0.add(str_0, int_1)
    float_0 = timers_0.stdev(str_0)
    assert float_0 == pytest.approx(3110.5627304396226, abs=0.01, rel=0.01)
    float_1 = timers_0.median(str_0)
    assert float_1 == pytest.approx(-477.5, abs=0.01, rel=0.01)
    timers_0.stdev(timers_0)
