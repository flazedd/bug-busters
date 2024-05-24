from typing import Dict
import statistics
from typing import Callable
from typing import Any
import timers as module_0
import collections
import pytest
import math
from typing import TYPE_CHECKING
from typing import List
def test_example_l2lr8nsi():
    timers = module_0.Timers()
    timers.add('timer1', 10)
    timers.add('timer1', 20)
    timers.add('timer2', 30)
    assert timers.mean('timer1') == 15.0


def test_example_06h7olx6():
    timers = module_0.Timers()
    timers.add('timer1', 10)
    timers.add('timer1', 20)
    timers.add('timer1', 30)
    assert timers.max('timer1') == 30.0


def test_example_2fae3xh9():
    timers = module_0.Timers()
    timers.add('timer1', 10)
    timers.add('timer1', 20)
    timers.add('timer1', 30)
    assert timers.count('timer1') == 3


def test_example_12h51twm():
    timers = module_0.Timers()
    timers.add('timer1', 10)
    timers.add('timer2', 20)
    assert 'timer1' in timers.data


def test_example_6xy2uaa7():
    timers = module_0.Timers()
    timers.add('timer1', 10)
    timers.add('timer1', 20)
    timers.clear()
    assert len(timers.data) == 0


def test_example_4ve7jtvn():
    timers = module_0.Timers()
    timers.add('timer1', 10)
    timers.add('timer1', 20)
    timers.add('timer2', 30)
    assert timers.total('timer1') == 30.0


def test_example_2wpogo01():
    timers = module_0.Timers()
    timers.add('timer1', 10)
    timers.add('timer1', 20)
    timers.add('timer2', 30)
    assert timers.median('timer1') == 15.0


def test_example_nas21lox():
    timers = module_0.Timers()
    timers.add('timer1', 10)
    assert timers.min('timer1') == 10.0


