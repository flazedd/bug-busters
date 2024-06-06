import doctest
import money as module_0
from typing import Tuple
from typing import Optional
from decimal import Decimal
import pytest
from decimal import ROUND_FLOOR
from typing import Union
from decimal import ROUND_HALF_DOWN
import logging
import re
def test_example_jgidgd0i():
    assert module_0.Money('100.00', 'USD') == module_0.Money('100.00', 'USD')


def test_example_kvfqk7xv():
    assert module_0.Money('100.00', 'USD') + module_0.Money('50.00', 'USD') == module_0.Money('150.00', 'USD')


def test_example_76nalipy():
    assert module_0.Money('100.00', 'USD') * 2 == module_0.Money('200.00', 'USD')


def test_example_x07rmg1g():
    m = module_0.Money('100.00', 'USD')
    m.truncate_fractional_cents()
    assert m == module_0.Money('100.00', 'USD')


def test_example_4pxa9s3c():
    m = module_0.Money('100.00', 'USD')
    m.round_fractional_cents()
    assert m == module_0.Money('100.00', 'USD')


def test_example_qfp7r4bw():
    assert module_0.Money('100.00', 'USD') - module_0.Money('50.00', 'USD') == module_0.Money('50.00', 'USD')


def test_example_3ryh0li5():
    assert module_0.Money('100.00', 'USD') / 2 == module_0.Money('50.00', 'USD')


def test_example_4ryae9ka():
    m = module_0.Money('100.00', 'USD')
    assert str(m) == '100.00 USD'


