from typing import Optional
import pytest
import rate as module_0
def test_example_7jnrmrh9():
    rate = module_0.Rate(multiplier=1.5)
    assert rate.of(100) == 150.0


def test_example_v10g2fk9():
    rate = module_0.Rate(percentage=150)
    assert rate.apply_to(100) == 150.0


def test_example_uvw2culm():
    rate = module_0.Rate(percent_change=50)
    assert rate.of(100) == 150.0


def test_example_eo4d0t6o():
    rate = module_0.Rate(multiplier=2.0)
    assert rate.__float__() == 2.0


def test_example_1ounpns6():
    rate1 = module_0.Rate(multiplier=2.0)
    rate2 = module_0.Rate(multiplier=3.0)
    assert rate1 * 10 == rate2 * 6.666666666666667


def test_example_7a1shm7t():
    rate1 = module_0.Rate(multiplier=2.0)
    rate2 = module_0.Rate(multiplier=2.0)
    assert rate1 == rate2


def test_example_ib00j8zw():
    rate1 = module_0.Rate(multiplier=2.0)
    rate2 = module_0.Rate(multiplier=3.0)
    assert rate1 < rate2


def test_example_8lxdd2wu():
    rate = module_0.Rate(multiplier=2.0)
    assert str(rate) == '+200.000%'


