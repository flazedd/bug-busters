import stringcase as module_0
import pytest
import re
def test_example_2nm7bbtw():
    assert module_0.camelcase('hello_world') == 'helloWorld'


def test_example_83v6uln3():
    assert module_0.snakecase('HelloWorld') == 'hello_world'


def test_example_xfp15ji8():
    assert module_0.spinalcase('HelloWorld') == 'hello-world'


def test_example_gda8uueq():
    assert module_0.pascalcase('hello_world') == 'HelloWorld'


def test_example_rz0y6w8b():
    assert module_0.capitalcase('hello') == 'Hello'


def test_example_evpfixri():
    assert module_0.uplowcase('HELLO', 'low') == 'hello'


def test_example_frcbohon():
    assert module_0.uplowcase('hello', 'up') == 'HELLO'


def test_example_weuv78tq():
    assert module_0.camelcase('hello world') == 'helloWorld'


