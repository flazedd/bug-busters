from enum import unique
import status as module_0
import pytest
from enum import IntEnum
def test_example_bjlnhrcv():
    assert module_0.http_status_to_exit_status(404) == module_0.ExitStatus.ERROR_HTTP_4XX


def test_example_76u76qkj():
    assert module_0.http_status_to_exit_status(302) == module_0.ExitStatus.ERROR_HTTP_3XX


def test_example_polg3wyw():
    assert module_0.http_status_to_exit_status(500) == module_0.ExitStatus.ERROR_HTTP_5XX


def test_example_pdo16iku():
    assert module_0.http_status_to_exit_status(200) == module_0.ExitStatus.SUCCESS


def test_example_jpwp22ta():
    assert module_0.http_status_to_exit_status(301, follow=True) == module_0.ExitStatus.SUCCESS


def test_example_vwbqr9yt():
    assert module_0.http_status_to_exit_status(600) == module_0.ExitStatus.SUCCESS


def test_example_h64s0s2v():
    assert module_0.ExitStatus.ERROR_CTRL_C == module_0.ExitStatus(130)


def test_example_phd98saz():
    assert module_0.http_status_to_exit_status(401) == module_0.ExitStatus.ERROR_HTTP_4XX


