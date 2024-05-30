import money as module_0
import doctest
import re
import pytest
from typing import Union
import logging
from decimal import ROUND_FLOOR
from decimal import ROUND_HALF_DOWN
from decimal import Decimal
from typing import Tuple
from typing import Optional
def test_example_hboq10u6():
    assert module_0.Money('100.00', 'USD') == module_0.Money('100.00', 'USD')


def test_example_g3wsf2ge():
    m = module_0.Money('100.00', 'USD')
    m *= 2
    m /= 3
    assert m.truncate_fractional_cents() == module_0.Decimal('66.66')


def test_example_qkjgtu0e():
    m1 = module_0.Money('100.00', 'USD')
    m2 = module_0.Money('50.00', 'USD')
    assert m1 > m2


def test_example_cygwmijr():
    m = module_0.Money('100.00', 'USD')
    m.round_fractional_cents()
    assert m.amount == module_0.Decimal('100.00')


def test_example_curppsu0():
    m1 = module_0.Money('100.00', 'USD')
    m2 = module_0.Money('50.00', 'USD')
    assert m1 - m2 == module_0.Money('50.00', 'USD')


def test_example_283mzlni():
    m = module_0.Money('100.00', 'USD')
    assert m.__repr__() == '100.00 USD'


def test_example_0dayashx():
    m = module_0.Money('100.00', 'USD')
    assert m.__float__() == 100.0


def test_example_8idzvv2k():
    m = module_0.Money('100.00', 'USD')
    assert m.__pos__() == module_0.Money('100.00', 'USD')


