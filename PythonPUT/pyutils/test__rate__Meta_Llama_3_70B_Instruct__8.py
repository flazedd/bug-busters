from typing import Optional
import pytest
import rate as module_0
def test_example_14clq8rh():
    rate = module_0.Rate(multiplier=1.5)
    assert rate.apply_to(100) == 150.0


def test_example_xzecslib():
    rate = module_0.Rate(percent_change=25)
    assert rate.of(100) == 125.0


def test_example_xtaotu2y():
    rate = module_0.Rate(percentage=150)
    assert rate.apply_to(100) == 150.0


def test_example_frtv46m7():
    rate = module_0.Rate(multiplier=0.5)
    assert rate.apply_to(100) == 50.0


def test_example_hrwkwafb():
    rate = module_0.Rate(multiplier=2.0)
    assert rate.__float__() == 2.0


def test_example_quxu5vwu():
    rate = module_0.Rate(multiplier=2.0)
    assert rate.__repr__() == '+200.000%'


def test_example_9c8vgrjn():
    rate = module_0.Rate(multiplier=1.0)
    assert rate == module_0.Rate(multiplier=1.0)


def test_example_j1dc52vz():
    rate = module_0.Rate(multiplier=1.0)
    assert rate.__le__(module_0.Rate(multiplier=1.0))


