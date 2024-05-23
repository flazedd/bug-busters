# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import status as module_0
import enum as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 1792
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
    exit_status_1 = module_0.ExitStatus.ERROR_HTTP_5XX
    exit_status_2 = module_0.http_status_to_exit_status(exit_status_1)
    assert exit_status_2 == module_0.ExitStatus.SUCCESS
    none_type_0 = None
    module_0.http_status_to_exit_status(none_type_0)


def test_case_1():
    bool_0 = False
    exit_status_0 = module_0.http_status_to_exit_status(bool_0)
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


@pytest.mark.xfail(strict=True)
def test_case_2():
    exit_status_0 = module_0.ExitStatus.ERROR_TOO_MANY_REDIRECTS
    bool_0 = True
    exit_status_1 = module_0.http_status_to_exit_status(exit_status_0)
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
    exit_status_2 = module_0.http_status_to_exit_status(bool_0)
    assert exit_status_2 == module_0.ExitStatus.SUCCESS
    none_type_0 = None
    int_0 = 331
    exit_status_3 = module_0.http_status_to_exit_status(int_0)
    assert exit_status_3 == module_0.ExitStatus.ERROR_HTTP_3XX
    exit_status_4 = module_0.http_status_to_exit_status(int_0)
    assert exit_status_4 == module_0.ExitStatus.ERROR_HTTP_3XX
    exit_status_5 = module_0.ExitStatus.ERROR_HTTP_4XX
    int_1 = 1356
    exit_status_6 = module_0.http_status_to_exit_status(int_1)
    assert exit_status_6 == module_0.ExitStatus.SUCCESS
    exit_status_7 = module_0.http_status_to_exit_status(exit_status_5)
    assert exit_status_7 == module_0.ExitStatus.SUCCESS
    bool_1 = False
    exit_status_8 = module_0.http_status_to_exit_status(bool_1)
    assert exit_status_8 == module_0.ExitStatus.SUCCESS
    exit_status_9 = module_0.http_status_to_exit_status(exit_status_4)
    assert exit_status_9 == module_0.ExitStatus.SUCCESS
    int_2 = -3242
    exit_status_10 = module_0.http_status_to_exit_status(int_2, none_type_0)
    assert exit_status_10 == module_0.ExitStatus.SUCCESS
    module_1.unique(exit_status_1)


def test_case_3():
    int_0 = -113
    exit_status_0 = module_0.http_status_to_exit_status(int_0, int_0)
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
    int_1 = 499
    exit_status_1 = module_0.http_status_to_exit_status(int_1)
    assert exit_status_1 == module_0.ExitStatus.ERROR_HTTP_4XX
    exit_status_2 = module_0.ExitStatus.ERROR_TOO_MANY_REDIRECTS
    exit_status_3 = module_0.ExitStatus.ERROR_TIMEOUT
    exit_status_4 = module_0.http_status_to_exit_status(exit_status_0)
    assert exit_status_4 == module_0.ExitStatus.SUCCESS
    int_2 = 755
    bool_0 = False
    exit_status_5 = module_0.http_status_to_exit_status(bool_0)
    assert exit_status_5 == module_0.ExitStatus.SUCCESS
    bool_1 = True
    exit_status_6 = module_0.http_status_to_exit_status(bool_0, bool_1)
    assert exit_status_6 == module_0.ExitStatus.SUCCESS
    exit_status_7 = module_0.http_status_to_exit_status(exit_status_6)
    assert exit_status_7 == module_0.ExitStatus.SUCCESS
    exit_status_8 = module_0.http_status_to_exit_status(int_2, int_2)
    assert exit_status_8 == module_0.ExitStatus.SUCCESS
    exit_status_9 = module_0.ExitStatus.ERROR_HTTP_4XX
    exit_status_10 = module_0.http_status_to_exit_status(exit_status_6, exit_status_9)
    assert exit_status_10 == module_0.ExitStatus.SUCCESS
    exit_status_11 = module_0.http_status_to_exit_status(exit_status_2)
    assert exit_status_11 == module_0.ExitStatus.SUCCESS
    exit_status_12 = module_0.http_status_to_exit_status(exit_status_3)
    assert exit_status_12 == module_0.ExitStatus.SUCCESS
    exit_status_13 = module_0.ExitStatus.PLUGIN_ERROR
    exit_status_14 = module_0.http_status_to_exit_status(bool_0)
    assert exit_status_14 == module_0.ExitStatus.SUCCESS
    exit_status_15 = module_0.http_status_to_exit_status(exit_status_11)
    assert exit_status_15 == module_0.ExitStatus.SUCCESS
    exit_status_16 = module_0.http_status_to_exit_status(exit_status_6)
    assert exit_status_16 == module_0.ExitStatus.SUCCESS
    bool_2 = True
    exit_status_17 = module_0.http_status_to_exit_status(bool_2, int_0)
    assert exit_status_17 == module_0.ExitStatus.SUCCESS
    exit_status_18 = module_0.http_status_to_exit_status(exit_status_13)
    assert exit_status_18 == module_0.ExitStatus.SUCCESS


def test_case_4():
    exit_status_0 = module_0.ExitStatus.ERROR_TOO_MANY_REDIRECTS
    bool_0 = True
    exit_status_1 = module_0.http_status_to_exit_status(exit_status_0)
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
    exit_status_2 = module_0.http_status_to_exit_status(bool_0)
    assert exit_status_2 == module_0.ExitStatus.SUCCESS
    exit_status_3 = module_0.http_status_to_exit_status(bool_0, bool_0)
    assert exit_status_3 == module_0.ExitStatus.SUCCESS
    exit_status_4 = module_0.ExitStatus.ERROR_HTTP_3XX
    exit_status_5 = module_0.ExitStatus.ERROR_HTTP_5XX
    int_0 = 331
    exit_status_6 = module_0.http_status_to_exit_status(int_0)
    assert exit_status_6 == module_0.ExitStatus.ERROR_HTTP_3XX
    exit_status_7 = module_0.http_status_to_exit_status(int_0)
    assert exit_status_7 == module_0.ExitStatus.ERROR_HTTP_3XX
    exit_status_8 = module_0.ExitStatus.ERROR
    exit_status_9 = module_0.ExitStatus.ERROR_HTTP_4XX
    int_1 = 1356
    exit_status_10 = module_0.http_status_to_exit_status(int_1)
    assert exit_status_10 == module_0.ExitStatus.SUCCESS
    exit_status_11 = module_0.http_status_to_exit_status(exit_status_9)
    assert exit_status_11 == module_0.ExitStatus.SUCCESS
    bool_1 = False
    exit_status_12 = module_0.http_status_to_exit_status(bool_1)
    assert exit_status_12 == module_0.ExitStatus.SUCCESS
    exit_status_13 = module_0.http_status_to_exit_status(exit_status_7)
    assert exit_status_13 == module_0.ExitStatus.SUCCESS
    int_2 = 300
    exit_status_14 = module_0.http_status_to_exit_status(int_2, exit_status_4)
    assert exit_status_14 == module_0.ExitStatus.SUCCESS
    exit_status_15 = module_0.http_status_to_exit_status(exit_status_5)
    assert exit_status_15 == module_0.ExitStatus.SUCCESS
    exit_status_16 = module_0.http_status_to_exit_status(exit_status_6, exit_status_8)
    assert exit_status_16 == module_0.ExitStatus.SUCCESS


@pytest.mark.xfail(strict=True)
def test_case_5():
    exit_status_0 = module_0.ExitStatus.ERROR_TOO_MANY_REDIRECTS
    bool_0 = True
    exit_status_1 = module_0.http_status_to_exit_status(exit_status_0)
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
    exit_status_2 = module_0.http_status_to_exit_status(bool_0)
    assert exit_status_2 == module_0.ExitStatus.SUCCESS
    exit_status_3 = module_0.http_status_to_exit_status(bool_0, bool_0)
    assert exit_status_3 == module_0.ExitStatus.SUCCESS
    none_type_0 = None
    int_0 = 331
    exit_status_4 = module_0.http_status_to_exit_status(int_0)
    assert exit_status_4 == module_0.ExitStatus.ERROR_HTTP_3XX
    exit_status_5 = module_0.http_status_to_exit_status(int_0)
    assert exit_status_5 == module_0.ExitStatus.ERROR_HTTP_3XX
    exit_status_6 = module_0.ExitStatus.ERROR_HTTP_4XX
    int_1 = 1356
    exit_status_7 = module_0.http_status_to_exit_status(int_1)
    assert exit_status_7 == module_0.ExitStatus.SUCCESS
    exit_status_8 = module_0.http_status_to_exit_status(exit_status_6)
    assert exit_status_8 == module_0.ExitStatus.SUCCESS
    int_2 = 540
    exit_status_9 = module_0.http_status_to_exit_status(int_2)
    assert exit_status_9 == module_0.ExitStatus.ERROR_HTTP_5XX
    module_0.http_status_to_exit_status(none_type_0)
