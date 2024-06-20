from typing import Callable
import pytest
from typing import List
from typing import TYPE_CHECKING
import math
from typing import Any
import timers as module_0
from typing import Dict
import statistics
import collections
def test_example_p3qwsblg():
    timers = module_0.Timers()
    timers.add('timer1', 1.0)
    timers.add('timer1', 2.0)
    timers.add('timer2', 3.0)
    assert timers.count('timer1') == 2


def test_example_qwq9xb56():
    timers = module_0.Timers()
    timers.add('timer1', 1.0)
    timers.add('timer1', 2.0)
    timers.add('timer2', 3.0)
    assert timers.mean('timer1') == 1.5


def test_example_3ohl0ukp():
    timers = module_0.Timers()
    timers.add('timer1', 1.0)
    timers.add('timer1', 2.0)
    timers.add('timer2', 3.0)
    assert timers.total('timer1') == 3.0


def test_example_36byw259():
    timers = module_0.Timers()
    timers.add('timer1', 1.0)
    timers.add('timer1', 2.0)
    timers.add('timer2', 3.0)
    timers.clear()
    assert len(timers.data) == 0


def test_example_y3xhjh9u():
    timers = module_0.Timers()
    timers.add('timer1', 1.0)
    timers.add('timer1', 2.0)
    timers.add('timer2', 3.0)
    assert timers.max('timer2') == 3.0


def test_example_t1sa4m8h():
    timers = module_0.Timers()
    timers.add('timer1', 1.0)
    timers.add('timer1', 2.0)
    timers.add('timer2', 3.0)
    assert timers.median('timer1') == 1.5


def test_example_dpsbgq7s():
    timers = module_0.Timers()
    timers.add('timer1', 1.0)
    timers.add('timer2', 2.0)
    assert 'timer1' in timers.data
    assert 'timer2' in timers.data


def test_example_v4y9dx4s():
    timers = module_0.Timers()
    timers.add('timer1', 1.0)
    timers.add('timer1', 2.0)
    timers.add('timer2', 3.0)
    assert timers.count('timer1') == 2
    assert timers.count('timer2') == 1


