import re
import stringcase as module_0
import pytest
def test_example():
    assert module_0.camelcase('hello_world') == 'helloWorld'


def test_example():
    assert module_0.spinalcase('Hello World') == 'hello--world'


