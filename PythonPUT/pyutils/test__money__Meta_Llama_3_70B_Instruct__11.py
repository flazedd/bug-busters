from typing import Optional
import pytest
from decimal import ROUND_HALF_DOWN
from decimal import Decimal
import money as module_0
from typing import Tuple
import doctest
import logging
import re
from decimal import ROUND_FLOOR
from typing import Union
def test_example_9as6bsmu():
    m = module_0.Money('100.00', 'USD')
    assert m.amount == Decimal('100.00')


def test_example_t9gez2mi():
    m1 = module_0.Money('100.00', 'USD')
    m2 = module_0.Money('50.00', 'USD')
    m3 = m1 + m2
    assert m3.amount == Decimal('150.00')


def test_example_lybtz871():
    m = module_0.Money('100.00', 'USD')
    m.truncate_fractional_cents()
    assert m.amount == Decimal('100.00')


def test_example_h9p57ocf():
    m1 = module_0.Money('100.00', 'USD')
    m2 = module_0.Money('100.00', 'EUR')
    try:
        m1 + m2
    except TypeError as e:
        assert str(e) == 'Incompatible currencies in add expression'


def test_example_sagmyent():
    m = module_0.Money('100.00', 'USD')
    assert m.__repr__() == '100.00 USD'


def test_example_wyo6la8l():
    m1 = module_0.Money('100.00', 'USD')
    m2 = module_0.Money('50.00', 'USD')
    assert m1 > m2


def test_example_vpadv6ok():
    m = module_0.Money('100.00', 'USD')
    assert m.__float__() == 100.0


def test_example_197y0gdz():
    m = module_0.Money('100.00', 'USD')
    m.round_fractional_cents()
    assert m.amount == Decimal('100.00')


