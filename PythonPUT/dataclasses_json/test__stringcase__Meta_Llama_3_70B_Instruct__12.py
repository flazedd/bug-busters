import pytest
import re
import stringcase as module_0
def test_example_fdbwivwc():
    assert module_0.camelcase('hello-world') == 'helloWorld'


def test_example_f5z9lpr3():
    assert module_0.pascalcase('hello world') == 'HelloWorld'


def test_example_rdrnov38():
    assert module_0.uplowcase('HELLO', 'low') == 'hello'


def test_example_wuer4qya():
    assert module_0.capitalcase('hello world') == 'Hello world'


def test_example_fw6hh2bm():
    assert module_0.uplowcase('hello', 'up') == 'HELLO'


def test_example_84a8k4xw():
    assert module_0.camelcase('hello world') == 'helloWorld'


def test_example_3r90ssjw():
    assert module_0.pascalcase('hello-world') == 'HelloWorld'


def test_example_d20978zs():
    assert module_0.uplowcase('hELLO', 'low') == 'hello'


