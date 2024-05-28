import re
from typing import Optional
import centcount as module_0
import pytest
from typing import Tuple
import logging
from typing import Union
import doctest
def test_example_cjch7dhb():
    assert module_0.CentCount(100, 'USD') == module_0.CentCount(1, 'USD') * 100


def test_example_98e06t5n():
    assert module_0.CentCount(50, 'USD') + module_0.CentCount(25, 'USD') == module_0.CentCount(75, 'USD')


def test_example_rbn0bwt0():
    assert module_0.CentCount(100, 'USD') / 2 == module_0.CentCount(50, 'USD')


def test_example_271eq9te():
    assert module_0.CentCount(100, 'USD') - module_0.CentCount(25, 'USD') == module_0.CentCount(75, 'USD')


def test_example_ysrfxsrg():
    assert module_0.CentCount('100.00 USD') == module_0.CentCount(10000, 'USD')


def test_example_iaic6sob():
    assert module_0.CentCount(100, 'USD') == module_0.CentCount('1.00 USD')


def test_example_6woj9iwb():
    assert module_0.CentCount(100, 'USD') > module_0.CentCount(50, 'USD')


def test_example_mxwm3264():
    assert module_0.CentCount(100, 'USD') != module_0.CentCount(100, 'EUR')


