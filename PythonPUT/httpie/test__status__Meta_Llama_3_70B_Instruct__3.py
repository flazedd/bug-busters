import status as module_0
from enum import IntEnum
from enum import unique
import pytest
def test_http_status_to_exit_status_kil3fy0z():
    assert module_0.http_status_to_exit_status(404) == module_0.ExitStatus.ERROR_HTTP_4XX


def test_http_status_to_exit_status_follow_08uqr89b():
    assert module_0.http_status_to_exit_status(301, follow=True) == module_0.ExitStatus.SUCCESS


def test_http_status_to_exit_status_500_c9wj3yqv():
    assert module_0.http_status_to_exit_status(500) == module_0.ExitStatus.ERROR_HTTP_5XX


def test_http_status_to_exit_status_200_j5ddi91s():
    assert module_0.http_status_to_exit_status(200) == module_0.ExitStatus.SUCCESS


def test_http_status_to_exit_status_302_q0wik1ng():
    assert module_0.http_status_to_exit_status(302) == module_0.ExitStatus.ERROR_HTTP_3XX


def test_http_status_to_exit_status_600_sz82v5l3():
    assert module_0.http_status_to_exit_status(600) == module_0.ExitStatus.SUCCESS


def test_http_status_to_exit_status_ctrl_c_9idj9nu4():
    assert module_0.ExitStatus.ERROR_CTRL_C == 130


def test_exit_status_success_v1bc43bs():
    assert module_0.ExitStatus.SUCCESS == 0


