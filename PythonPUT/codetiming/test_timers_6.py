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
    str_0 = "Sn:Llh$x`16{~b"
    timers_0.min(str_0)


def test_case_2():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    bool_0 = True
    none_type_0 = None
    none_type_1 = timers_0.add(none_type_0, bool_0)
    assert len(timers_0) == 1
    float_0 = timers_0.median(none_type_1)
    assert float_0 is True
    float_1 = timers_0.max(none_type_0)
    assert float_1 is True


@pytest.mark.xfail(strict=True)
def test_case_3():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    none_type_0 = timers_0.clear()
    str_0 = '+.RU9  N\r$u"tts^B'
    bytes_0 = b"+\x1a\x0c\xdb\xe5\xf2\x81\xa2\xd2\x9e=\xdc>\x10\x88\x8etq"
    timers_0.__setitem__(bytes_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    none_type_0 = None
    timers_0.__setitem__(none_type_0, timers_0)


def test_case_5():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    bool_0 = True
    none_type_0 = None
    none_type_1 = timers_0.add(none_type_0, bool_0)
    assert len(timers_0) == 1
    float_0 = timers_0.median(none_type_1)
    assert float_0 is True
    float_1 = timers_0.mean(none_type_0)
    assert float_1 == 1


def test_case_6():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = 's!^PhwW"g){fMSROp~W'
    bool_0 = True
    none_type_0 = None
    none_type_1 = timers_0.add(none_type_0, bool_0)
    assert len(timers_0) == 1
    float_0 = timers_0.median(none_type_1)
    assert float_0 is True
    bool_1 = False
    none_type_2 = timers_0.add(str_0, bool_1)
    assert len(timers_0) == 2
    float_1 = timers_0.stdev(str_0)
    float_2 = timers_0.max(none_type_0)
    assert float_2 is True
    float_3 = timers_0.min(str_0)
    assert float_3 is False
    float_4 = timers_0.mean(none_type_0)
    assert float_4 == 1
    none_type_3 = timers_0.clear()
    assert len(timers_0) == 0
    var_0 = timers_0.copy()
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "timers.Timers"
    assert len(var_0) == 0
    with pytest.raises(KeyError):
        timers_0.stdev(str_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
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
    timers_1.median(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = '+.RU9  N\r$u"tts^B'
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    timers_0.count(str_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = 's!^PhwW"g){fM}SROp~W'
    bool_0 = True
    none_type_0 = timers_0.add(str_0, bool_0)
    assert len(timers_0) == 1
    float_0 = timers_0.total(str_0)
    assert float_0 == 1
    float_1 = timers_0.stdev(str_0)
    float_2 = timers_0.min(str_0)
    assert float_2 is True
    none_type_1 = timers_0.clear()
    assert len(timers_0) == 0
    timers_0.__setitem__(bool_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_10():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    none_type_0 = None
    int_0 = 635
    none_type_1 = timers_0.add(none_type_0, int_0)
    assert len(timers_0) == 1
    var_0 = timers_0.update()
    float_0 = timers_0.median(none_type_1)
    assert float_0 == 635
    bool_0 = False
    none_type_2 = timers_0.add(var_0, bool_0)
    float_1 = timers_0.stdev(var_0)
    assert float_1 == pytest.approx(449.01280605345767, abs=0.01, rel=0.01)
    float_2 = timers_0.max(none_type_0)
    assert float_2 == 635
    none_type_3 = timers_0.clear()
    assert len(timers_0) == 0
    var_1 = timers_0.copy()
    assert f"{type(var_1).__module__}.{type(var_1).__qualname__}" == "timers.Timers"
    assert len(var_1) == 0
    var_1.translate()