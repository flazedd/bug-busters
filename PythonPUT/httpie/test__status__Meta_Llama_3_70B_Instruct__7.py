from enum import unique
import status as module_0
import pytest
from enum import IntEnum
def test_example_xsm8id8e():
    assert module_0.http_status_to_exit_status(404) == module_0.ExitStatus.ERROR_HTTP_4XX


def test_example_35s7nr23():
    assert module_0.http_status_to_exit_status(302, follow=True) == module_0.ExitStatus.SUCCESS


def test_example_5pc89svm():
    assert module_0.http_status_to_exit_status(500) == module_0.ExitStatus.ERROR_HTTP_5XX


def test_example_xa9iec5j():
    assert module_0.http_status_to_exit_status(200) == module_0.ExitStatus.SUCCESS


def test_example_6xl78jat():
    assert module_0.http_status_to_exit_status(301) == module_0.ExitStatus.ERROR_HTTP_3XX


def test_example_oun0mi4q():
    assert module_0.http_status_to_exit_status(499) == module_0.ExitStatus.ERROR_HTTP_4XX


def test_example_ojw954cs():
    assert module_0.http_status_to_exit_status(399) == module_0.ExitStatus.ERROR_HTTP_3XX


def test_example_h7sib5bk():
    assert module_0.http_status_to_exit_status(100) == module_0.ExitStatus.SUCCESS


