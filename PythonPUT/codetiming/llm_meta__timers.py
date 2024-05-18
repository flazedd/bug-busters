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

def test_timers_mean():
    timers = Timers()
    timers.add("my_timer", 1.0)
    timers.add("my_timer", 2.0)
    timers.add("my_timer", 3.0)
    assert timers.mean("my_timer") == 2.0