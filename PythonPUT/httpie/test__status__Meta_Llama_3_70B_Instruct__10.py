from enum import IntEnum
import pytest
import status as module_0
from enum import unique
def test_example_io07xvqq():
    assert module_0.http_status_to_exit_status(404) == module_0.ExitStatus.ERROR_HTTP_4XX


def test_example_54fgzakn():
    assert module_0.http_status_to_exit_status(302, follow=True) == module_0.ExitStatus.SUCCESS


def test_example_4fzefmb8():
    assert module_0.http_status_to_exit_status(500) == module_0.ExitStatus.ERROR_HTTP_5XX


def test_example_766wh1r4():
    assert module_0.http_status_to_exit_status(200) == module_0.ExitStatus.SUCCESS


def test_example_tkdbzb2f():
    assert module_0.http_status_to_exit_status(301) == module_0.ExitStatus.ERROR_HTTP_3XX


def test_example_eup1ztfv():
    assert module_0.http_status_to_exit_status(600) == module_0.ExitStatus.SUCCESS


def test_example_cxogijrz():
    assert module_0.http_status_to_exit_status(400, follow=False) == module_0.ExitStatus.ERROR_HTTP_4XX


def test_example_bml8ltki():
    assert module_0.http_status_to_exit_status(399, follow=True) == module_0.ExitStatus.SUCCESS


