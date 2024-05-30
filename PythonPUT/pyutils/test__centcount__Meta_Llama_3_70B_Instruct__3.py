import doctest
import re
import pytest
from typing import Union
import logging
import centcount as module_0
from typing import Tuple
from typing import Optional
def test_example_70lvkiov():
    assert module_0.CentCount(100, 'USD') == module_0.CentCount(1, 'USD') * 100





def test_example_ghgry7fd():
    assert module_0.CentCount(150, 'USD') == module_0.CentCount(100, 'USD') + module_0.CentCount(50, 'USD')





def test_example_r7018xk1():
    assert module_0.CentCount(50, 'USD') == module_0.CentCount(100, 'USD') / 2





def test_example_3kys1ayq():
    assert module_0.CentCount(0, 'USD') == -module_0.CentCount(0, 'USD')





def test_example_ystmok21():
    assert module_0.CentCount(100, 'USD') == module_0.CentCount(100, 'USD')


def test_example_zkkdk80x():
    assert module_0.CentCount(50, 'USD') < module_0.CentCount(100, 'USD')


def test_example_yoj4cqnr():
    assert module_0.CentCount(100, 'USD') + module_0.CentCount(50, 'USD') == module_0.CentCount(150, 'USD')


def test_example_eylu50u3():
    assert module_0.CentCount(100, 'USD') * 2 == module_0.CentCount(200, 'USD')


