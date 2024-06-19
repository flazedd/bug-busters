from enum import IntEnum
import pytest
from enum import unique
import status as module_0
def test_example_hh7uzcb7():
    assert module_0.http_status_to_exit_status(404) == module_0.ExitStatus.ERROR_HTTP_4XX


def test_example_ww6ma0qe():
    assert module_0.http_status_to_exit_status(502) == module_0.ExitStatus.ERROR_HTTP_5XX


def test_example_un7y48cr():
    assert module_0.http_status_to_exit_status(301, follow=True) == module_0.ExitStatus.SUCCESS


def test_example_ldk4eip5():
    assert module_0.http_status_to_exit_status(200) == module_0.ExitStatus.SUCCESS


def test_example_mys11v66():
    assert module_0.http_status_to_exit_status(399) == module_0.ExitStatus.ERROR_HTTP_3XX


def test_example_nzi49c13():
    assert module_0.http_status_to_exit_status(499) == module_0.ExitStatus.ERROR_HTTP_4XX


def test_example_f8g4ucsp():
    assert module_0.http_status_to_exit_status(599) == module_0.ExitStatus.ERROR_HTTP_5XX


def test_example_xnyyh9xd():
    assert module_0.http_status_to_exit_status(300) == module_0.ExitStatus.ERROR_HTTP_3XX


