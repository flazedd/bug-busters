import timers as module_0
import statistics
from typing import List
import pytest
from typing import TYPE_CHECKING
from typing import Any
import collections
from typing import Callable
import math
from typing import Dict
def test_example_5tsfd8xg():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer2', 30.0)
    assert timers.mean('timer1') == 15.0


def test_example_wwagusyi():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer1', 30.0)
    assert timers.max('timer1') == 30.0


