import statistics
from typing import Dict
from typing import List
from typing import Callable
import math
import timers as module_0
from typing import Any
from typing import TYPE_CHECKING
import collections
import pytest
def test_example_n33wtwur():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer2', 30.0)
    assert timers.total('timer1') == 30.0


def test_example_vw9sezkl():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer2', 30.0)
    assert timers.mean('timer1') == 15.0


def test_example_bbdtek7v():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer2', 30.0)
    assert timers.median('timer1') == 15.0


def test_example_dns18orl():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer2', 30.0)
    timers.clear()
    assert len(timers.data) == 0


def test_example_346738y4():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer2', 30.0)
    assert timers.count('timer1') == 2


def test_example_1hhjeezd():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer2', 20.0)
    assert timers.min('timer1') == 10.0


def test_example_pe5xq70p():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer2', 20.0)
    assert timers.max('timer2') == 20.0


def test_example_tf5f8nm9():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer2', 20.0)
    assert 'timer1' in timers.data
    assert 'timer2' in timers.data


