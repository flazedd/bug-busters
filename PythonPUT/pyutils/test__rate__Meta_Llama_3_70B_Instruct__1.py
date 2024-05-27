from typing import Optional
import rate as module_0
import pytest
def test_rate_example_rv03gfl5():
    rate = module_0.Rate(multiplier=1.5)
    assert rate.of(100) == 150.0


def test_rate_percentage_12jphmm0():
    rate = module_0.Rate(percentage=150)
    assert rate.of(100) == 150.0


def test_rate_percent_change_ltr7a4w6():
    rate = module_0.Rate(percent_change=50)
    assert rate.of(100) == 150.0


def test_rate_equality_f9p8777o():
    rate1 = module_0.Rate(multiplier=1.5)
    rate2 = module_0.Rate(percentage=150)
    assert rate1 == rate2


def test_rate_repr_y4eulcyv():
    rate = module_0.Rate(multiplier=1.5)
    assert repr(rate) == '+150.000%'


def test_rate_addition_3ok8nxkw():
    rate1 = module_0.Rate(multiplier=1.5)
    rate2 = module_0.Rate(multiplier=2.0)
    assert rate1 + rate2 == 3.5


def test_rate_subtraction_e2m1bdr9():
    rate1 = module_0.Rate(multiplier=2.0)
    rate2 = module_0.Rate(multiplier=1.5)
    assert rate1 - rate2 == 0.5


def test_rate_division_npe48hk6():
    rate1 = module_0.Rate(multiplier=2.0)
    assert rate1 / 2.0 == 1.0


