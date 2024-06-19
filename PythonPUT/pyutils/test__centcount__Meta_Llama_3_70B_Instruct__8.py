from typing import Union
import centcount as module_0
from typing import Tuple
import doctest
from typing import Optional
import logging
import pytest
import re
def test_example_tu0rb0xy():
    c = module_0.CentCount(100.0)
    assert c.centcount == 10000


def test_example_hwleepc8():
    c = module_0.CentCount('100.00 USD')
    assert c.currency == 'USD'


def test_example_t93exfx5():
    c1 = module_0.CentCount(100.0)
    c2 = module_0.CentCount(50.0)
    c3 = c1 + c2
    assert c3.centcount == 15000


def test_example_aqu59jz3():
    c = module_0.CentCount(100.0)
    c2 = c * 2
    assert c2.centcount == 20000


def test_example_ktmxjn7r():
    c1 = module_0.CentCount(100.0, 'USD')
    c2 = module_0.CentCount(50.0, 'EUR')
    try:
        c3 = c1 + c2
    except TypeError:
        assert True
    else:
        assert False


def test_example_pc48jpoy():
    c = module_0.CentCount(100.0)
    c2 = c / 2
    assert c2.centcount == 5000


def test_example_ahgzfv7s():
    c = module_0.CentCount(100.0)
    assert str(c) == '100.00 USD'


def test_example_7v27i2m4():
    c = module_0.CentCount(100.0)
    c2 = module_0.CentCount(50.0)
    assert c > c2


