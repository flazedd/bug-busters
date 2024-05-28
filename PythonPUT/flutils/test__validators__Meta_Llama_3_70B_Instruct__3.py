import keyword
import validators as module_0
from typing import Union
from collections import UserString
import pytest
def test_example_f6hh3hr3():
    module_0.validate_identifier('valid_identifier')


def test_example_4n3pel3k():
    try:
        module_0.validate_identifier('123invalid')
        assert False, 'Expected SyntaxError for invalid identifier'
    except SyntaxError:
        assert True


def test_example_741u90z0():
    module_0.validate_identifier('valid_identifier', allow_underscore=False)
    try:
        module_0.validate_identifier('_private', allow_underscore=False)
        assert False, 'Expected SyntaxError for identifier starting with underscore'
    except SyntaxError:
        assert True


def test_example_9lw3dony():
    try:
        module_0.validate_identifier('class')
        assert False, 'Expected SyntaxError for keyword identifier'
    except SyntaxError:
        assert True


def test_example_1uwcx1nb():
    try:
        module_0.validate_identifier('True')
        assert False, 'Expected SyntaxError for keyword identifier'
    except SyntaxError:
        assert True


def test_example_g7n8drhd():
    try:
        module_0.validate_identifier('123abc')
        assert False, 'Expected SyntaxError for identifier starting with a number'
    except SyntaxError:
        assert True


def test_example_i5ums9uf():
    try:
        module_0.validate_identifier('abc-def')
        assert False, 'Expected SyntaxError for invalid identifier'
    except SyntaxError:
        assert True


def test_example_292gxwdy():
    try:
        module_0.validate_identifier('abc*def')
        assert False, 'Expected SyntaxError for invalid identifier'
    except SyntaxError:
        assert True


