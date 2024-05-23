import pytest
from typing import Callable
from typing import Dict
import math
import statistics
import collections
from typing import TYPE_CHECKING
from typing import List
from typing import Any
import timers as module_0
def test_example_bpi7swar():
    timers = module_0.Timers()
    timers.add('my_timer', 1.0)
    timers.add('my_timer', 2.0)
    timers.add('my_timer', 3.0)
    assert timers.mean('my_timer') == 2.0


def test_example_8a6imnt7():
    timers = module_0.Timers()
    timers.add('my_timer', 1.0)
    timers.add('my_timer', 2.0)
    timers.add('my_timer', 3.0)
    assert timers.count('my_timer') == 3


def test_example_p6z1d1wr():
    timers = module_0.Timers()
    timers.add('my_timer', 1.0)
    timers.add('my_timer', 2.0)
    timers.add('my_timer', 3.0)
    assert timers.max('my_timer') == 3.0


def test_example_o7i3o7ia():
    timers = module_0.Timers()
    timers.add('my_timer', 1.0)
    timers.add('my_timer', 2.0)
    timers.add('my_timer', 3.0)
    timers.clear()
    assert 'my_timer' not in timers._timings


def test_example_30zj49b8():
    timers = module_0.Timers()
    timers.add('my_timer', 1.0)
    timers.add('my_timer', 2.0)
    timers.add('my_timer', 3.0)
    assert math.isclose(timers.stdev('my_timer'), 1.0)


def test_example_xfxv9qub():
    timers = module_0.Timers()
    timers.add('my_timer', 1.0)
    timers.add('my_timer', 2.0)
    timers.add('my_timer', 3.0)
    assert timers.median('my_timer') == 2.0


def test_example_01lvh441():
    timers = module_0.Timers()
    timers.add('my_timer', 3.0)
    timers.add('my_timer', 2.0)
    timers.add('my_timer', 1.0)
    assert timers.min('my_timer') == 1.0


def test_example_bcg9nyw6():
    timers = module_0.Timers()
    timers.add('my_timer', 1.0)
    try:
        timers.total('non_existent_timer')
        assert False, 'Expected KeyError'
    except KeyError:
        pass


