# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import status as module_0
import enum as module_1


def test_case_0():
    int_0 = 714
    exit_status_0 = module_0.http_status_to_exit_status(int_0)
    assert exit_status_0 == module_0.ExitStatus.SUCCESS
    assert module_0.ExitStatus.SUCCESS == module_0.ExitStatus.SUCCESS
    assert module_0.ExitStatus.ERROR == module_0.ExitStatus.ERROR
    assert module_0.ExitStatus.ERROR_TIMEOUT == module_0.ExitStatus.ERROR_TIMEOUT
    assert module_0.ExitStatus.ERROR_HTTP_3XX == module_0.ExitStatus.ERROR_HTTP_3XX
    assert module_0.ExitStatus.ERROR_HTTP_4XX == module_0.ExitStatus.ERROR_HTTP_4XX
    assert module_0.ExitStatus.ERROR_HTTP_5XX == module_0.ExitStatus.ERROR_HTTP_5XX
    assert (
        module_0.ExitStatus.ERROR_TOO_MANY_REDIRECTS
        == module_0.ExitStatus.ERROR_TOO_MANY_REDIRECTS
    )
    assert module_0.ExitStatus.PLUGIN_ERROR == module_0.ExitStatus.PLUGIN_ERROR
    assert module_0.ExitStatus.ERROR_CTRL_C == module_0.ExitStatus.ERROR_CTRL_C


def test_case_1():
    float_0 = -1207.1
    exit_status_0 = module_0.http_status_to_exit_status(float_0, float_0)
    assert exit_status_0 == module_0.ExitStatus.SUCCESS
    assert module_0.ExitStatus.SUCCESS == module_0.ExitStatus.SUCCESS
    assert module_0.ExitStatus.ERROR == module_0.ExitStatus.ERROR
    assert module_0.ExitStatus.ERROR_TIMEOUT == module_0.ExitStatus.ERROR_TIMEOUT
    assert module_0.ExitStatus.ERROR_HTTP_3XX == module_0.ExitStatus.ERROR_HTTP_3XX
    assert module_0.ExitStatus.ERROR_HTTP_4XX == module_0.ExitStatus.ERROR_HTTP_4XX
    assert module_0.ExitStatus.ERROR_HTTP_5XX == module_0.ExitStatus.ERROR_HTTP_5XX
    assert (
        module_0.ExitStatus.ERROR_TOO_MANY_REDIRECTS
        == module_0.ExitStatus.ERROR_TOO_MANY_REDIRECTS
    )
    assert module_0.ExitStatus.PLUGIN_ERROR == module_0.ExitStatus.PLUGIN_ERROR
    assert module_0.ExitStatus.ERROR_CTRL_C == module_0.ExitStatus.ERROR_CTRL_C


def test_case_2():
    pass


def test_case_3():
    int_0 = 397
    exit_status_0 = module_0.http_status_to_exit_status(int_0)
    assert exit_status_0 == module_0.ExitStatus.ERROR_HTTP_3XX
    assert module_0.ExitStatus.SUCCESS == module_0.ExitStatus.SUCCESS
    assert module_0.ExitStatus.ERROR == module_0.ExitStatus.ERROR
    assert module_0.ExitStatus.ERROR_TIMEOUT == module_0.ExitStatus.ERROR_TIMEOUT
    assert module_0.ExitStatus.ERROR_HTTP_3XX == module_0.ExitStatus.ERROR_HTTP_3XX
    assert module_0.ExitStatus.ERROR_HTTP_4XX == module_0.ExitStatus.ERROR_HTTP_4XX
    assert module_0.ExitStatus.ERROR_HTTP_5XX == module_0.ExitStatus.ERROR_HTTP_5XX
    assert (
        module_0.ExitStatus.ERROR_TOO_MANY_REDIRECTS
        == module_0.ExitStatus.ERROR_TOO_MANY_REDIRECTS
    )
    assert module_0.ExitStatus.PLUGIN_ERROR == module_0.ExitStatus.PLUGIN_ERROR
    assert module_0.ExitStatus.ERROR_CTRL_C == module_0.ExitStatus.ERROR_CTRL_C
    bool_0 = False
    exit_status_1 = module_0.http_status_to_exit_status(int_0, bool_0)
    assert exit_status_1 == module_0.ExitStatus.ERROR_HTTP_3XX


def test_case_4():
    bool_0 = False
    int_0 = 507
    exit_status_0 = module_0.http_status_to_exit_status(int_0)
    assert exit_status_0 == module_0.ExitStatus.ERROR_HTTP_5XX
    assert module_0.ExitStatus.SUCCESS == module_0.ExitStatus.SUCCESS
    assert module_0.ExitStatus.ERROR == module_0.ExitStatus.ERROR
    assert module_0.ExitStatus.ERROR_TIMEOUT == module_0.ExitStatus.ERROR_TIMEOUT
    assert module_0.ExitStatus.ERROR_HTTP_3XX == module_0.ExitStatus.ERROR_HTTP_3XX
    assert module_0.ExitStatus.ERROR_HTTP_4XX == module_0.ExitStatus.ERROR_HTTP_4XX
    assert module_0.ExitStatus.ERROR_HTTP_5XX == module_0.ExitStatus.ERROR_HTTP_5XX
    assert (
        module_0.ExitStatus.ERROR_TOO_MANY_REDIRECTS
        == module_0.ExitStatus.ERROR_TOO_MANY_REDIRECTS
    )
    assert module_0.ExitStatus.PLUGIN_ERROR == module_0.ExitStatus.PLUGIN_ERROR
    assert module_0.ExitStatus.ERROR_CTRL_C == module_0.ExitStatus.ERROR_CTRL_C
    exit_status_1 = module_0.http_status_to_exit_status(bool_0, bool_0)
    assert exit_status_1 == module_0.ExitStatus.SUCCESS


@pytest.mark.xfail(strict=True)
def test_case_5():
    int_0 = 305
    exit_status_0 = module_0.http_status_to_exit_status(int_0)
    assert exit_status_0 == module_0.ExitStatus.ERROR_HTTP_3XX
    assert module_0.ExitStatus.SUCCESS == module_0.ExitStatus.SUCCESS
    assert module_0.ExitStatus.ERROR == module_0.ExitStatus.ERROR
    assert module_0.ExitStatus.ERROR_TIMEOUT == module_0.ExitStatus.ERROR_TIMEOUT
    assert module_0.ExitStatus.ERROR_HTTP_3XX == module_0.ExitStatus.ERROR_HTTP_3XX
    assert module_0.ExitStatus.ERROR_HTTP_4XX == module_0.ExitStatus.ERROR_HTTP_4XX
    assert module_0.ExitStatus.ERROR_HTTP_5XX == module_0.ExitStatus.ERROR_HTTP_5XX
    assert (
        module_0.ExitStatus.ERROR_TOO_MANY_REDIRECTS
        == module_0.ExitStatus.ERROR_TOO_MANY_REDIRECTS
    )
    assert module_0.ExitStatus.PLUGIN_ERROR == module_0.ExitStatus.PLUGIN_ERROR
    assert module_0.ExitStatus.ERROR_CTRL_C == module_0.ExitStatus.ERROR_CTRL_C
    exit_status_1 = module_0.http_status_to_exit_status(int_0, int_0)
    assert exit_status_1 == module_0.ExitStatus.SUCCESS
    none_type_0 = None
    module_0.http_status_to_exit_status(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    int_0 = 400
    exit_status_0 = module_0.http_status_to_exit_status(int_0)
    assert exit_status_0 == module_0.ExitStatus.ERROR_HTTP_4XX
    assert module_0.ExitStatus.SUCCESS == module_0.ExitStatus.SUCCESS
    assert module_0.ExitStatus.ERROR == module_0.ExitStatus.ERROR
    assert module_0.ExitStatus.ERROR_TIMEOUT == module_0.ExitStatus.ERROR_TIMEOUT
    assert module_0.ExitStatus.ERROR_HTTP_3XX == module_0.ExitStatus.ERROR_HTTP_3XX
    assert module_0.ExitStatus.ERROR_HTTP_4XX == module_0.ExitStatus.ERROR_HTTP_4XX
    assert module_0.ExitStatus.ERROR_HTTP_5XX == module_0.ExitStatus.ERROR_HTTP_5XX
    assert (
        module_0.ExitStatus.ERROR_TOO_MANY_REDIRECTS
        == module_0.ExitStatus.ERROR_TOO_MANY_REDIRECTS
    )
    assert module_0.ExitStatus.PLUGIN_ERROR == module_0.ExitStatus.PLUGIN_ERROR
    assert module_0.ExitStatus.ERROR_CTRL_C == module_0.ExitStatus.ERROR_CTRL_C
    module_1.unique(int_0)