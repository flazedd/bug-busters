import logging
from typing import Tuple
import pytest
import doctest
from decimal import ROUND_FLOOR
from decimal import Decimal
from typing import Union
from decimal import ROUND_HALF_DOWN
from typing import Optional
import money as module_0
import re
def test_example_pxoq88ex():
    m = module_0.Money(amount='100.00', currency='USD')
    assert str(m) == '100.00 USD'


def test_example_7y9bruuw():
    m1 = module_0.Money(amount='100.00', currency='USD')
    m2 = module_0.Money(amount='50.00', currency='USD')
    assert str(m1 + m2) == '150.00 USD'


def test_example_cwu3ztuy():
    m = module_0.Money(amount='100.00', currency='USD')
    assert m.truncate_fractional_cents() == Decimal('100.00')


def test_example_lmdmak3z():
    m = module_0.Money(amount='100.00', currency='USD')
    assert m.round_fractional_cents() == Decimal('100.00')


def test_example_o68f1jjf():
    m = module_0.Money(amount='100.00', currency='USD')
    assert m.__float__() == 100.0


def test_example_347bnnci():
    m = module_0.Money(amount='100.00', currency='USD')
    assert m.__repr__() == '100.00 USD'


def test_example_9y1xb47e():
    m = module_0.Money(amount='100.00', currency='USD')
    assert m.__neg__() == module_0.Money(amount='-100.00', currency='USD')


def test_example_ngifm73h():
    m1 = module_0.Money(amount='100.00', currency='USD')
    m2 = module_0.Money(amount='50.00', currency='USD')
    assert m1 > m2


