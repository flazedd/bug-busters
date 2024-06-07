# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import status as module_0


def test_case_0():
    exit_status_0 = module_0.ExitStatus.ERROR_TOO_MANY_REDIRECTS
    int_0 = 2396
    exit_status_1 = module_0.http_status_to_exit_status(int_0, exit_status_0)
    assert exit_status_1 == module_0.ExitStatus.SUCCESS
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
    int_0 = 284
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


def test_case_2():
    pass


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 313
    bool_0 = False
    exit_status_0 = module_0.http_status_to_exit_status(bool_0, bool_0)
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
    none_type_0 = None
    exit_status_1 = module_0.http_status_to_exit_status(int_0)
    assert exit_status_1 == module_0.ExitStatus.ERROR_HTTP_3XX
    module_0.http_status_to_exit_status(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = -3898
    int_1 = 450
    exit_status_0 = module_0.http_status_to_exit_status(int_1)
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
    dict_0 = {int_0: int_0}
    module_0.http_status_to_exit_status(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    int_0 = 1713
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
    exit_status_1 = module_0.ExitStatus.ERROR_TIMEOUT
    int_1 = -3169
    exit_status_2 = module_0.http_status_to_exit_status(exit_status_1, exit_status_0)
    assert exit_status_2 == module_0.ExitStatus.SUCCESS
    exit_status_3 = module_0.ExitStatus.ERROR
    exit_status_4 = module_0.http_status_to_exit_status(int_1, exit_status_3)
    assert exit_status_4 == module_0.ExitStatus.SUCCESS
    int_2 = 562
    exit_status_5 = module_0.http_status_to_exit_status(int_2, int_0)
    assert exit_status_5 == module_0.ExitStatus.ERROR_HTTP_5XX
    none_type_0 = None
    exit_status_6 = module_0.http_status_to_exit_status(int_2)
    assert exit_status_6 == module_0.ExitStatus.ERROR_HTTP_5XX
    module_0.http_status_to_exit_status(none_type_0, exit_status_4)


def test_case_6():
    int_0 = 1820
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
    exit_status_1 = module_0.http_status_to_exit_status(int_0)
    assert exit_status_1 == module_0.ExitStatus.SUCCESS
    exit_status_2 = module_0.ExitStatus.ERROR_HTTP_5XX
    bool_0 = False
    exit_status_3 = module_0.http_status_to_exit_status(bool_0)
    assert exit_status_3 == module_0.ExitStatus.SUCCESS
    exit_status_4 = module_0.http_status_to_exit_status(exit_status_0)
    assert exit_status_4 == module_0.ExitStatus.SUCCESS
    exit_status_5 = module_0.http_status_to_exit_status(exit_status_2)
    assert exit_status_5 == module_0.ExitStatus.SUCCESS
    exit_status_6 = module_0.ExitStatus.ERROR_TOO_MANY_REDIRECTS
    int_1 = 316
    exit_status_7 = module_0.http_status_to_exit_status(int_1)
    assert exit_status_7 == module_0.ExitStatus.ERROR_HTTP_3XX
    exit_status_8 = module_0.http_status_to_exit_status(exit_status_3, exit_status_6)
    assert exit_status_8 == module_0.ExitStatus.SUCCESS
    exit_status_9 = module_0.ExitStatus.SUCCESS
    exit_status_10 = module_0.ExitStatus.ERROR_TIMEOUT
    exit_status_11 = module_0.ExitStatus.ERROR_HTTP_3XX
    bool_1 = False
    exit_status_12 = module_0.http_status_to_exit_status(bool_1)
    assert exit_status_12 == module_0.ExitStatus.SUCCESS
    exit_status_13 = module_0.http_status_to_exit_status(exit_status_10, exit_status_9)
    assert exit_status_13 == module_0.ExitStatus.SUCCESS
    int_2 = 997
    exit_status_14 = module_0.http_status_to_exit_status(int_2)
    assert exit_status_14 == module_0.ExitStatus.SUCCESS
    exit_status_15 = module_0.http_status_to_exit_status(exit_status_3)
    assert exit_status_15 == module_0.ExitStatus.SUCCESS
    exit_status_16 = module_0.http_status_to_exit_status(exit_status_10)
    assert exit_status_16 == module_0.ExitStatus.SUCCESS
    int_3 = 2524
    exit_status_17 = module_0.http_status_to_exit_status(int_3)
    assert exit_status_17 == module_0.ExitStatus.SUCCESS
    exit_status_18 = module_0.http_status_to_exit_status(int_1, exit_status_10)
    assert exit_status_18 == module_0.ExitStatus.SUCCESS
    exit_status_19 = module_0.http_status_to_exit_status(exit_status_11)
    assert exit_status_19 == module_0.ExitStatus.SUCCESS