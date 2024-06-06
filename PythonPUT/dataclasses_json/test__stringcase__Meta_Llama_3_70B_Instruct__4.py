import stringcase as module_0
import re
import pytest
def test_example_3eoqco0n():
    assert module_0.camelcase('hello-world') == 'helloWorld'


def test_example_1hdqixb2():
    assert module_0.pascalcase('hello world') == 'HelloWorld'


def test_example_a93ibj7x():
    assert module_0.uplowcase('HeLlO', 'low') == 'hello'


def test_example_34f72afb():
    assert module_0.capitalcase('hello world') == 'Hello world'


def test_example_ur2v4j4b():
    assert module_0.camelcase('hello_World-abc.def-ghi.jkl-mno.pqr-stu.vwx.yz-abc.def-ghi.jkl-mno.pqr-stu.vwx.yz') == 'helloWorldAbcDefGhiJklMnoPqrStuVwxYzAbcDefGhiJklMnoPqrStuVwxYz'


