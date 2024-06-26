# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import status as module_0


def test_case_0():
    int_0 = 1151
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


def test_case_2():
    int_0 = 708
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
    int_1 = 300
    exit_status_1 = module_0.http_status_to_exit_status(int_1)
    assert exit_status_1 == module_0.ExitStatus.ERROR_HTTP_3XX


def test_case_3():
    int_0 = 708
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
    exit_status_1 = module_0.http_status_to_exit_status(exit_status_0, exit_status_0)
    assert exit_status_1 == module_0.ExitStatus.SUCCESS
    exit_status_2 = module_0.ExitStatus.ERROR_TIMEOUT
    int_1 = 4495
    exit_status_3 = module_0.http_status_to_exit_status(exit_status_2)
    assert exit_status_3 == module_0.ExitStatus.SUCCESS
    exit_status_4 = module_0.ExitStatus.ERROR_TIMEOUT
    exit_status_5 = module_0.http_status_to_exit_status(exit_status_0)
    assert exit_status_5 == module_0.ExitStatus.SUCCESS
    exit_status_6 = module_0.http_status_to_exit_status(exit_status_2, int_1)
    assert exit_status_6 == module_0.ExitStatus.SUCCESS
    exit_status_7 = module_0.http_status_to_exit_status(exit_status_3)
    assert exit_status_7 == module_0.ExitStatus.SUCCESS
    int_2 = -441
    exit_status_8 = module_0.http_status_to_exit_status(int_2, exit_status_4)
    assert exit_status_8 == module_0.ExitStatus.SUCCESS
    exit_status_9 = module_0.ExitStatus.ERROR_CTRL_C
    exit_status_10 = module_0.http_status_to_exit_status(exit_status_3, exit_status_9)
    assert exit_status_10 == module_0.ExitStatus.SUCCESS
    int_3 = 38
    exit_status_11 = module_0.http_status_to_exit_status(int_3, exit_status_8)
    assert exit_status_11 == module_0.ExitStatus.SUCCESS
    exit_status_12 = module_0.http_status_to_exit_status(exit_status_11)
    assert exit_status_12 == module_0.ExitStatus.SUCCESS
    int_4 = 499
    exit_status_13 = module_0.http_status_to_exit_status(int_4)
    assert exit_status_13 == module_0.ExitStatus.ERROR_HTTP_4XX
    int_5 = 761
    exit_status_14 = module_0.http_status_to_exit_status(int_5)
    assert exit_status_14 == module_0.ExitStatus.SUCCESS


def test_case_4():
    int_0 = 708
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
    bool_0 = False
    exit_status_1 = module_0.http_status_to_exit_status(int_0)
    assert exit_status_1 == module_0.ExitStatus.SUCCESS
    int_1 = 300
    exit_status_2 = module_0.http_status_to_exit_status(bool_0, bool_0)
    assert exit_status_2 == module_0.ExitStatus.SUCCESS
    exit_status_3 = module_0.ExitStatus.ERROR_HTTP_5XX
    exit_status_4 = module_0.http_status_to_exit_status(exit_status_3)
    assert exit_status_4 == module_0.ExitStatus.SUCCESS
    exit_status_5 = module_0.http_status_to_exit_status(int_1, exit_status_4)
    assert exit_status_5 == module_0.ExitStatus.ERROR_HTTP_3XX
    exit_status_6 = module_0.http_status_to_exit_status(bool_0)
    assert exit_status_6 == module_0.ExitStatus.SUCCESS
    exit_status_7 = module_0.http_status_to_exit_status(int_1, exit_status_3)
    assert exit_status_7 == module_0.ExitStatus.SUCCESS


def test_case_5():
    int_0 = 708
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
    exit_status_1 = module_0.http_status_to_exit_status(exit_status_0)
    assert exit_status_1 == module_0.ExitStatus.SUCCESS
    bool_0 = False
    exit_status_2 = module_0.http_status_to_exit_status(int_0, exit_status_0)
    assert exit_status_2 == module_0.ExitStatus.SUCCESS
    int_1 = 528
    exit_status_3 = module_0.http_status_to_exit_status(int_1, bool_0)
    assert exit_status_3 == module_0.ExitStatus.ERROR_HTTP_5XX
    exit_status_4 = module_0.ExitStatus.ERROR
    exit_status_5 = module_0.http_status_to_exit_status(exit_status_4)
    assert exit_status_5 == module_0.ExitStatus.SUCCESS
