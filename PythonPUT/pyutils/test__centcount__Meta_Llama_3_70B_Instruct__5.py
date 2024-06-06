import pytest
from typing import Tuple
import centcount as module_0
import re
import logging
import doctest
from typing import Optional
from typing import Union
def test_example_csz7pmsw():
    assert module_0.CentCount(100, 'USD') == module_0.CentCount(100, 'USD')


def test_example_av9u2y09():
    assert module_0.CentCount(50, 'USD') + module_0.CentCount(25, 'USD') == module_0.CentCount(75, 'USD')


def test_example_pl72hado():
    assert module_0.CentCount(100, 'USD') * 2 == module_0.CentCount(200, 'USD')


def test_example_lfeki1i5():
    assert module_0.CentCount(100, 'USD') / 2 == module_0.CentCount(50, 'USD')


def test_example_grfpv2kg():
    assert module_0.CentCount.parse('100.00 USD') == module_0.CentCount(10000, 'USD')


def test_example_c09c57nr():
    assert module_0.CentCount(100, 'USD') > module_0.CentCount(50, 'USD')


def test_example_6fp5w66r():
    assert module_0.CentCount(100, 'USD') - module_0.CentCount(25, 'USD') == module_0.CentCount(75, 'USD')


def test_example_d587cq0t():
    assert module_0.CentCount(100, 'USD') != module_0.CentCount(100, 'EUR')


