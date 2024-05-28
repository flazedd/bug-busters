import stringcase as module_0
import re
import pytest
def test_camelcase_tbxdaysq():
    assert module_0.camelcase('hello_world') == 'helloWorld'





def test_pascalcase_z9plp88m():
    assert module_0.pascalcase('hello world') == 'HelloWorld'





def test_uplowcase_igrhg5o9():
    assert module_0.uplowcase('HeLlO', 'up') == 'HELLO'





def test_uplowcase_low_qlmdlovv():
    assert module_0.uplowcase('HeLlO', 'low') == 'hello'





def test_camelcase_with_underscores_aczlsjnw():
    assert module_0.camelcase('hello_world') == 'helloWorld'





def test_camelcase_with_dashes_5lw667k6():
    assert module_0.camelcase('hello-world') == 'helloWorld'





def test_spinalcase_with_underscores_5do8iswb():
    assert module_0.spinalcase('hello_world') == 'hello-world'





def test_camelcase_nxmzpzhc():
    assert module_0.camelcase('hello_world') == 'helloWorld'


