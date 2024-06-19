import logging
import centcount as module_0
import doctest
from typing import Tuple
import re
from typing import Optional
import pytest
from typing import Union
def test_example_231ppkhh():
    assert module_0.CentCount(100, 'USD') == module_0.CentCount(1, 'USD') * 100


def test_example_fj2klg5f():
    assert module_0.CentCount(50, 'USD') + module_0.CentCount(25, 'USD') == module_0.CentCount(75, 'USD')


def test_example_e2c5gpp1():
    assert module_0.CentCount(100, 'USD') / 2 == module_0.CentCount(50, 'USD')


def test_example_o0limckr():
    assert module_0.CentCount('100.00 USD') == module_0.CentCount(10000, 'USD')


def test_example_uox43rxa():
    assert module_0.CentCount(100, 'USD') > module_0.CentCount(50, 'USD')


def test_example_et7avgk9():
    assert module_0.CentCount(100, 'USD') - module_0.CentCount(25, 'USD') == module_0.CentCount(75, 'USD')


def test_example_xsfaaj6v():
    assert module_0.CentCount(100, 'USD') == module_0.CentCount('1.00 USD')


def test_example_zlv95cel():
    assert module_0.CentCount(100, 'USD').__repr__() == '1.00 USD'


