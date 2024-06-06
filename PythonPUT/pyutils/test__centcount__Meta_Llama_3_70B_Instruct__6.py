import doctest
from typing import Tuple
from typing import Optional
import pytest
import centcount as module_0
from typing import Union
import logging
import re
def test_example_104lkxzx():
    assert module_0.CentCount(100, 'USD') == module_0.CentCount(100, 'USD')


def test_example_u7kkani1():
    assert module_0.CentCount(50, 'USD') < module_0.CentCount(100, 'USD')


def test_example_o6y4yps8():
    assert module_0.CentCount(200, 'USD') == module_0.CentCount(100, 'USD') * 2


def test_example_coybbydh():
    assert module_0.CentCount('100.00 USD') == module_0.CentCount(10000, 'USD')


def test_example_bv4sigjr():
    assert module_0.CentCount(100, 'USD') + module_0.CentCount(50, 'USD') == module_0.CentCount(150, 'USD')


def test_example_vl3ud1n5():
    assert module_0.CentCount(150, 'USD') - module_0.CentCount(50, 'USD') == module_0.CentCount(100, 'USD')


def test_example_46fhmad6():
    assert module_0.CentCount(100, 'USD') / 2 == module_0.CentCount(50, 'USD')


def test_example_5e56xjk3():
    assert module_0.CentCount(100, 'USD').__repr__() == '1.00 USD'


