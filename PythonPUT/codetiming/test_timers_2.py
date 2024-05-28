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
    str_0 = "1<\rED5"
    timers_0.max(str_0)


def test_case_2():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    none_type_0 = timers_0.clear()
    str_0 = ' xJ."%<SblPq'
    with pytest.raises(KeyError):
        timers_0.stdev(str_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "_j`b}"
    str_1 = " "
    dict_0 = {str_0: str_0, str_1: str_0, str_0: str_1, str_1: str_1}
    module_0.Timers(**dict_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "Gki'E*LE\x0b4\x0c2g\\H\""
    timers_0.count(str_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "{*$qS9,=.SMuPHLdyv9"
    timers_0.min(str_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    none_type_0 = None
    timers_0.mean(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    float_0 = 1912.44980195385
    str_0 = "@38oE+e>+E"
    none_type_0 = timers_0.add(str_0, float_0)
    assert len(timers_0) == 1
    float_1 = timers_0.median(str_0)
    assert float_1 == pytest.approx(1912.44980195385, abs=0.01, rel=0.01)
    timers_1 = module_0.Timers()
    assert (
        f"{type(timers_1).__module__}.{type(timers_1).__qualname__}" == "timers.Timers"
    )
    assert len(timers_1) == 0
    float_2 = timers_1.keys()
    assert (
        f"{type(float_2).__module__}.{type(float_2).__qualname__}"
        == "collections.abc.KeysView"
    )
    assert len(float_2) == 0
    timers_0.__contains__(float_2)


def test_case_8():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = 'Y xJ."%<YSblPq^'
    with pytest.raises(KeyError):
        timers_0.stdev(str_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    timers_0.total(timers_0)


@pytest.mark.xfail(strict=True)
def test_case_10():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    float_0 = 623.2220661983096
    float_1 = timers_0.copy()
    assert f"{type(float_1).__module__}.{type(float_1).__qualname__}" == "timers.Timers"
    assert len(float_1) == 0
    timers_0.add(timers_0, float_0)


def test_case_11():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    float_0 = 1882.91
    str_0 = "Gki'E*LE\x0b4\x0c2g\\H\""
    none_type_0 = timers_0.add(str_0, float_0)
    assert len(timers_0) == 1
    float_1 = timers_0.stdev(str_0)
    none_type_1 = timers_0.add(str_0, float_1)


@pytest.mark.xfail(strict=True)
def test_case_12():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    float_0 = 1882.91
    str_0 = "Gki'E*LE\x0b4\x0c2g\\H\""
    none_type_0 = timers_0.add(str_0, float_0)
    assert len(timers_0) == 1
    str_1 = "LIu\\:\x0cr*'S"
    float_1 = timers_0.stdev(str_0)
    timers_0.apply(str_1, str_0)


def test_case_13():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    bool_0 = False
    str_0 = "Gki'E*LE\x0b4\x0c2g\\H\""
    none_type_0 = timers_0.add(str_0, bool_0)
    assert len(timers_0) == 1
    float_0 = timers_0.mean(str_0)
    assert float_0 == 0
    float_1 = timers_0.min(str_0)
    assert float_1 is False
    float_2 = timers_0.stdev(str_0)
    float_3 = timers_0.max(str_0)
    assert float_3 is False
    float_4 = timers_0.median(str_0)
    assert float_4 is False


def test_case_14():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    str_0 = "R4Sam|:J'hzJ*P\tM"
    bool_0 = False
    none_type_0 = timers_0.add(str_0, bool_0)
    assert len(timers_0) == 1
    str_1 = "Gki'E*LE\x0b4\x0c2g\\H\""
    none_type_1 = timers_0.add(str_1, bool_0)
    assert len(timers_0) == 2
    float_0 = timers_0.mean(str_1)
    assert float_0 == 0
    float_1 = timers_0.stdev(str_1)
    float_2 = timers_0.max(str_0)
    assert float_2 is False


def test_case_15():
    timers_0 = module_0.Timers()
    assert (
        f"{type(timers_0).__module__}.{type(timers_0).__qualname__}" == "timers.Timers"
    )
    assert len(timers_0) == 0
    assert module_0.TYPE_CHECKING is False
    float_0 = 1882.91
    str_0 = 'u"W#x\x0bc?)\x0cY'
    bool_0 = False
    none_type_0 = timers_0.add(str_0, bool_0)
    assert len(timers_0) == 1
    none_type_1 = timers_0.add(str_0, float_0)
    float_1 = timers_0.min(str_0)
    assert float_1 is False
    str_1 = "LIu\\:\x0cr*'S"
    float_2 = timers_0.stdev(str_0)
    assert float_2 == pytest.approx(1331.4184293639623, abs=0.01, rel=0.01)
    float_3 = timers_0.max(str_0)
    assert float_3 == pytest.approx(1882.91, abs=0.01, rel=0.01)
    float_4 = timers_0.median(str_0)
    assert float_4 == pytest.approx(941.455, abs=0.01, rel=0.01)
    int_0 = -1743
    with pytest.raises(TypeError):
        timers_0.__setitem__(str_1, int_0)
