from typing import Union
import centcount as module_0
from typing import Tuple
import doctest
from typing import Optional
import logging
import pytest
import re
def test_example_wb4f68as():
    assert module_0.CentCount(100, 'USD') == module_0.CentCount(100, 'USD')


def test_example_mirs3sqq():
    assert module_0.CentCount(100, 'USD') + module_0.CentCount(50, 'USD') == module_0.CentCount(150, 'USD')


def test_example_g851ngal():
    assert module_0.CentCount(100, 'USD') * 2 == module_0.CentCount(200, 'USD')


def test_example_vniz3x8r():
    assert module_0.CentCount(150, 'USD') / 2 == module_0.CentCount(75, 'USD')


def test_example_n5ku95kx():
    assert module_0.CentCount.parse('100.00 USD') == module_0.CentCount(10000, 'USD')


def test_example_vtfkb7tc():
    assert module_0.CentCount(100, 'USD') > module_0.CentCount(50, 'USD')


def test_example_k2g0nf9m():
    assert module_0.CentCount(100, 'USD') - module_0.CentCount(50, 'USD') == module_0.CentCount(50, 'USD')


def test_example_shh6ecdz():
    assert module_0.CentCount('100.00 USD') == module_0.CentCount(10000, 'USD')


