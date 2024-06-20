from enum import IntEnum
import pytest
from enum import unique
import status as module_0
def test_example_2yge6rpo():
    assert module_0.http_status_to_exit_status(404) == module_0.ExitStatus.ERROR_HTTP_4XX


def test_example_wbk6yyv6():
    assert module_0.http_status_to_exit_status(302, follow=True) == module_0.ExitStatus.SUCCESS


def test_example_u9v6zoif():
    assert module_0.http_status_to_exit_status(500) == module_0.ExitStatus.ERROR_HTTP_5XX


def test_example_1ksgsy83():
    assert module_0.http_status_to_exit_status(200) == module_0.ExitStatus.SUCCESS


def test_example_4xuvshkj():
    assert module_0.http_status_to_exit_status(301, follow=True) == module_0.ExitStatus.SUCCESS


def test_example_zzfjfkhy():
    assert module_0.http_status_to_exit_status(502) == module_0.ExitStatus.ERROR_HTTP_5XX


def test_example_f5ofbvek():
    assert module_0.ExitStatus.ERROR_CTRL_C == 130


def test_example_n4uigje4():
    assert module_0.http_status_to_exit_status(401) == module_0.ExitStatus.ERROR_HTTP_4XX


