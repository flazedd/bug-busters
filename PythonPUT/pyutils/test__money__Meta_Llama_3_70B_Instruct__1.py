import logging
from typing import Tuple
from decimal import ROUND_HALF_DOWN
from typing import Optional
import re
from typing import Union
import pytest
from decimal import ROUND_FLOOR
from decimal import Decimal
import money as module_0
import doctest
def test_example_1ri0n9ec():
    m = module_0.Money(amount=100, currency='USD')
    assert m.amount == Decimal('100')


def test_example_d5yq8qow():
    m1 = module_0.Money(amount=100, currency='USD')
    m2 = module_0.Money(amount=50, currency='USD')
    assert m1 > m2


def test_example_zz4tu128():
    m = module_0.Money(amount='100.50', currency='USD')
    assert m.currency == 'USD'


def test_example_jmg9g3cc():
    m = module_0.Money(amount=100, currency='USD')
    m.truncate_fractional_cents()
    assert m.amount == Decimal('100.00')


def test_example_o9hy87gt():
    m = module_0.Money(amount='100.67', currency='USD')
    m.round_fractional_cents()
    assert m.amount == Decimal('100.67')


def test_example_fd9zgovb():
    m1 = module_0.Money(amount=100, currency='USD')
    m2 = module_0.Money(amount=100, currency='USD')
    assert m1 == m2


def test_example_pad6yisl():
    m = module_0.Money(amount=100, currency='USD')
    assert str(m) == '100.00 USD'


def test_example_r3bdkoqr():
    m1 = module_0.Money(amount=100, currency='USD')
    m2 = module_0.Money(amount=50, currency='EUR')
    try:
        m1 + m2
        assert False
    except TypeError:
        assert True


