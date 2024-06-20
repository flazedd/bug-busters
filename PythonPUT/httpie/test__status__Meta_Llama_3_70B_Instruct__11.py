from enum import IntEnum
import pytest
from enum import unique
import status as module_0
def test_example_uy0x2w8t():
    assert module_0.http_status_to_exit_status(404) == module_0.ExitStatus.ERROR_HTTP_4XX


def test_example_kswxiv4j():
    assert module_0.http_status_to_exit_status(302) == module_0.ExitStatus.ERROR_HTTP_3XX


def test_example_bw2y033d():
    assert module_0.http_status_to_exit_status(200) == module_0.ExitStatus.SUCCESS


def test_example_ub3fxkxz():
    assert module_0.http_status_to_exit_status(500) == module_0.ExitStatus.ERROR_HTTP_5XX


def test_example_gm9ssb12():
    assert module_0.http_status_to_exit_status(301, follow=True) == module_0.ExitStatus.SUCCESS


def test_example_6anahsl2():
    assert module_0.http_status_to_exit_status(600) == module_0.ExitStatus.SUCCESS


def test_example_v8dd228v():
    assert module_0.ExitStatus.ERROR_CTRL_C == module_0.ExitStatus(130)


def test_example_e1brn6wc():
    assert module_0.http_status_to_exit_status(401) == module_0.ExitStatus.ERROR_HTTP_4XX


