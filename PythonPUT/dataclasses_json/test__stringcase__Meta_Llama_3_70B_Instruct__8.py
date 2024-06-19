import pytest
import re
import stringcase as module_0
def test_example_k8qii9p9():
    assert module_0.camelcase('hello world') == 'helloWorld'


def test_example_9kdxe41i():
    assert module_0.pascalcase('hello world') == 'HelloWorld'


def test_example_dhs4ws1o():
    assert module_0.uplowcase('Hello World', 'low') == 'hello world'


def test_example_g0hbtcku():
    assert module_0.capitalcase('hello world') == 'Hello world'


def test_example_mzgelr0s():
    assert module_0.camelcase('hello-world') == 'helloWorld'


def test_example_btk8sx19():
    assert module_0.uplowcase('HELLO WORLD', 'up') == 'HELLO WORLD'


def test_example_htips4ck():
    assert module_0.pascalcase('hello_world') == 'HelloWorld'


def test_example_gmrneixm():
    assert module_0.camelcase('hello_world') == 'helloWorld'


