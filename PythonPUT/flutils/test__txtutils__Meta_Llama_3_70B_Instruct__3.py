from __decorators import cached_property
import re
from textwrap import TextWrapper
import pytest
from functools import cached_property
from typing import List
from typing import Sequence
from typing import Optional
from itertools import chain
from typing import cast
from sys import hexversion
import txtutils as module_0
def test_example_kxbv4ojg():
    assert 1 == 1


def test_len_without_ansi_lq5xfo5f():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert module_0.len_without_ansi(text) == 6


def test_AnsiTextWrapper_d22giww7():
    wrapper = module_0.AnsiTextWrapper(width=40)
    text = '\x1b[31m\x1b[1m\x1b[4mLorem ipsum dolor sit amet, consectetur adipiscing elit.\x1b[0m'
    wrapped_text = wrapper.fill(text)
    assert wrapped_text != text


def test_AnsiTextWrapper_initial_indent_0wepfzga():
    wrapper = module_0.AnsiTextWrapper(width=40, initial_indent='\x1b[31m    ')
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    wrapped_text = wrapper.fill(text)
    assert wrapped_text.startswith('\x1b[31m    ')


def test_AnsiTextWrapper_subsequent_indent_9751sdrz():
    wrapper = module_0.AnsiTextWrapper(width=40, subsequent_indent='\x1b[31m    ')
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras fermentum maximus auctor.'
    wrapped_text = wrapper.fill(text)
    lines = wrapped_text.split('\n')
    assert all((line.startswith('\x1b[31m    ') for line in lines[1:]))


def test_AnsiTextWrapper_max_lines_wc8i2t92():
    wrapper = module_0.AnsiTextWrapper(width=40, max_lines=2)
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras fermentum maximus auctor. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.'
    wrapped_text = wrapper.fill(text)
    lines = wrapped_text.split('\n')
    assert len(lines) == 2


def test_AnsiTextWrapper_placeholder_3nzr7ema():
    wrapper = module_0.AnsiTextWrapper(width=40, max_lines=2, placeholder=' [more]')
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras fermentum maximus auctor. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.'
    wrapped_text = wrapper.fill(text)
    lines = wrapped_text.split('\n')
    assert lines[-1].endswith(' [more]')


def test_AnsiTextWrapper_break_long_words_a8frthar():
    wrapper = module_0.AnsiTextWrapper(width=10, break_long_words=True)
    text = 'Loremipsumdolorsitamet'
    wrapped_text = wrapper.fill(text)
    lines = wrapped_text.split('\n')
    assert len(max(lines, key=len)) <= 10


