from typing import Union
import keyword
import validators as module_0
import pytest
from collections import UserString
def test_example_bzhvw9vq():
    module_0.validate_identifier('valid_identifier')
    assert True


def test_example_kvc6v3k4():
    try:
        module_0.validate_identifier('123_invalid')
    except SyntaxError:
        assert True


def test_example_ge3bs5ui():
    try:
        module_0.validate_identifier('class')
    except SyntaxError:
        assert True


def test_example_stze4e3f():
    try:
        module_0.validate_identifier('__builtins__')
    except SyntaxError:
        assert True


def test_example_7soiw5tk():
    try:
        module_0.validate_identifier('_private')
    except SyntaxError:
        assert False
    assert True


def test_example_fdl7iseg():
    try:
        module_0.validate_identifier('_private', allow_underscore=False)
    except SyntaxError:
        assert True


def test_example_89zpifdq():
    try:
        module_0.validate_identifier('')
    except SyntaxError:
        assert True


def test_example_3ecr9p1f():
    try:
        module_0.validate_identifier(123)
    except TypeError:
        assert True


