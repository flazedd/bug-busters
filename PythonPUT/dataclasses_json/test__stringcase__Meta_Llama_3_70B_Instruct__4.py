import re
import stringcase as module_0
import pytest
def test_example_3eoqco0n():
    assert module_0.camelcase('hello-world') == 'helloWorld'





def test_example_1hdqixb2():
    assert module_0.pascalcase('hello world') == 'HelloWorld'





def test_example_a93ibj7x():
    assert module_0.uplowcase('HeLlO', 'low') == 'hello'





def test_example_34f72afb():
    assert module_0.capitalcase('hello world') == 'Hello world'





def test_example_83kygc04():
    assert module_0.camelcase('hello_world') == 'helloWorld'


def test_example_gk7rg2ep():
    assert module_0.snakecase('HelloWorld') == 'hello_world'


def test_example_pc86st27():
    assert module_0.pascalcase('hello world') == 'HelloWorld'


def test_example_rf7zph10():
    assert module_0.uplowcase('HeLlO', 'up') == 'HELLO'


