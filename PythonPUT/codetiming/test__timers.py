# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import _timers as module_0


def test_case_0():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "_timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False


@pytest.mark.xfail(strict=True)
def test_case_1():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "_timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "*\x0b\x0basA@FEgOX"
    timers_0.median(str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "_timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = ""
    none_type_0 = timers_0.clear()
    int_0 = -174
    var_0 = timers_0.__iter__()
    none_type_1 = timers_0.add(str_0, int_0)
    assert len(timers_0) == 1
    float_0 = timers_0.min(str_0)
    assert float_0 == -174
    float_1 = timers_0.stdev(str_0)
    float_2 = timers_0.median(str_0)
    assert float_2 == -174
    float_3 = timers_0.max(str_0)
    assert float_3 == -174
    var_0.mean(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = ":vQ)VH9zTtx"
    str_1 = "y"
    str_2 = ">|"
    dict_0 = {str_0: str_0, str_0: str_0, str_1: str_1, str_2: str_2}
    module_0.Timers(**dict_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    list_0 = []
    timers_0 = module_0.Timers(*list_0)
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "_timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    none_type_0 = None
    timers_0.count(none_type_0)


def test_case_5():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "_timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "X"
    int_0 = -166
    none_type_0 = None
    var_0 = timers_0.__contains__(none_type_0)
    assert var_0 is False
    none_type_1 = timers_0.add(str_0, int_0)
    assert len(timers_0) == 1
    float_0 = timers_0.stdev(str_0)
    float_1 = timers_0.count(str_0)
    assert float_1 == 1
    float_2 = timers_0.total(str_0)
    assert float_2 == -166


@pytest.mark.xfail(strict=True)
def test_case_6():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "_timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = ""
    timers_0.min(str_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "_timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "J%1="
    timers_0.mean(str_0)


def test_case_8():
    str_0 = "yGcOHFn:6? "
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "_timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    with pytest.raises(KeyError):
        timers_0.stdev(str_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "_timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    timers_0.max(timers_0)


def test_case_10():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "_timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = ""
    int_0 = 131
    none_type_0 = timers_0.add(str_0, int_0)
    assert len(timers_0) == 1
    float_0 = timers_0.mean(str_0)
    assert float_0 == 131


def test_case_11():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "_timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = ""
    int_0 = -166
    none_type_0 = timers_0.add(str_0, int_0)
    assert len(timers_0) == 1
    float_0 = timers_0.median(str_0)
    assert float_0 == -166
    float_1 = timers_0.max(str_0)
    assert float_1 == -166
    float_2 = timers_0.mean(str_0)
    assert float_2 == -166


@pytest.mark.xfail(strict=True)
def test_case_12():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "_timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "X"
    int_0 = -166
    none_type_0 = timers_0.add(str_0, int_0)
    assert len(timers_0) == 1
    float_0 = timers_0.stdev(str_0)
    float_1 = timers_0.count(str_0)
    assert float_1 == 1
    none_type_1 = None
    timers_0.mean(none_type_1)


@pytest.mark.xfail(strict=True)
def test_case_13():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "_timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = ""
    int_0 = -174
    none_type_0 = timers_0.add(str_0, int_0)
    assert len(timers_0) == 1
    float_0 = timers_0.median(str_0)
    assert float_0 == -174
    str_1 = "E3"
    timers_0.count(str_1)


@pytest.mark.xfail(strict=True)
def test_case_14():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "_timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = ""
    int_0 = -174
    none_type_0 = timers_0.add(str_0, int_0)
    assert len(timers_0) == 1
    none_type_1 = timers_0.add(str_0, int_0)
    float_0 = timers_0.min(str_0)
    assert float_0 == -174
    float_1 = timers_0.stdev(str_0)
    assert float_1 == pytest.approx(0.0, abs=0.01, rel=0.01)
    float_2 = timers_0.median(str_0)
    assert float_2 == pytest.approx(-174.0, abs=0.01, rel=0.01)
    float_3 = timers_0.max(str_0)
    assert float_3 == -174
    var_0 = timers_0.__contains__(none_type_1)
    assert var_0 is False
    float_4 = timers_0.mean(str_0)
    assert float_4 == -174
    str_1 = "E3"
    timers_0.count(str_1)


@pytest.mark.xfail(strict=True)
def test_case_15():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "_timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = ""
    int_0 = -174
    none_type_0 = timers_0.add(str_0, int_0)
    assert len(timers_0) == 1
    float_0 = timers_0.min(str_0)
    assert float_0 == -174
    str_1 = "E3"
    timers_0.count(str_1)