import pytest
import rate as module_0
from typing import Optional
def test_example_6cvbdbf6():
    rate = module_0.Rate(multiplier=1.5)
    assert rate.of(100) == 150.0


def test_example_qw8rvb7j():
    rate = module_0.Rate(percent_change=25)
    assert rate.apply_to(100) == 125.0


def test_example_hj7qxi5t():
    rate = module_0.Rate(percentage=120)
    assert rate.of(100) == 120.0


def test_example_udds8gxn():
    rate = module_0.Rate(multiplier=2.0)
    assert rate * 10 == 20.0


def test_example_yckox3vn():
    rate = module_0.Rate(percent_change=50)
    assert rate * 100 == 150.0


def test_example_f2srm676():
    rate1 = module_0.Rate(multiplier=2.0)
    rate2 = module_0.Rate(multiplier=3.0)
    assert rate1 * rate2 == 6.0


def test_example_206cr3ke():
    rate = module_0.Rate(multiplier=1.25)
    assert rate.__repr__() == '+125.000%'


def test_example_493vdkeb():
    rate1 = module_0.Rate(multiplier=2.0)
    rate2 = module_0.Rate(multiplier=0.5)
    assert rate1 / rate2 == 4.0


