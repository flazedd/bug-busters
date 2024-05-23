import status as module_0
import pytest
from enum import IntEnum
from enum import unique
def test_example_igdkb93b():
    assert module_0.http_status_to_exit_status(200) == module_0.ExitStatus.SUCCESS


def test_example_gelmi08c():
    assert module_0.http_status_to_exit_status(404) == module_0.ExitStatus.ERROR_HTTP_4XX


def test_example_2baxdfxf():
    assert module_0.http_status_to_exit_status(500) == module_0.ExitStatus.ERROR_HTTP_5XX


def test_example_w0vjbm5s():
    assert module_0.http_status_to_exit_status(302) == module_0.ExitStatus.ERROR_HTTP_3XX


def test_example_o9efo4xa():
    assert module_0.http_status_to_exit_status(401) == module_0.ExitStatus.ERROR_HTTP_4XX


def test_example_qz9zemjz():
    assert module_0.http_status_to_exit_status(503) == module_0.ExitStatus.ERROR_HTTP_5XX


def test_example_h2660uzg():
    assert module_0.http_status_to_exit_status(300) == module_0.ExitStatus.ERROR_HTTP_3XX


def test_example_ed00shnt():
    assert module_0.http_status_to_exit_status(100) == module_0.ExitStatus.SUCCESS


