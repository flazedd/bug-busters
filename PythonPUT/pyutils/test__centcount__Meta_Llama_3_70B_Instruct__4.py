from typing import Tuple
import logging
import doctest
import centcount as module_0
import pytest
import re
from typing import Optional
from typing import Union
def test_example_zck6kvzx():
    c = module_0.CentCount(100.0, 'USD')
    assert str(c) == '100.00 USD'





def test_example_rzrr8tm0():
    c1 = module_0.CentCount(100.0, 'USD')
    c2 = module_0.CentCount(50.0, 'USD')
    c3 = c1 + c2
    assert str(c3) == '150.00 USD'





def test_example_rnnfkba5():
    c1 = module_0.CentCount(100.0, 'USD')
    c2 = 2
    c3 = c1 * c2
    assert str(c3) == '200.00 USD'





def test_example_kh347uwi():
    c1 = module_0.CentCount(150.0, 'USD')
    c2 = 0.5
    c3 = c1 * c2
    assert str(c3) == '75.00 USD'





def test_example_dss8ve15():
    c1 = module_0.CentCount(100.0, 'USD')
    c2 = module_0.CentCount(50.0, 'EUR')
    try:
        c3 = c1 + c2
        assert False, 'Expected TypeError'
    except TypeError:
        assert True





def test_example_nge6mp9r():
    c1 = module_0.CentCount(100.0, 'USD')
    c2 = module_0.CentCount(50.0, 'USD')
    c3 = c1 - c2
    assert str(c3) == '50.00 USD'





def test_example_u8qqi5mj():
    c1 = module_0.CentCount(100.0, 'USD')
    c2 = 2.5
    c3 = c1 / c2
    assert str(c3) == '40.00 USD'





def test_example_p98mhywy():
    c = module_0.CentCount(100.0)
    assert str(c) == '100.00 USD'


