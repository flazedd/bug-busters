import rate as module_0
from typing import Optional
import pytest
def test_example_kat5ws87():
    rate = module_0.Rate(multiplier=1.5)
    assert rate.of(100) == 150.0


def test_example_h5sogdes():
    rate = module_0.Rate(percentage=120)
    assert rate.apply_to(100) == 120.0


def test_example_zfkwed5n():
    rate = module_0.Rate(percent_change=25)
    assert rate.of(100) == 125.0


def test_example_5o1sv434():
    rate = module_0.Rate(multiplier='150%')
    assert rate.apply_to(100) == 150.0


def test_example_5xwq2ur8():
    rate = module_0.Rate(multiplier=2)
    assert rate == module_0.Rate(percentage=200)


def test_example_blrb6kbw():
    rate1 = module_0.Rate(multiplier=2)
    rate2 = module_0.Rate(multiplier=0.5)
    assert rate1 / rate2 == module_0.Rate(multiplier=4)


def test_example_8kx0ck0l():
    rate = module_0.Rate(multiplier=2)
    assert rate.__repr__() == '+200.000%'


def test_example_904likyo():
    rate1 = module_0.Rate(multiplier=2)
    rate2 = module_0.Rate(multiplier=3)
    assert rate1.of(100) > rate2.of(50)


