from typing import Optional
import pytest
import centcount as module_0
from typing import Tuple
import doctest
import logging
import re
from typing import Union
def test_example_5ozfkr4u():
    assert module_0.CentCount(100, 'USD') == module_0.CentCount(100, 'USD')


def test_example_jejzd1e6():
    c = module_0.CentCount(100.0)
    assert c == module_0.CentCount(10000, 'USD')


def test_example_dfelvbx8():
    c1 = module_0.CentCount(100.0)
    c2 = module_0.CentCount(50.0)
    assert c1 - c2 == module_0.CentCount(50.0)


def test_example_r2pexnpz():
    c = module_0.CentCount(100.0)
    assert c * 2 == module_0.CentCount(200.0)


def test_example_a7pg6wwm():
    c = module_0.CentCount(100.0)
    assert c / 2 == module_0.CentCount(50.0)


def test_example_93y19929():
    c = module_0.CentCount('100.00 USD')
    assert c == module_0.CentCount(100.0, 'USD')


def test_example_uitlcl2u():
    c1 = module_0.CentCount(100.0, 'USD')
    c2 = module_0.CentCount(100.0, 'EUR')
    try:
        c1 + c2
        assert False
    except TypeError:
        assert True


def test_example_4t9z72d8():
    c = module_0.CentCount(100.0)
    assert int(c) == 10000


