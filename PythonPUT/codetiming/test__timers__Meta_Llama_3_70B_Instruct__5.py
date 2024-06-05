import collections
from typing import Any
import timers as module_0
from typing import List
import pytest
import statistics
from typing import TYPE_CHECKING
from typing import Callable
import math
from typing import Dict
def test_example_es2sqrw1():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer2', 30.0)
    assert timers.total('timer1') == 30.0





def test_example_fo29hhii():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer2', 30.0)
    assert timers.mean('timer1') == 15.0





def test_example_z1ji0jvp():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer2', 30.0)
    assert timers.total('timer1') == 30.0


def test_example_6iex75sh():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer2', 30.0)
    assert timers.mean('timer1') == 15.0


def test_example_o8ed7n3t():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer2', 20.0)
    assert timers.count('timer1') == 1


def test_example_4mfsk0yn():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer1', 30.0)
    assert timers.median('timer1') == 20.0


def test_example_jp2uy95e():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer2', 20.0)
    assert 'timer1' in timers.data


def test_example_nobw9doi():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.clear()
    assert len(timers.data) == 0


