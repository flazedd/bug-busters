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
    str_0 = ".E"
    timers_0.mean(str_0)


def test_case_2():
    none_type_0 = None
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    with pytest.raises(KeyError):
        timers_0.stdev(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = '"jZc_5%8x\tq#dvH)U%?'
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    none_type_0 = timers_0.clear()
    float_0 = -1455.169991
    none_type_1 = timers_0.add(str_0, float_0)
    assert len(timers_0) == 1
    float_1 = timers_0.median(str_0)
    assert float_1 == pytest.approx(-1455.169991, abs=0.01, rel=0.01)
    float_2 = timers_0.min(str_0)
    assert float_2 == pytest.approx(-1455.169991, abs=0.01, rel=0.01)
    float_3 = timers_0.max(str_0)
    assert float_3 == pytest.approx(-1455.169991, abs=0.01, rel=0.01)
    float_4 = timers_0.max(str_0)
    assert float_4 == pytest.approx(-1455.169991, abs=0.01, rel=0.01)
    timers_0.count(none_type_1)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "^0TI\x0cY"
    str_1 = ".3U="
    dict_0 = {str_0: str_0, str_0: str_0, str_1: str_1}
    module_0.Timers(**dict_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "~k>{\r"
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    timers_0.count(str_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = '"jZc_5%8x\tq#dvH)U%?'
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    float_0 = -1455.169991
    none_type_0 = timers_0.add(str_0, float_0)
    assert len(timers_0) == 1
    float_1 = timers_0.min(str_0)
    assert float_1 == pytest.approx(-1455.169991, abs=0.01, rel=0.01)
    float_2 = timers_0.mean(str_0)
    assert float_2 == pytest.approx(-1455.169991, abs=0.01, rel=0.01)
    float_3 = timers_0.stdev(str_0)
    float_4 = timers_0.max(str_0)
    assert float_4 == pytest.approx(-1455.169991, abs=0.01, rel=0.01)
    timers_0.count(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = '"jZc_5%8x\tq#dvH)U%?'
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    timers_0.total(str_0)