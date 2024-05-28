import collections
import statistics
from typing import Callable
from typing import Any
from typing import Dict
from typing import List
from typing import TYPE_CHECKING
import timers as module_0
import math
import pytest
def test_example():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer2', 30.0)
    assert timers.total('timer1') == 30.0


def test_example_p6lun2mq():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer2', 30.0)
    assert timers.count('timer1') == 2


def test_example_pimkziy1():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer2', 30.0)
    assert timers.mean('timer1') == 15.0


def test_example_uotjlzlq():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer2', 30.0)
    assert timers.max('timer1') == 20.0


def test_example_hfms5lgs():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer2', 30.0)
    assert timers.median('timer1') == 15.0


def test_example_yy6beh2d():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer2', 30.0)
    timers.clear()
    assert len(timers.data) == 0


def test_example_83e7cqoh():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer2', 20.0)
    assert timers.total('timer1') == 10.0


def test_example_du9cmth2():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer2', 30.0)
    assert timers.min('timer1') == 10.0


