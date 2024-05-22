import statistics
import timers as module_0
import math
import collections
import pytest
from typing import TYPE_CHECKING, Any, Callable, Dict, List
def test_timers():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer2', 30.0)


def test_timers_count():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer1', 30.0)


