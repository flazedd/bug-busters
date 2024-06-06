from typing import Any
import pytest
from typing import Callable
from typing import List
import timers as module_0
import math
import collections
import statistics
from typing import TYPE_CHECKING
from typing import Dict
def test_example_fl7p37oc():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer2', 30.0)
    assert timers.total('timer1') == 30.0


def test_example_jqkub4zf():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer2', 30.0)
    assert timers.mean('timer1') == 15.0


def test_example_k2kc0nm3():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer2', 30.0)
    assert timers.count('timer1') == 2


def test_example_t8ey174i():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer2', 30.0)
    assert timers.max('timer1') == 20.0


def test_example_jn8trjnq():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer2', 30.0)
    timers.clear()
    assert len(timers.data) == 0


def test_example_b3yqcird():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    assert timers.median('timer1') == 15.0


def test_example_khkum35q():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    assert timers.min('timer1') == 10.0


def test_example_20dhl1oj():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer2', 20.0)
    assert 'timer1' in timers.data


