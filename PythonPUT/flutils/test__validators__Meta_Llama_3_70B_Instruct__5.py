from typing import Union
from collections import UserString
import pytest
import keyword
import validators as module_0
def test_example_ljcsaiol():
    try:
        module_0.validate_identifier('valid_identifier')
        assert True
    except SyntaxError:
        assert False


def test_example_d90g0e9e():
    try:
        module_0.validate_identifier('123_invalid')
        assert False
    except SyntaxError:
        assert True


def test_example_pk2z2jvk():
    try:
        module_0.validate_identifier('_private_identifier', allow_underscore=False)
        assert False
    except SyntaxError:
        assert True


def test_example_eqj07j36():
    try:
        module_0.validate_identifier('True')
        assert False
    except SyntaxError:
        assert True


def test_example_k5ub9qnt():
    try:
        module_0.validate_identifier('')
        assert False
    except SyntaxError:
        assert True


def test_example_0uml5i5x():
    try:
        module_0.validate_identifier(123)
        assert False
    except TypeError:
        assert True


def test_example_z4c5ehcq():
    try:
        module_0.validate_identifier('async')
        assert False
    except SyntaxError:
        assert True


def test_example_quppdpei():
    try:
        module_0.validate_identifier('__builtins__', allow_underscore=True)
        assert True
    except SyntaxError:
        assert False


