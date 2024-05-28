import pytest
from typing import Optional
import rate as module_0
def test_example_kx8vzq4u():
    rate = module_0.Rate(multiplier=1.5)
    assert rate.apply_to(100) == 150.0








def test_example_b0v091hb():
    rate = module_0.Rate(percentage=120)
    assert rate.of(50) == 60.0








def test_example_51d0q2x3():
    rate = module_0.Rate(percent_change=25)
    assert rate.apply_to(80) == 100.0








def test_example_vayb16kw():
    rate = module_0.Rate(multiplier='150%')
    assert rate.of(100) == 150.0








def test_example_fkh11jz4():
    rate1 = module_0.Rate(multiplier=1.5)
    rate2 = module_0.Rate(percentage=150)
    assert rate1 == rate2








def test_example_3ardaevq():
    rate = module_0.Rate(multiplier=2)
    assert rate.__repr__(relative=True) == '+100.000%'








def test_example_z69bif0o():
    rate = module_0.Rate(multiplier=1.5)
    assert rate.apply_to(100) == 150





def test_example_d0dti1ex():
    rate = module_0.Rate(multiplier=1.5)
    assert rate.apply_to(100) == 150.0


