from decimal import ROUND_HALF_DOWN
import logging
import doctest
from typing import Tuple
import re
import money as module_0
from typing import Optional
import pytest
from decimal import Decimal
from decimal import ROUND_FLOOR
from typing import Union
def test_example_ee44qm12():
    assert module_0.Money('100.00', 'USD') == module_0.Money('100.00', 'USD')


def test_example_n1wv51sb():
    assert module_0.Money('100.00', 'USD') + module_0.Money('50.00', 'USD') == module_0.Money('150.00', 'USD')


def test_example_rtgg6yfj():
    m = module_0.Money('100.00', 'USD')
    m *= 2
    m /= 3
    assert m.truncate_fractional_cents() == module_0.Decimal('66.66')


def test_example_iwwmpcly():
    m = module_0.Money('100.00', 'USD')
    m *= 2
    m /= 3
    assert m.round_fractional_cents() == module_0.Decimal('66.67')


def test_example_mipwgxv2():
    m1 = module_0.Money('100.00', 'USD')
    m2 = module_0.Money('50.00', 'USD')
    assert m1 > m2


def test_example_y8doav45():
    m = module_0.Money('100.00', 'USD')
    assert m.__repr__() == '100.00 USD'


def test_example_irg4fx8p():
    m = module_0.Money('100.00', 'USD')
    assert m.__float__() == 100.0


def test_example_ek5k24c4():
    m = module_0.Money('100.00', 'USD')
    assert m.parse('100.00 USD') == m


