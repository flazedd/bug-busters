from typing import Union
import money as module_0
from typing import Tuple
from decimal import ROUND_FLOOR
import doctest
from typing import Optional
import logging
import pytest
from decimal import ROUND_HALF_DOWN
from decimal import Decimal
import re
def test_example_8pakcxp1():
    assert module_0.Money('100.00', 'USD') == module_0.Money('100.00', 'USD')


def test_example_m8vcl5ff():
    m = module_0.Money('100.00', 'USD')
    m2 = m * 2
    assert m2 == module_0.Money('200.00', 'USD')


def test_example_0e5p27ea():
    m = module_0.Money('100.00', 'USD')
    m2 = m.truncate_fractional_cents()
    assert m2 == module_0.Money('100.00', 'USD')


def test_example_7t0hfi3t():
    m = module_0.Money('100.00', 'USD')
    m2 = m + module_0.Money('50.00', 'USD')
    assert m2 == module_0.Money('150.00', 'USD')


def test_example_pv6yqb4f():
    m = module_0.Money('100.00', 'USD')
    m2 = m - module_0.Money('50.00', 'USD')
    assert m2 == module_0.Money('50.00', 'USD')


def test_example_ehgohsq6():
    m = module_0.Money('100.00', 'USD')
    m2 = m / 2
    assert m2 == module_0.Money('50.00', 'USD')


def test_example_q39hfgtk():
    m = module_0.Money('100.00', 'USD')
    m2 = -m
    assert m2 == module_0.Money('-100.00', 'USD')


def test_example_jc0kvw3y():
    m = module_0.Money('100.00', 'USD')
    assert m.round_fractional_cents() == module_0.Money('100.00', 'USD')


