import pytest

from _timers import Timers
import statistics
import math

def test_timers():
    timers = Timers()
    timers.add("timer1", 1.5)
    timers.add("timer1", 2.5)
    timers.add("timer2", 3.0)

    assert timers.count("timer1") == 2
    assert math.isclose(timers.total("timer1"), 4.0)
    assert math.isclose(timers.min("timer1"), 1.5)
    assert math.isclose(timers.max("timer1"), 2.5)
    assert math.isclose(timers.mean("timer1"), 2.0)
    assert math.isclose(timers.median("timer1"), 2.0)
    assert math.isclose(timers.stdev("timer1"), math.sqrt(((1.5 - 2.0) ** 2 + (2.5 - 2.0) ** 2) / 2))

    assert timers.count("timer2") == 1
    assert math.isclose(timers.total("timer2"), 3.0)
    assert math.isclose(timers.min("timer2"), 3.0)
    assert math.isclose(timers.max("timer2"), 3.0)
    assert math.isclose(timers.mean("timer2"), 3.0)
    assert math.isclose(timers.median("timer2"), 3.0)
    assert math.isnan(timers.stdev("timer2"))

    assert len(timers) == 2
    assert "timer1" in timers
    assert "timer3" not in timers

    with pytest.raises(TypeError):
        timers["timer1"] = 10.0

    timers.clear()
    assert len(timers) == 0
    assert "timer1" not in timers