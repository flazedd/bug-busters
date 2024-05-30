import pytest
import rate as module_0
from typing import Optional
def test_example_xwu85dpl():
    rate = module_0.Rate(multiplier=1.5)
    assert rate.apply_to(100) == 150.0





def test_example_jgub0pfe():
    rate = module_0.Rate(percent_change=25)
    assert rate.of(100) == 125.0





def test_example_49eby6po():
    rate = module_0.Rate(percentage=120)
    assert rate.apply_to(50) == 60.0





def test_example_mk482jws():
    rate = module_0.Rate(multiplier='150%')
    assert rate.apply_to(100) == 150.0





def test_example_kizoaruz():
    rate = module_0.Rate(multiplier=2.0)
    assert rate.__float__() == 2.0





def test_example_0wx4ge0u():
    rate1 = module_0.Rate(multiplier=1.5)
    rate2 = module_0.Rate(multiplier=2.0)
    assert rate1.__mul__(100) + rate2.__mul__(50) == 250.0





def test_example_1mzpcbi4():
    rate = module_0.Rate(multiplier=1.5)
    assert rate.apply_to(100) == 150


def test_example_sgvygr1d():
    rate = module_0.Rate(percent_change=25)
    assert rate.of(100) == 125


