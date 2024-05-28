import re
import stringcase as module_0
import pytest
def test_example_78feqh5a():
    assert module_0.camelcase('hello world') == 'helloWorld'


def test_example_oopwwfyq():
    assert module_0.pascalcase('hello world') == 'HelloWorld'


def test_example_mfgqpvpy():
    assert module_0.uplowcase('HeLlO', 'up') == 'HELLO'


def test_example_en1rv42e():
    assert module_0.capitalcase('hello world') == 'Hello world'


def test_example_807tsizi():
    assert module_0.uplowcase('HeLlO', 'low') == 'hello'


def test_example_974p4lif():
    assert module_0.camelcase('hello.world') == 'helloWorld'


def test_example_u1snorjm():
    assert module_0.pascalcase('hello_world') == 'HelloWorld'


def test_example_kvqvr7f3():
    assert module_0.camelcase('hello.world') == 'helloWorld'


