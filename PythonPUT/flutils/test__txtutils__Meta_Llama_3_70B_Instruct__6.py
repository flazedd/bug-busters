from __decorators import cached_property
from typing import List
from typing import Optional
from textwrap import TextWrapper
import re
from typing import Sequence
import txtutils as module_0
from itertools import chain
from sys import hexversion
from typing import cast
import pytest
from functools import cached_property
def test_AnsiTextWrapper_n9ttjcoy():
    wrapper = module_0.AnsiTextWrapper(width=40)
    text = '\x1b[31m\x1b[1m\x1b[4mLorem ipsum dolor sit amet, consectetur adipiscing elit.\x1b[0m'
    wrapped_text = wrapper.fill(text)
    assert len(wrapped_text.splitlines()) == 2





def test_len_without_ansi_wiolfxi0():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert module_0.len_without_ansi(text) == 6





def test_AnsiTextWrapper_max_lines_qjtfdm5h():
    wrapper = module_0.AnsiTextWrapper(width=40, max_lines=2)
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras fermentum maximus auctor. Phasellus ut ipsum eu erat consequat posuere.'
    wrapped_text = wrapper.fill(text)
    lines = wrapped_text.splitlines()
    assert len(lines) == 2
    assert lines[1].endswith('[...]')





def test_len_without_ansi_mwktgior():
    assert module_0.len_without_ansi('\x1b[38;5;209mfoobar\x1b[0m') == 6


def test_AnsiTextWrapper_jgjjtdx4():
    wrapper = module_0.AnsiTextWrapper(width=20)
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    wrapped_text = wrapper.fill(text)
    assert all((len(line) <= 20 for line in wrapped_text.split('\n')))


def test_AnsiTextWrapper_max_lines_0bjjj88z():
    wrapper = module_0.AnsiTextWrapper(width=40, max_lines=2)
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus ut ipsum eu erat consequat posuere. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.'
    wrapped_text = wrapper.fill(text)
    assert len(wrapped_text.split('\n')) <= 2


def test_AnsiTextWrapper_placeholder_fbv5jyle():
    wrapper = module_0.AnsiTextWrapper(width=40, max_lines=2, placeholder=' [more]')
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus ut ipsum eu erat consequat posuere. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.'
    wrapped_text = wrapper.fill(text)
    assert wrapped_text.endswith(' [more]')


def test_AnsiTextWrapper_break_long_words_g85ebgj1():
    wrapper = module_0.AnsiTextWrapper(width=10, break_long_words=False)
    text = 'Loremipsumdolorsitamet'
    wrapped_text = wrapper.fill(text)
    assert len(wrapped_text.split('\n')[0]) > 10


