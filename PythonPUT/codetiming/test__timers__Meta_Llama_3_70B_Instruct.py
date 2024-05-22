from typing import TYPE_CHECKING, Any, Callable, Dict, List
import collections
from timers import *
import math
import pytest
import statistics
def test_timers():
    timers = Timers()
    timers.add("timer1", 10.0)
    timers.add("timer1", 20.0)
    timers.add("timer2", 30.0)

def test_timers_count():
    timers = Timers()
    timers.add("timer1", 10.0)
    timers.add("timer1", 20.0)
    timers.add("timer1", 30.0)

