import dummy as module_0
import pytest
def test_dummy_add():
    dummy = module_0.Dummy()
    assert dummy.add(2, 3) == 5


def test_dummy_add_negative():
    dummy = module_0.Dummy()
    assert dummy.add(-2, 3) == 1


