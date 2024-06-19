import keyword
import pytest
import validators as module_0
from collections import UserString
from typing import Union
def test_example_e53seirp():
    try:
        module_0.validate_identifier('valid_identifier')
    except Exception as e:
        assert False, f'Unexpected exception: {e}'
    else:
        assert True


def test_example_z05msntd():
    try:
        module_0.validate_identifier('123_invalid')
    except SyntaxError as e:
        assert str(e) == "The given 'identifier', '123_invalid', cannot start with a number"
    else:
        assert False, 'Expected SyntaxError not raised'


def test_example_wb196uxo():
    try:
        module_0.validate_identifier('_private', allow_underscore=False)
    except SyntaxError as e:
        assert str(e) == "The given 'identifier', '_private', cannot start with an underscore '_'"
    else:
        assert False, 'Expected SyntaxError not raised'


def test_example_tfa588dg():
    try:
        module_0.validate_identifier('True')
    except SyntaxError as e:
        assert str(e) == "The given 'identifier', 'True', cannot be a keyword"
    else:
        assert False, 'Expected SyntaxError not raised'


def test_example_pgc9cv4e():
    try:
        module_0.validate_identifier('__builtins__', allow_underscore=True)
    except Exception as e:
        assert False, f'Unexpected exception: {e}'
    else:
        assert True


def test_example_dgkkyg4a():
    try:
        module_0.validate_identifier('')
    except SyntaxError as e:
        assert str(e) == "The given 'identifier' cannot be empty"
    else:
        assert False, 'Expected SyntaxError not raised'


def test_example_r9qcz106():
    try:
        module_0.validate_identifier('invalid identifier')
    except SyntaxError as e:
        assert str(e) == "The given 'identifier', 'invalid identifier', is invalid."
    else:
        assert False, 'Expected SyntaxError not raised'


def test_example_yy4kknar():
    try:
        module_0.validate_identifier('a' * 1000)
    except Exception as e:
        assert False, f'Unexpected exception: {e}'
    else:
        assert True


