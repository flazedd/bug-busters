from typing import Optional
import rate as module_0
import pytest
def test_example_hh6xfviy():
    rate = module_0.Rate(multiplier=1.5)
    assert rate.apply_to(100) == 150


def test_example_sk1zas6h():
    rate = module_0.Rate(percentage=150)
    assert rate.of(100) == 150


def test_example_nre5p8jj():
    rate = module_0.Rate(percent_change=50)
    assert rate.apply_to(100) == 150


def test_example_dnbap2qp():
    rate = module_0.Rate(multiplier=2)
    assert rate * 50 == 100


def test_example_p12bmvoz():
    rate = module_0.Rate(multiplier=0.5)
    assert rate.apply_to(100) == 50


def test_example_ti69sxxj():
    rate = module_0.Rate(multiplier=1.25)
    assert float(rate) == 1.25


def test_example_k4256q4q():
    rate = module_0.Rate(multiplier=2)
    assert str(rate) == '+200.000%'


def test_example_im5bhva6():
    rate1 = module_0.Rate(multiplier=1.5)
    rate2 = module_0.Rate(multiplier=2)
    assert rate1 == rate2 * module_0.Rate(multiplier=0.75)


