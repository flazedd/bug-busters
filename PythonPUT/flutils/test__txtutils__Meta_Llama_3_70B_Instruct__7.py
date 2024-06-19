from itertools import chain
from typing import cast
from functools import cached_property
from typing import Optional
from sys import hexversion
import pytest
from __decorators import cached_property
import re
from textwrap import TextWrapper
from typing import List
from typing import Sequence
import txtutils as module_0
def test_example_v0pb2vw6():
    text = '\x1b[31m\x1b[1m\x1b[4mLorem ipsum dolor sit amet, consectetur adipiscing elit.\x1b[0m'
    wrapper = module_0.AnsiTextWrapper(width=40)
    wrapped_text = wrapper.fill(text)
    assert wrapped_text.startswith('\x1b[31m\x1b[1m\x1b[4mLorem ipsum dolor ')


def test_example_lj09nqsw():
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    wrapper = module_0.AnsiTextWrapper(width=20)
    wrapped_text = wrapper.fill(text)
    assert len(wrapped_text.split('\n')[0]) <= 20


def test_example_28qynpir():
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras fermentum maximus auctor. Cras a varius ligula.'
    wrapper = module_0.AnsiTextWrapper(width=30)
    wrapped_text = wrapper.fill(text)
    assert '\n' in wrapped_text


def test_example_bjv6ehi6():
    text = '\x1b[31mLorem ipsum dolor sit amet, consectetur adipiscing elit.\x1b[0m'
    wrapper = module_0.AnsiTextWrapper(width=30)
    wrapped_text = wrapper.fill(text)
    assert '\x1b[31m' in wrapped_text


def test_example_3p97g8w5():
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    wrapper = module_0.AnsiTextWrapper(width=100)
    wrapped_text = wrapper.fill(text)
    assert wrapped_text == text


def test_example_wwzdcvaq():
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras fermentum maximus auctor.'
    wrapper = module_0.AnsiTextWrapper(width=40, initial_indent='    ')
    wrapped_text = wrapper.fill(text)
    assert wrapped_text.startswith('    Lorem ipsum dolor')


def test_example_xkk112le():
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras fermentum maximus auctor.'
    wrapper = module_0.AnsiTextWrapper(width=40, subsequent_indent='    ')
    wrapped_text = wrapper.fill(text)
    lines = wrapped_text.split('\n')
    assert all((line.startswith('    ') for line in lines[1:]))


def test_example_zcl1sofo():
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras fermentum maximus auctor.'
    wrapper = module_0.AnsiTextWrapper(width=40, max_lines=2)
    wrapped_text = wrapper.fill(text)
    assert wrapped_text.count('\n') == 1


