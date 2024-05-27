import logging
from typing import Tuple
import doctest
import pytest
import re
from typing import Optional
import centcount as module_0
from typing import Union
def test_centcount_addition_pf7eh8qd():
    assert module_0.CentCount(100, 'USD') + module_0.CentCount(50, 'USD') == module_0.CentCount(150, 'USD')


def test_centcount_multiplication_o1twis35():
    assert module_0.CentCount(100, 'USD') * 2 == module_0.CentCount(200, 'USD')


def test_centcount_subtraction_95zt7xxb():
    assert module_0.CentCount(150, 'USD') - module_0.CentCount(50, 'USD') == module_0.CentCount(100, 'USD')


def test_centcount_equality_6t1fbiei():
    assert module_0.CentCount(100, 'USD') == module_0.CentCount(100, 'USD')


def test_centcount_parsing_8bn7edfl():
    assert module_0.CentCount.parse('100.00 USD') == module_0.CentCount(10000, 'USD')


def test_centcount_division_u3bf014w():
    assert module_0.CentCount(200, 'USD') / 2 == module_0.CentCount(100, 'USD')


def test_centcount_lt_9h2qmowh():
    assert module_0.CentCount(100, 'USD') < module_0.CentCount(150, 'USD')


def test_centcount_ne_nuf2i7fv():
    assert module_0.CentCount(100, 'USD') != module_0.CentCount(150, 'USD')


