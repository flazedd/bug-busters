import pytest
import status as module_0
from enum import IntEnum
from enum import unique
def test_example_o3eghsau():
    assert module_0.http_status_to_exit_status(404) == module_0.ExitStatus.ERROR_HTTP_4XX


def test_example_m1qscrgb():
    assert module_0.http_status_to_exit_status(302, follow=True) == module_0.ExitStatus.SUCCESS


def test_example_mwuifvw5():
    assert module_0.http_status_to_exit_status(500) == module_0.ExitStatus.ERROR_HTTP_5XX


def test_example_fiar5msy():
    assert module_0.http_status_to_exit_status(200) == module_0.ExitStatus.SUCCESS


def test_example_jw8nm0qd():
    assert module_0.http_status_to_exit_status(301) == module_0.ExitStatus.ERROR_HTTP_3XX


def test_example_xlkuvdbw():
    assert module_0.http_status_to_exit_status(400, follow=True) == module_0.ExitStatus.ERROR_HTTP_4XX


def test_example_6xeflw7f():
    assert module_0.http_status_to_exit_status(502) == module_0.ExitStatus.ERROR_HTTP_5XX


def test_example_eqpw6el8():
    assert module_0.http_status_to_exit_status(399, follow=True) == module_0.ExitStatus.SUCCESS


