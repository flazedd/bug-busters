import collections
import math
import pytest
import statistics
from typing import TYPE_CHECKING, Any, Callable, Dict, List
from timers import *
def test_timers_mean():
    timers = Timers()
    timers.add('timer1', 1.0)
    timers.add('timer1', 2.0)
    timers.add('timer1', 3.0)
def test_timers_stdev():
    timers = Timers()
    timers.add('timer1', 1.0)
    timers.add('timer1', 1.0)
    timers.add('timer1', 1.0)
