import pytest
import re
import stringcase as module_0
def test_example_0p25ew7r():
    assert module_0.camelcase('hello world') == 'helloWorld'


def test_example_xp0oo8zm():
    assert module_0.snakecase('HelloWorld') == 'hello_world'


def test_example_p38mpwe3():
    assert module_0.spinalcase('HelloWorld') == 'hello-world'


def test_example_3ai3kw3r():
    assert module_0.pascalcase('hello world') == 'HelloWorld'


def test_example_utp23npt():
    assert module_0.uplowcase('HeLlO', 'up') == 'HELLO'


def test_example_qx5l9wb3():
    assert module_0.capitalcase('hello world') == 'Hello world'


def test_example_ra8e8a4k():
    assert module_0.uplowcase('HeLlO', 'low') == 'hello'


def test_example_bk6afxf0():
    assert module_0.uplowcase('HELLO', 'low') == 'hello'


