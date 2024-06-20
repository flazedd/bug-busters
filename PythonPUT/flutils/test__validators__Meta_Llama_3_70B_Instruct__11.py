import pytest
from collections import UserString
import validators as module_0
import keyword
from typing import Union
def test_example_ookrg8uz():
    try:
        module_0.validate_identifier('123')
        assert False, 'Expected SyntaxError for identifier starting with a number'
    except SyntaxError:
        assert True


def test_example_isuy49s3():
    try:
        module_0.validate_identifier('if')
        assert False, 'Expected SyntaxError for keyword identifier'
    except SyntaxError:
        assert True


def test_example_zqdfkzjp():
    module_0.validate_identifier('valid_identifier')
    assert True


def test_example_0x4mg15j():
    try:
        module_0.validate_identifier('_private', allow_underscore=False)
        assert False, 'Expected SyntaxError for identifier starting with underscore'
    except SyntaxError:
        assert True


def test_example_n6ks5mbr():
    try:
        module_0.validate_identifier(' invalid identifier')
        assert False, 'Expected SyntaxError for identifier with leading whitespace'
    except SyntaxError:
        assert True


def test_example_v35zb9lw():
    try:
        module_0.validate_identifier('')
        assert False, 'Expected SyntaxError for empty identifier'
    except SyntaxError:
        assert True


def test_example_28mpujmx():
    try:
        module_0.validate_identifier('hello-world')
        assert False, 'Expected SyntaxError for identifier with hyphen'
    except SyntaxError:
        assert True


def test_example_i2yiiqto():
    try:
        module_0.validate_identifier('hello!')
        assert False, 'Expected SyntaxError for identifier with special character'
    except SyntaxError:
        assert True


