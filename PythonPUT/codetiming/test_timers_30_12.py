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
    str_0 = "awe1"
    timers_0.max(str_0)


def test_case_2():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "TyU\x0c8I/~3BaFz9"
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
    str_0 = "Vhf!8Yb{K 8}Y8"
    int_0 = 720
    none_type_0 = timers_0.add(str_0, int_0)
    assert len(timers_0) == 1
    timers_0.mean(timers_0)


def test_case_4():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "N\t'y3;d/U"
    var_0 = timers_0.clear()
    float_0 = 526.0
    none_type_0 = timers_0.add(str_0, float_0)
    assert len(timers_0) == 1
    float_1 = timers_0.stdev(str_0)


def test_case_5():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    with pytest.raises(TypeError):
        timers_0.__setitem__(timers_0, timers_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    var_0 = timers_0.__copy__()
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "timers.Timers"
    assert len(var_0) == 0
    str_0 = "'BXtr"
    var_0.count(str_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    timers_0.total(timers_0)


def test_case_8():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "N\t'y3;d/U"
    float_0 = 526.0
    none_type_0 = timers_0.add(str_0, float_0)
    assert len(timers_0) == 1
    float_1 = timers_0.median(str_0)
    assert float_1 == pytest.approx(526.0, abs=0.01, rel=0.01)


@pytest.mark.xfail(strict=True)
def test_case_9():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "VhJq\\DR#JdJv4"
    timers_0.min(str_0)


def test_case_10():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "3AM\t'~Z&\x0b]U"
    int_0 = -73
    none_type_0 = timers_0.add(str_0, int_0)
    assert len(timers_0) == 1
    float_0 = timers_0.stdev(str_0)


def test_case_11():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "N'y;Md/U"
    float_0 = 527.8139747549037
    none_type_0 = timers_0.add(str_0, float_0)
    assert len(timers_0) == 1
    float_1 = timers_0.max(str_0)
    assert float_1 == pytest.approx(527.8139747549037, abs=0.01, rel=0.01)


def test_case_12():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "N'y;Md/U"
    float_0 = 527.8139747549037
    none_type_0 = timers_0.add(str_0, float_0)
    assert len(timers_0) == 1
    float_1 = timers_0.mean(str_0)
    assert float_1 == pytest.approx(527.8139747549037, abs=0.01, rel=0.01)


def test_case_13():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "3AM\t'~Z&\x0b]U)&"
    int_0 = 2963
    str_1 = "3AM\t'~Z&\x0b]U)&"
    var_0 = timers_0.__copy__()
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "timers.Timers"
    assert len(var_0) == 0
    none_type_0 = var_0.add(str_0, int_0)
    assert len(var_0) == 1
    float_0 = timers_0.min(str_1)
    assert float_0 == 2963


@pytest.mark.xfail(strict=True)
def test_case_14():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "N\t'y3;d/U"
    float_0 = 527.8139747549037
    none_type_0 = timers_0.add(str_0, float_0)
    assert len(timers_0) == 1
    float_1 = timers_0.median(str_0)
    assert float_1 == pytest.approx(527.8139747549037, abs=0.01, rel=0.01)
    int_0 = 1
    none_type_1 = timers_0.add(str_0, int_0)
    float_2 = timers_0.stdev(str_0)
    assert float_2 == pytest.approx(372.51373397303104, abs=0.01, rel=0.01)
    float_3 = timers_0.mean(str_0)
    assert float_3 == pytest.approx(264.40698737745186, abs=0.01, rel=0.01)
    timers_0.min(float_0)
