import money as module_0
from decimal import Decimal
import logging
import doctest
from decimal import ROUND_HALF_DOWN
from typing import Tuple
import re
from typing import Union
import pytest
from typing import Optional
from decimal import ROUND_FLOOR
def test_example_g3swogg1():
    assert module_0.Money('100.00', 'USD') == module_0.Money('100.00', 'USD')





def test_example_vlr577fq():
    assert module_0.Money('100.00', 'USD') == module_0.Money('100.00', 'USD')


def test_example_zvg8zlem():
    assert module_0.Money('50.00', 'USD') + module_0.Money('25.00', 'USD') == module_0.Money('75.00', 'USD')


def test_example_knmwuyef():
    m = module_0.Money('100.00', 'USD')
    m *= 2
    m /= 3
    assert m.truncate_fractional_cents() == module_0.Decimal('66.66')


def test_example_v61kdk9e():
    m = module_0.Money('100.00', 'USD')
    m *= 2
    m /= 3
    assert m.round_fractional_cents() == module_0.Decimal('66.67')


def test_example_s80gz9mc():
    m1 = module_0.Money('100.00', 'USD')
    m2 = module_0.Money('50.00', 'USD')
    assert m1 > m2


def test_example_vjfgptb0():
    m = module_0.Money('100.00', 'USD')
    assert m.__repr__() == '100.00 USD'


def test_example_lnacu1r2():
    m = module_0.Money('100.00', 'USD')
    assert m.__float__() == 100.0


