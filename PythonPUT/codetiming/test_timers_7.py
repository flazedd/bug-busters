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
    none_type_0 = None
    timers_0.total(none_type_0)


def test_case_2():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    none_type_0 = None
    with pytest.raises(KeyError):
        timers_0.stdev(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "r"
    str_1 = "@#tt9i<\t-\\"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_1: str_1}
    module_0.Timers(**dict_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = ""
    int_0 = -3082
    none_type_0 = timers_0.add(str_0, int_0)
    assert len(timers_0) == 1
    float_0 = timers_0.max(str_0)
    assert float_0 == -3082
    float_1 = timers_0.median(str_0)
    assert float_1 == -3082
    float_2 = timers_0.mean(str_0)
    assert float_2 == -3082
    float_3 = timers_0.min(str_0)
    assert float_3 == -3082
    timers_0.max(float_2)


@pytest.mark.xfail(strict=True)
def test_case_5():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "k(=8BR\x0b\\Al7fz"
    timers_0.mean(str_0)


def test_case_6():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = ""
    int_0 = -3082
    none_type_0 = timers_0.add(str_0, int_0)
    assert len(timers_0) == 1
    float_0 = timers_0.median(str_0)
    assert float_0 == -3082
    float_1 = timers_0.mean(str_0)
    assert float_1 == -3082
    var_0 = timers_0.__or__(float_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    bool_0 = True
    timers_0.count(bool_0)


def test_case_8():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = ""
    int_0 = -3082
    none_type_0 = timers_0.add(str_0, int_0)
    assert len(timers_0) == 1
    float_0 = timers_0.median(str_0)
    assert float_0 == -3082
    float_1 = timers_0.mean(str_0)
    assert float_1 == -3082
    str_1 = ""
    float_2 = timers_0.min(str_1)
    assert float_2 == -3082
    var_0 = timers_0.__or__(float_0)


def test_case_9():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "k}=L2n\x0bG\n:Q"
    none_type_0 = timers_0.clear()
    int_0 = -4868
    with pytest.raises(TypeError):
        timers_0.__setitem__(str_0, int_0)


def test_case_10():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = ""
    int_0 = -3082
    none_type_0 = timers_0.add(str_0, int_0)
    assert len(timers_0) == 1
    float_0 = timers_0.stdev(str_0)
    var_0 = timers_0.__or__(str_0)
    float_1 = timers_0.stdev(str_0)


def test_case_11():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = ""
    int_0 = 516
    none_type_0 = timers_0.add(str_0, int_0)
    assert len(timers_0) == 1
    int_1 = -3082
    none_type_1 = timers_0.add(str_0, int_1)
    bool_0 = True
    float_0 = timers_0.mean(str_0)
    assert float_0 == -1283
    float_1 = timers_0.stdev(str_0)
    assert float_1 == pytest.approx(2544.170198709198, abs=0.01, rel=0.01)
    with pytest.raises(TypeError):
        timers_0.__setitem__(str_0, bool_0)
