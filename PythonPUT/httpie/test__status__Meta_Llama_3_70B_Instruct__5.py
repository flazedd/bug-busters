from enum import IntEnum
import status as module_0
import pytest
from enum import unique
def test_http_status_to_exit_status_3b60ommi():
    assert module_0.http_status_to_exit_status(404) == module_0.ExitStatus.ERROR_HTTP_4XX





def test_http_status_to_exit_status_follow_redirect_uibdq6bg():
    assert module_0.http_status_to_exit_status(301, follow=True) == module_0.ExitStatus.SUCCESS





def test_http_status_to_exit_status_500_ohqic8e5():
    assert module_0.http_status_to_exit_status(500) == module_0.ExitStatus.ERROR_HTTP_5XX





def test_http_status_to_exit_status_200_vxwq97mb():
    assert module_0.http_status_to_exit_status(200) == module_0.ExitStatus.SUCCESS





def test_example_givl7sus():
    assert module_0.http_status_to_exit_status(404) == module_0.ExitStatus.ERROR_HTTP_4XX


def test_example_q2mywlnx():
    assert module_0.http_status_to_exit_status(502, follow=False) == module_0.ExitStatus.ERROR_HTTP_5XX


def test_example_389y4hkl():
    assert module_0.http_status_to_exit_status(301, follow=True) == module_0.ExitStatus.SUCCESS


def test_example_p9he8p9b():
    assert module_0.http_status_to_exit_status(200) == module_0.ExitStatus.SUCCESS


