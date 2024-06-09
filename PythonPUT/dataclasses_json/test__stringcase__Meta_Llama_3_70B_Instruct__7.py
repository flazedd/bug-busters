import pytest
import stringcase as module_0
import re
def test_example_x8nms64g():
    assert module_0.camelcase('hello_world') == 'helloWorld'


def test_example_49jpmkht():
    assert module_0.snakecase('HelloWorld') == 'hello_world'


def test_example_vzpmmvyi():
    assert module_0.spinalcase('HelloWorld') == 'hello-world'


def test_example_s3k4rnrx():
    assert module_0.pascalcase('hello_world') == 'HelloWorld'


def test_example_xc0flomf():
    assert module_0.capitalcase('hello world') == 'Hello world'


def test_example_rxnoi5ny():
    assert module_0.uplowcase('HeLlO', 'low') == 'hello'


def test_example_j23jkc1m():
    assert module_0.uplowcase('HeLlO', 'up') == 'HELLO'


def test_example_2kgw4c1k():
    assert module_0.camelcase('hello world') == 'helloWorld'


