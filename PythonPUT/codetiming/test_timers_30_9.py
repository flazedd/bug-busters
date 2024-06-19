# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import timers as module_0
import collections as module_1


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
    str_0 = "5= >fUJ\tp`\x0c5w1Vo1"
    timers_0.min(str_0)


def test_case_2():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "b@"
    with pytest.raises(KeyError):
        timers_0.stdev(str_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "Q;'9.xGphrE\x0c=k"
    str_1 = ")f6qG,a;N<A$L"
    str_2 = "~!U$5l"
    dict_0 = {str_0: str_0, str_0: str_0, str_1: str_0, str_2: str_0}
    module_0.Timers(**dict_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "9w4v;pgNNRmv8B5VK"
    timers_0.count(str_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "9?QY .C/6k{R"
    timers_0.total(str_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "vN{Qt[c|D=0yps:\t~Y/U"
    var_0 = module_1._OrderedDictValuesView(str_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "collections._OrderedDictValuesView"
    )
    assert len(var_0) == 20
    timers_0.max(str_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    timers_0.mean(timers_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = "Hzd5RZ%"
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    timers_0.median(str_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    none_type_0 = timers_0.clear()
    str_0 = "9?QY .C/6k{R"
    var_0 = timers_0.__len__()
    assert var_0 == 0
    timers_0.median(str_0)


def test_case_10():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "\x0cWsd#QG}':=dK\x0bvdr{"
    float_0 = -1823.73
    none_type_0 = timers_0.add(str_0, float_0)
    assert len(timers_0) == 1
    float_1 = timers_0.stdev(str_0)


@pytest.mark.xfail(strict=True)
def test_case_11():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "\x0cWsd#QG}':=dK\x0bvdr{"
    float_0 = -1823.73
    none_type_0 = timers_0.add(str_0, float_0)
    assert len(timers_0) == 1
    float_1 = timers_0.stdev(str_0)
    float_2 = timers_0.median(str_0)
    assert float_2 == pytest.approx(-1823.73, abs=0.01, rel=0.01)
    timers_0.median(none_type_0)


def test_case_12():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "\x0cWsd#QG}':=dK\x0bvdr{"
    float_0 = -1823.73
    none_type_0 = timers_0.add(str_0, float_0)
    assert len(timers_0) == 1
    float_1 = timers_0.stdev(str_0)
    float_2 = timers_0.mean(str_0)
    assert float_2 == pytest.approx(-1823.73, abs=0.01, rel=0.01)
    float_3 = timers_0.median(str_0)
    assert float_3 == pytest.approx(-1823.73, abs=0.01, rel=0.01)


@pytest.mark.xfail(strict=True)
def test_case_13():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "\x0cWsd#Q}':=dKvdr{"
    float_0 = -1823.73
    none_type_0 = timers_0.add(str_0, float_0)
    assert len(timers_0) == 1
    float_1 = timers_0.stdev(str_0)
    float_2 = timers_0.max(str_0)
    assert float_2 == pytest.approx(-1823.73, abs=0.01, rel=0.01)
    float_3 = timers_0.median(str_0)
    assert float_3 == pytest.approx(-1823.73, abs=0.01, rel=0.01)
    timers_0.__ior__(float_2)


@pytest.mark.xfail(strict=True)
def test_case_14():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "\x0cW2d#Q}':=dKvdr{"
    float_0 = -1823.73
    none_type_0 = timers_0.add(str_0, float_0)
    assert len(timers_0) == 1
    float_1 = timers_0.min(str_0)
    assert float_1 == pytest.approx(-1823.73, abs=0.01, rel=0.01)
    float_2 = timers_0.mean(str_0)
    assert float_2 == pytest.approx(-1823.73, abs=0.01, rel=0.01)
    float_3 = timers_0.max(str_0)
    assert float_3 == pytest.approx(-1823.73, abs=0.01, rel=0.01)
    float_4 = timers_0.mean(str_0)
    assert float_4 == pytest.approx(-1823.73, abs=0.01, rel=0.01)
    timers_0.__ior__(str_0)


@pytest.mark.xfail(strict=True)
def test_case_15():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "\x0cWsd#Q}':=dKvdr{"
    float_0 = -1823.73
    bool_0 = False
    none_type_0 = timers_0.add(str_0, bool_0)
    assert len(timers_0) == 1
    none_type_1 = timers_0.add(str_0, float_0)
    var_0 = timers_0.update()
    float_1 = timers_0.stdev(str_0)
    assert float_1 == pytest.approx(1289.5718500533424, abs=0.01, rel=0.01)
    float_2 = timers_0.min(str_0)
    assert float_2 == pytest.approx(-1823.73, abs=0.01, rel=0.01)
    float_3 = timers_0.mean(str_0)
    assert float_3 == pytest.approx(-911.865, abs=0.01, rel=0.01)
    float_4 = timers_0.max(str_0)
    assert float_4 is False
    float_5 = timers_0.median(str_0)
    assert float_5 == pytest.approx(-911.865, abs=0.01, rel=0.01)
    timers_0.min(none_type_1)
