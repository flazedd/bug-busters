# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import dummy as module_0


def test_case_0():
    dummy_0 = module_0.Dummy()


@pytest.mark.xfail(strict=True)
def test_case_1():
    dummy_0 = module_0.Dummy()
    dummy_0.add(dummy_0, dummy_0)
