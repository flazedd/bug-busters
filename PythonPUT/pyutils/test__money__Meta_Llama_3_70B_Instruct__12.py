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
def test_example_ly9x3px3():
    m = module_0.Money('100.00', 'USD')
    assert m.amount == Decimal('100.00')


def test_example_wi4jpw5s():
    m1 = module_0.Money('100.00', 'USD')
    m2 = module_0.Money('50.00', 'USD')
    assert m1 - m2 == module_0.Money('50.00', 'USD')


def test_example_erm0aatd():
    m = module_0.Money('100.00', 'USD')
    m.truncate_fractional_cents()
    assert m.amount == Decimal('100.00')


def test_example_x5727460():
    m = module_0.Money('100.00', 'USD')
    assert str(m) == '100.00 USD'


def test_example_08ucloxf():
    m1 = module_0.Money('100.00', 'USD')
    m2 = module_0.Money('50.00', 'USD')
    assert m1 > m2


def test_example_wh8t92c7():
    m = module_0.Money('100.00', 'USD')
    assert m.round_fractional_cents() == Decimal('100.00')


def test_example_35h4b42s():
    m = module_0.Money('100.00', 'USD')
    assert m.__float__() == 100.0


def test_example_40iceg34():
    m = module_0.Money('100.00', 'USD')
    assert m.__repr__() == '100.00 USD'


