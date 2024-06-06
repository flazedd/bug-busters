from decimal import Decimal
import re
import pytest
from typing import Optional
from decimal import ROUND_HALF_DOWN
from typing import Tuple
import money as module_0
from decimal import ROUND_FLOOR
import doctest
from typing import Union
import logging
def test_example_zcno1llo():
    assert module_0.Money('100.00', 'USD') == module_0.Money('100.00', 'USD')


def test_example_6hwvlg3g():
    assert module_0.Money('100.00', 'USD') + module_0.Money('50.00', 'USD') == module_0.Money('150.00', 'USD')


def test_example_oxgsk6u5():
    m = module_0.Money('100.00', 'USD')
    m *= 2
    m /= 3
    m.truncate_fractional_cents()
    assert m == module_0.Money('66.66', 'USD')


def test_example_usx0gr4w():
    m = module_0.Money('100.00', 'USD')
    m.round_fractional_cents()
    assert m == module_0.Money('100.00', 'USD')


def test_example_g9x0lhqt():
    assert module_0.Money('100.00', 'USD') > module_0.Money('50.00', 'USD')


def test_example_b0onv4tp():
    assert module_0.Money.parse('100.00 USD') == module_0.Money('100.00', 'USD')


def test_example_gz000myq():
    m = module_0.Money('100.00', 'USD')
    assert m.__repr__() == '100.00 USD'


def test_example_qg1kocx5():
    m = module_0.Money('100.00', 'USD')
    assert m.__float__() == 100.0


