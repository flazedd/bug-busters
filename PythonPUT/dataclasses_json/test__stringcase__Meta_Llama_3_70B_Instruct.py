import stringcase as module_0
import re
import pytest
def test_example_2g7jq5iu():
    assert module_0.camelcase('hello_world') == 'helloWorld'


def test_example_uihyhb8b():
    assert module_0.spinalcase('HelloWorld') == 'hello-world'


def test_example_rpb3wxxy():
    assert module_0.pascalcase('hello world') == 'HelloWorld'


def test_example_2w7fbiul():
    assert module_0.snakecase('Hello World') == 'hello__world'


def test_example_4t50z27y():
    assert module_0.capitalcase('hello world') == 'Hello world'


def test_example_wobe7hoz():
    assert module_0.uplowcase('HeLlO', 'low') == 'hello'


def test_example_yugdvkwl():
    assert module_0.uplowcase('hello', 'up') == 'HELLO'


def test_example_f1s8yhw2():
    assert module_0.camelcase('hello-world') == 'helloWorld'


