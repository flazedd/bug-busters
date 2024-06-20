import doctest
from typing import Union
import re
from typing import Optional
from typing import Tuple
import logging
import centcount as module_0
import pytest
def test_example_dvv1yp3y():
    c = module_0.CentCount(100.0, 'USD')
    assert str(c) == '100.00 USD'


def test_example_5n3cz594():
    c1 = module_0.CentCount(100.0, 'USD')
    c2 = module_0.CentCount(50.0, 'USD')
    c3 = c1 + c2
    assert str(c3) == '150.00 USD'


def test_example_4vvxl1lb():
    c1 = module_0.CentCount(100.0, 'USD')
    c2 = c1 * 2
    assert str(c2) == '200.00 USD'


def test_example_vywve0ix():
    c1 = module_0.CentCount(150.0, 'USD')
    c2 = c1 / 3
    assert str(c2) == '50.00 USD'


def test_example_9uzxfejp():
    c1 = module_0.CentCount(100.0, 'USD')
    c2 = module_0.CentCount(100.0, 'EUR')
    try:
        c3 = c1 + c2
        assert False, 'Expected TypeError to be raised'
    except TypeError:
        assert True


def test_example_cr6cll2r():
    c1 = module_0.CentCount(100.0, 'USD')
    c2 = module_0.CentCount(50.0, 'USD')
    assert c1 > c2


def test_example_a4jfo7vk():
    c1 = module_0.CentCount(100.0, 'USD')
    c2 = module_0.CentCount(100.0, 'USD')
    assert c1 == c2


def test_example_59j4vh17():
    c1 = module_0.CentCount(100.0, 'USD')
    c2 = module_0.CentCount(50.0, 'EUR')
    try:
        c3 = c1 + c2
        assert False, 'Expected TypeError to be raised'
    except TypeError:
        assert True


