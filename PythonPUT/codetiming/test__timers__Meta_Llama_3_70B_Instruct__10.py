import collections
import statistics
import math
from typing import TYPE_CHECKING
import timers as module_0
from typing import Dict
import pytest
from typing import List
from typing import Callable
from typing import Any
def test_example_3hefcu9c():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer2', 30.0)
    assert timers.total('timer1') == 30.0


def test_example_afxvis5e():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer2', 30.0)
    assert timers.mean('timer1') == 15.0


def test_example_ax6a5vkd():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer2', 30.0)
    assert timers.median('timer1') == 15.0


def test_example_10s94zio():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer2', 30.0)
    assert timers.count('timer1') == 2


def test_example_aunrkvfr():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer2', 20.0)
    assert timers.min('timer1') == 10.0


def test_example_nm2ntn1g():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer2', 20.0)
    assert timers.max('timer2') == 20.0


def test_example_kkucnjug():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer2', 20.0)
    assert 'timer1' in timers.data


def test_example_vez7bm70():
    timers = module_0.Timers()
    assert len(timers.data) == 0


