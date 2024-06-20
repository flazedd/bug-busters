import doctest
from typing import Union
import re
from typing import Optional
from typing import Tuple
import money as module_0
from decimal import Decimal
from decimal import ROUND_FLOOR
import logging
from decimal import ROUND_HALF_DOWN
import pytest
def test_example_y0nc4pif():
    assert module_0.Money('10.00 USD') == module_0.Money('10.00 USD')


def test_example_pobo3bfd():
    assert module_0.Money('10.00 USD') + module_0.Money('5.00 USD') == module_0.Money('15.00 USD')


def test_example_6kh2p4qn():
    assert module_0.Money('10.00 USD') * 2 == module_0.Money('20.00 USD')


def test_example_8nihuw9w():
    m = module_0.Money('100.00 USD')
    m *= 2
    m /= 3
    assert m.truncate_fractional_cents() == module_0.Decimal('66.66')


def test_example_a1nj1un3():
    m = module_0.Money('100.00 USD')
    m *= 2
    m /= 3
    assert m.round_fractional_cents() == module_0.Decimal('66.67')


def test_example_376nu116():
    assert module_0.Money('10.00 USD') > module_0.Money('5.00 USD')


def test_example_t00zso7k():
    assert module_0.Money('10.00 USD') - module_0.Money('5.00 USD') == module_0.Money('5.00 USD')


def test_example_zta3hhaj():
    assert module_0.Money('10.00 USD').__repr__() == '10.00 USD'


