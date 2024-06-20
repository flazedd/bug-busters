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
def test_example_5kj3znfl():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer2', 30.0)
    assert timers.total('timer1') == 30.0


def test_example_0e4ykss5():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer2', 30.0)
    assert timers.mean('timer1') == 15.0


def test_example_rdbkc0mz():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer1', 30.0)
    assert timers.max('timer1') == 30.0


def test_example_dxntrjm9():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer1', 30.0)
    assert timers.median('timer1') == 20.0


def test_example_035mc3jx():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer2', 20.0)
    assert timers.count('timer1') == 1


def test_example_qt2x4hsj():
    timers = module_0.Timers()
    assert len(timers) == 0


def test_example_82rhm0te():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer2', 20.0)
    assert 'timer1' in timers


def test_example_kpep5r7o():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer2', 20.0)
    assert list(timers.keys()) == ['timer1', 'timer2']


