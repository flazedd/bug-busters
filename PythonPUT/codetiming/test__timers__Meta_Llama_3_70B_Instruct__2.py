import collections
from typing import Any
import statistics
from typing import TYPE_CHECKING
import math
import timers as module_0
from typing import Dict
import pytest
from typing import Callable
from typing import List
def test_timers_mean_ll4vojz8():
    timers = module_0.Timers()
    timers.add('timer1', 1.0)
    timers.add('timer1', 2.0)
    timers.add('timer1', 3.0)
    assert timers.mean('timer1') == 2.0





def test_timers_clear_f6zzqh7f():
    timers = module_0.Timers()
    timers.add('timer1', 1.0)
    timers.add('timer2', 2.0)
    timers.clear()
    assert len(timers.data) == 0





def test_timers_count_h8i2489m():
    timers = module_0.Timers()
    timers.add('timer1', 1.0)
    timers.add('timer1', 2.0)
    timers.add('timer1', 3.0)
    assert timers.count('timer1') == 3





def test_timers_median_oq3c9n6z():
    timers = module_0.Timers()
    timers.add('timer1', 1.0)
    timers.add('timer1', 2.0)
    timers.add('timer1', 3.0)
    assert timers.median('timer1') == 2.0





def test_timers_max_6zaz47t4():
    timers = module_0.Timers()
    timers.add('timer1', 1.0)
    timers.add('timer1', 2.0)
    timers.add('timer1', 3.0)
    assert timers.max('timer1') == 3.0





def test_timers_min_78e5n301():
    timers = module_0.Timers()
    timers.add('timer1', 3.0)
    timers.add('timer1', 2.0)
    timers.add('timer1', 1.0)
    assert timers.min('timer1') == 1.0





def test_timers_total_w5dxdpp2():
    timers = module_0.Timers()
    timers.add('timer1', 1.0)
    timers.add('timer1', 2.0)
    timers.add('timer1', 3.0)
    assert timers.total('timer1') == 6.0





def test_example_kcfieogi():
    timers = module_0.Timers()
    timers.add('timer1', 10.0)
    timers.add('timer1', 20.0)
    timers.add('timer2', 30.0)
    assert timers.mean('timer1') == 15.0


