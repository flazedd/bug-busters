import re
from sys import hexversion
from functools import cached_property
from typing import Sequence
from typing import cast
from itertools import chain
import pytest
from typing import List
from textwrap import TextWrapper
from __decorators import cached_property
from typing import Optional
import txtutils as module_0
def test_example_0px76qun():
    assert module_0.len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6


def test_example_qq0ii1cd():
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    wrapper = module_0.AnsiTextWrapper(width=20)
    wrapped_text = wrapper.fill(text)
    assert len(wrapped_text.split('\n')[0]) <= 20


def test_example_u3f3nfoe():
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    wrapper = module_0.AnsiTextWrapper(width=10, initial_indent='    ')
    wrapped_text = wrapper.fill(text)
    assert wrapped_text.startswith('    ')


def test_example_2vngzcva():
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    wrapper = module_0.AnsiTextWrapper(width=20, break_long_words=False)
    wrapped_text = wrapper.fill(text)
    assert 'consectetur' not in wrapped_text.split('\n')[0]


def test_example_dtm5qhai():
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    wrapper = module_0.AnsiTextWrapper(width=20, break_on_hyphens=False)
    wrapped_text = wrapper.fill(text)
    assert '-' not in wrapped_text.split('\n')[0]


def test_example_sp9ki071():
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    wrapper = module_0.AnsiTextWrapper(width=20, max_lines=2)
    wrapped_text = wrapper.fill(text)
    assert len(wrapped_text.split('\n')) <= 2


def test_example_yh63iunm():
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    wrapper = module_0.AnsiTextWrapper(width=20, max_lines=2, placeholder='[...]')
    wrapped_text = wrapper.fill(text)
    assert '[...]' in wrapped_text


def test_example_ci37vidu():
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    wrapper = module_0.AnsiTextWrapper(width=20, expand_tabs=False)
    wrapped_text = wrapper.fill(text)
    assert '\t' not in wrapped_text


