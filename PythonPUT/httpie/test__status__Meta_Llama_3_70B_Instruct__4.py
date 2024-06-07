import pytest
import status as module_0
from enum import IntEnum
from enum import unique
def test_example_y06yz6ql():
    assert module_0.http_status_to_exit_status(404) == module_0.ExitStatus.ERROR_HTTP_4XX


def test_example_3atbgwg0():
    assert module_0.http_status_to_exit_status(301) == module_0.ExitStatus.ERROR_HTTP_3XX


def test_example_7088xplc():
    assert module_0.http_status_to_exit_status(200) == module_0.ExitStatus.SUCCESS


def test_example_47mgnzjf():
    assert module_0.http_status_to_exit_status(502, follow=False) == module_0.ExitStatus.ERROR_HTTP_5XX


def test_example_k5mzjx23():
    assert module_0.http_status_to_exit_status(300) == module_0.ExitStatus.ERROR_HTTP_3XX


def test_example_uyei1mou():
    assert module_0.http_status_to_exit_status(100) == module_0.ExitStatus.SUCCESS


def test_example_6t3d0php():
    assert module_0.http_status_to_exit_status(504, follow=True) == module_0.ExitStatus.ERROR_HTTP_5XX


def test_example_cex5qf04():
    assert module_0.http_status_to_exit_status(401) == module_0.ExitStatus.ERROR_HTTP_4XX


