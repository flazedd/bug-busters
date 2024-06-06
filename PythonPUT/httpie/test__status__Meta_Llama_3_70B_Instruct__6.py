from enum import unique
from enum import IntEnum
import pytest
import status as module_0
def test_example_3uvh0wx6():
    assert module_0.http_status_to_exit_status(404) == module_0.ExitStatus.ERROR_HTTP_4XX


def test_example_sibc6g5h():
    assert module_0.http_status_to_exit_status(302, follow=True) == module_0.ExitStatus.SUCCESS


def test_example_ly6fa22i():
    assert module_0.http_status_to_exit_status(500) == module_0.ExitStatus.ERROR_HTTP_5XX


def test_example_woimp3xu():
    assert module_0.http_status_to_exit_status(200) == module_0.ExitStatus.SUCCESS


def test_example_j69v3102():
    assert module_0.http_status_to_exit_status(301) == module_0.ExitStatus.ERROR_HTTP_3XX


def test_example_jk4k1u9e():
    assert module_0.http_status_to_exit_status(400, follow=False) == module_0.ExitStatus.ERROR_HTTP_4XX


def test_example_86lpd2pg():
    assert module_0.http_status_to_exit_status(599) == module_0.ExitStatus.ERROR_HTTP_5XX


def test_example_862rio90():
    assert module_0.http_status_to_exit_status(399) == module_0.ExitStatus.ERROR_HTTP_3XX


