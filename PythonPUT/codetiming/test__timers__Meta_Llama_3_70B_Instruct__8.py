from typing import Any
import math
from typing import TYPE_CHECKING
from typing import Dict
import timers as module_0
import statistics
import pytest
from typing import List
import collections
from typing import Callable
def test_example_ndveqoo3():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer2', 30.0)
    assert timers.mean('timer1') == 15.0


def test_example_dm691xsp():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer2', 30.0)
    assert timers.max('timer2') == 30.0


def test_example_dhpmoe36():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer1', 30.0)
    assert timers.count('timer1') == 3


def test_example_5p6s8xfs():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer2', 20.0)
    assert timers.total('timer1') == 10.0


def test_example_bplpim72():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer2', 20.0)
    assert 'timer1' in timers.data


def test_example_9g96asa8():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer1', 30.0)
    timers.clear()
    assert len(timers.data) == 0


def test_example_m2yw0yv9():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer2', 20.0)
    assert timers.median('timer2') == 20.0


def test_example_7sigxsgm():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer1', 30.0)
    assert timers.min('timer1') == 10.0


