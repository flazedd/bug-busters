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
def test_example_e7k32zzv():
    assert module_0.Money('100.00', 'USD') == module_0.Money('100.00', 'USD')


def test_example_axny2mif():
    m1 = module_0.Money('100.00', 'USD')
    m2 = module_0.Money('50.00', 'USD')
    assert m1 - m2 == module_0.Money('50.00', 'USD')


def test_example_1j4ic99u():
    m = module_0.Money('100.00', 'USD')
    assert m.truncate_fractional_cents() == module_0.Decimal('100.00')


def test_example_xubk9c58():
    m1 = module_0.Money('100.00', 'USD')
    m2 = module_0.Money('150.00', 'USD')
    assert m1 < m2


def test_example_e0g4lr5s():
    m = module_0.Money('100.00', 'USD')
    assert m.round_fractional_cents() == module_0.Decimal('100.00')


def test_example_a9c48ltw():
    m = module_0.Money('100.00', 'USD')
    assert m.__repr__() == '100.00 USD'


def test_example_yo14dz02():
    m = module_0.Money('100.00', 'USD')
    assert m.__float__() == 100.0


def test_example_3rmqmmd4():
    m = module_0.Money('100.00', 'USD')
    assert m.parse('100.00 USD') == m


