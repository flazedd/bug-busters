import keyword
import validators as module_0
from typing import Union
from collections import UserString
import pytest
def test_example_r9nzwopq():
    try:
        module_0.validate_identifier('valid_identifier')
    except Exception:
        assert False, "Expected 'valid_identifier' to be a valid identifier"
    else:
        assert True


def test_example_58l57tqz():
    try:
        module_0.validate_identifier('123invalid')
    except SyntaxError:
        assert True
    else:
        assert False, "Expected '123invalid' to raise a SyntaxError"


def test_example_or3z8fqn():
    try:
        module_0.validate_identifier('__builtin__', allow_underscore=False)
    except SyntaxError:
        assert True
    else:
        assert False, "Expected '__builtin__' to raise a SyntaxError when allow_underscore=False"


def test_example_luful8gu():
    try:
        module_0.validate_identifier('True')
    except SyntaxError:
        assert True
    else:
        assert False, "Expected 'True' to raise a SyntaxError because it's a keyword"


def test_example_siga6r5r():
    try:
        module_0.validate_identifier('')
    except SyntaxError:
        assert True
    else:
        assert False, "Expected '' to raise a SyntaxError because it's an empty string"


def test_example_cy810coz():
    try:
        module_0.validate_identifier('_private', allow_underscore=False)
    except SyntaxError:
        assert True
    else:
        assert False, "Expected '_private' to raise a SyntaxError when allow_underscore=False"


def test_example_gjv4virm():
    try:
        module_0.validate_identifier(None)
    except TypeError:
        assert True
    else:
        assert False, "Expected None to raise a TypeError because it's not a string"


def test_example_7gatfmt5():
    try:
        module_0.validate_identifier(123)
    except TypeError:
        assert True
    else:
        assert False, "Expected 123 to raise a TypeError because it's not a string"


