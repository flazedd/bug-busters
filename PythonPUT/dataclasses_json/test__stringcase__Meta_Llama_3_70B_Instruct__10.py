import re
import stringcase as module_0
import pytest
def test_example_69hfh88j():
    assert module_0.camelcase('hello world') == 'helloWorld'


def test_example_kaa0gj57():
    assert module_0.pascalcase('hello world') == 'HelloWorld'


def test_example_z7e6krp9():
    assert module_0.uplowcase('HeLlO', 'low') == 'hello'


def test_example_lmuces5z():
    assert module_0.capitalcase('hello world') == 'Hello world'


def test_example_cw46gdc0():
    assert module_0.camelcase('hello-world') == 'helloWorld'


def test_example_pke0y3s5():
    assert module_0.snakecase('HelloWorld') == 'hello_world'


def test_example_neke0r5n():
    assert module_0.uplowcase('HELLO', 'up') == 'HELLO'


def test_example_iripabt2():
    assert module_0.pascalcase('hello_world') == 'HelloWorld'


