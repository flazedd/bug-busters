from typing import Optional
import pytest
import rate as module_0
def test_example_g6a5ia1c():
    rate = module_0.Rate(multiplier=1.5)
    assert rate.apply_to(100) == 150


def test_example_rqfv1r5g():
    rate = module_0.Rate(percent_change=50)
    assert rate.of(100) == 150


def test_example_a29u42ks():
    rate = module_0.Rate(percentage=150)
    assert rate.apply_to(100) == 150


def test_example_eze1bfll():
    rate = module_0.Rate(multiplier='150%')
    assert rate.of(100) == 150


def test_example_o1ohav7r():
    rate1 = module_0.Rate(multiplier=1.5)
    rate2 = module_0.Rate(multiplier=1.5)
    assert rate1 == rate2


def test_example_0cpc6ntp():
    rate = module_0.Rate(multiplier=2.0)
    assert rate.__repr__() == '+200.000%'


def test_example_66jxbfun():
    rate = module_0.Rate(multiplier=0.5)
    assert rate.__repr__(relative=True) == '-50.000%'


def test_example_g70j214t():
    rate1 = module_0.Rate(multiplier=2.0)
    rate2 = module_0.Rate(multiplier=3.0)
    assert rate1 < rate2


