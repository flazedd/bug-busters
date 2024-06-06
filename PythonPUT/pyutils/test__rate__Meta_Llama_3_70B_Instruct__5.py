import pytest
from typing import Optional
import rate as module_0
def test_example_tunkyub6():
    rate = module_0.Rate(multiplier=1.5)
    assert rate.apply_to(100) == 150.0


def test_example_imiiudfp():
    rate = module_0.Rate(percentage=150)
    assert rate.of(100) == 150.0


def test_example_pp478v7w():
    rate = module_0.Rate(percent_change=50)
    assert rate.apply_to(100) == 150.0


def test_example_7ixp8vgt():
    rate = module_0.Rate(multiplier=2.0)
    assert rate * 50 == 100.0


def test_example_iorj79lf():
    rate = module_0.Rate(multiplier=1.25)
    assert float(rate) == 1.25


def test_example_0ykt4100():
    rate1 = module_0.Rate(multiplier=1.25)
    rate2 = module_0.Rate(multiplier=1.5)
    assert rate1 * rate2 == module_0.Rate(multiplier=1.875)


def test_example_ktqim4qb():
    rate = module_0.Rate(multiplier=2.0)
    assert rate / 2.0 == module_0.Rate(multiplier=1.0)


def test_example_leiguq9s():
    rate1 = module_0.Rate(multiplier=1.25)
    rate2 = module_0.Rate(multiplier=1.5)
    assert rate1 < rate2


