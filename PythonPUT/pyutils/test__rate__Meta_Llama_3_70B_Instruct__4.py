import rate as module_0
from typing import Optional
import pytest
def test_example_ojlyc57i():
    rate = module_0.Rate(multiplier=1.5)
    assert rate.apply_to(100) == 150


def test_example_t1102kef():
    rate = module_0.Rate(percent_change=50)
    assert rate.of(100) == 150


def test_example_44tbgz0v():
    rate = module_0.Rate(percentage=150)
    assert rate.apply_to(100) == 150


def test_example_6cwebzz1():
    rate = module_0.Rate(multiplier=2.0)
    assert rate.of(50) == 100


def test_example_m2gy710g():
    rate1 = module_0.Rate(multiplier=1.2)
    rate2 = module_0.Rate(multiplier=1.5)
    assert rate1 * rate2.of(100) == 180


def test_example_tx42b16q():
    rate = module_0.Rate(percent_change=-25)
    assert rate.apply_to(100) == 75


def test_example_o7swf1fv():
    rate1 = module_0.Rate(multiplier=0.8)
    rate2 = module_0.Rate(multiplier=0.9)
    assert rate1.of(rate2.of(100)) == 72


def test_example_dedfnou8():
    rate = module_0.Rate(percentage=50)
    assert rate.apply_to(200) == 100


