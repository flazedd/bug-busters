import keyword
import pytest
from typing import Union
import validators as module_0
from collections import UserString
def test_example_dme69vi4():
    module_0.validate_identifier('valid_identifier')


def test_example_gztqgd0b():
    try:
        module_0.validate_identifier('123invalid')
        assert False, 'Should have raised a SyntaxError'
    except SyntaxError:
        assert True


def test_example_l79kl65d():
    try:
        module_0.validate_identifier('break')
        assert False, 'Should have raised a SyntaxError'
    except SyntaxError:
        assert True


def test_example_9tep7u9f():
    module_0.validate_identifier('valid_identifier', allow_underscore=True)


def test_example_mfln7jau():
    try:
        module_0.validate_identifier('class')
        assert False, 'Should have raised a SyntaxError'
    except SyntaxError:
        assert True


def test_example_bhwu99uu():
    try:
        module_0.validate_identifier('class', allow_underscore=False)
        assert False, 'Should have raised a SyntaxError'
    except SyntaxError:
        assert True


def test_example_39mg30ho():
    try:
        module_0.validate_identifier('')
        assert False, 'Should have raised a SyntaxError'
    except SyntaxError:
        assert True


def test_example_0sfn793b():
    try:
        module_0.validate_identifier('hello world')
        assert False, 'Should have raised a SyntaxError'
    except SyntaxError:
        assert True


