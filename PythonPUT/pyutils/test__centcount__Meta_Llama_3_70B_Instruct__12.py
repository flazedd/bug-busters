from typing import Optional
import pytest
import centcount as module_0
from typing import Tuple
import doctest
import logging
import re
from typing import Union
def test_example_snl7nlwp():
    assert module_0.CentCount(100, 'USD') == module_0.CentCount(100, 'USD')


def test_example_t2igz6my():
    assert module_0.CentCount(200, 'USD') - module_0.CentCount(100, 'USD') == module_0.CentCount(100, 'USD')


def test_example_a2ponr3g():
    assert module_0.CentCount(100, 'USD') * 2 == module_0.CentCount(200, 'USD')


def test_example_sqgtvjur():
    assert module_0.CentCount(100, 'USD') / 2 == module_0.CentCount(50, 'USD')


def test_example_7huz03un():
    assert module_0.CentCount(100, 'USD') + module_0.CentCount(50, 'USD') == module_0.CentCount(150, 'USD')


def test_example_itps9t9s():
    assert module_0.CentCount.parse('100.00 USD') == module_0.CentCount(10000, 'USD')


def test_example_uap8wtuv():
    assert module_0.CentCount(100, 'USD') > module_0.CentCount(50, 'USD')


def test_example_h4v7ru07():
    assert module_0.CentCount(100, 'USD') != module_0.CentCount(100, 'EUR')


