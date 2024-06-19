from typing import Optional
import pytest
import rate as module_0
def test_example_6vn3qeh2():
    rate = module_0.Rate(multiplier=1.5)
    assert rate.of(100) == 150.0


def test_example_vb8lsvsg():
    rate = module_0.Rate(percentage=150)
    assert rate.apply_to(100) == 150.0


def test_example_gddf2s0j():
    rate = module_0.Rate(percent_change=50)
    assert rate.of(100) == 150.0


def test_example_2yd98gde():
    rate1 = module_0.Rate(multiplier=2.0)
    rate2 = module_0.Rate(multiplier=1.5)
    assert rate1.of(100) * rate2.of(1) == 300.0


def test_example_gjbhxc6g():
    rate = module_0.Rate(percent_change=-25)
    assert rate.of(100) == 75.0


def test_example_gplp8tgd():
    rate = module_0.Rate(multiplier=0.5)
    assert rate.of(200) == 100.0


def test_example_kg97h53t():
    rate1 = module_0.Rate(multiplier=2.0)
    rate2 = module_0.Rate(multiplier=0.5)
    assert rate1.of(rate2.of(100)) == 100.0


def test_example_nohi29mh():
    rate = module_0.Rate(multiplier=1.0)
    assert rate.of(100) == 100.0


