import pytest
from collections import UserString
import validators as module_0
import keyword
from typing import Union
def test_example_tmlh13fw():
    module_0.validate_identifier('valid_identifier')
    assert True


def test_example_gs3ypee2():
    try:
        module_0.validate_identifier('123invalid')
    except SyntaxError:
        assert True
    else:
        assert False


def test_example_gw8i9ns2():
    try:
        module_0.validate_identifier('invalid_identifier@')
    except SyntaxError:
        assert True
    else:
        assert False


def test_example_tqrgmdyp():
    try:
        module_0.validate_identifier('True')
    except SyntaxError:
        assert True
    else:
        assert False


def test_example_xk9g6aqz():
    try:
        module_0.validate_identifier('_private')
    except SyntaxError:
        assert False
    else:
        assert True


def test_example_ntab7yhn():
    try:
        module_0.validate_identifier('_private', allow_underscore=False)
    except SyntaxError:
        assert True
    else:
        assert False


def test_example_td0xlri6():
    try:
        module_0.validate_identifier(None)
    except TypeError:
        assert True
    else:
        assert False


def test_example_lwv0o53u():
    try:
        module_0.validate_identifier(123)
    except TypeError:
        assert True
    else:
        assert False


