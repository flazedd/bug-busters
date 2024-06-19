import pytest
import re
import stringcase as module_0
def test_example_g36qc54k():
    assert module_0.camelcase('hello world') == 'helloWorld'


def test_example_pls3xc3q():
    assert module_0.snakecase('HelloWorld') == 'hello_world'


def test_example_qn5jryam():
    assert module_0.pascalcase('hello world') == 'HelloWorld'


def test_example_1biv6fpx():
    assert module_0.uplowcase('HeLlO', 'low') == 'hello'


def test_example_e7bd80hm():
    assert module_0.capitalcase('hello world') == 'Hello world'


def test_example_o1azxcfs():
    assert module_0.uplowcase('HeLlO', 'up') == 'HELLO'


def test_example_uwwyhk0l():
    assert module_0.camelcase('hello-world') == 'helloWorld'


def test_example_goxalh76():
    assert module_0.capitalcase('hello WORLD') == 'Hello WORLD'


