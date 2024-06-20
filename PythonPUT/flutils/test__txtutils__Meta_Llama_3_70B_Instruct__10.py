import re
from textwrap import TextWrapper
from itertools import chain
from typing import List
from typing import Optional
from typing import Sequence
from typing import cast
from functools import cached_property
from __decorators import cached_property
import txtutils as module_0
import pytest
from sys import hexversion
def test_example_xp34v92g():
    text = '\x1b[31m\x1b[1m\x1b[4mLorem ipsum dolor sit amet, consectetur adipiscing elit. Cras fermentum maximus auctor. Cras a varius ligula. Phasellus ut ipsum eu erat consequat posuere.\x1b[0m Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas ultricies lacus id massa interdum dignissim. Curabitur \x1b[38;2;55;172;230m efficitur ante sit amet nibh consectetur, consequat rutrum nunc\x1b[0m egestas. Duis mattis arcu eget orci euismod, sit amet vulputate ante scelerisque. Aliquam ultrices, turpis id gravida vestibulum, tortor ipsum consequat mauris, eu cursus nisi felis at felis. Quisque blandit lacus nec mattis suscipit. Proin sed tortor ante.  Praesent fermentum orci id dolor \x1b[38;5;208meuismod, quis auctor nisl sodales.\x1b[0m'
    wrapper = module_0.AnsiTextWrapper(width=40)
    wrapped_text = wrapper.fill(text)
    assert isinstance(wrapped_text, str)


def test_example_5co9jgrs():
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    wrapper = module_0.AnsiTextWrapper(width=20)
    wrapped_text = wrapper.fill(text)
    assert len(wrapped_text.split('\n')[0]) <= 20


def test_example_81i334u7():
    text = '\x1b[31mHello\x1b[0m, world!'
    assert module_0.len_without_ansi(text) == 13


def test_example_yh002ru1():
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    wrapper = module_0.AnsiTextWrapper(width=20, break_long_words=False)
    wrapped_text = wrapper.fill(text)
    assert len(max(wrapped_text.split('\n'), key=len)) <= 20


def test_example_yjr5zob4():
    text = '\x1b[31mHello\x1b[0m, world!'
    wrapper = module_0.AnsiTextWrapper(width=10)
    wrapped_text = wrapper.fill(text)
    assert '\n' in wrapped_text


def test_example_kxf74nc6():
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    wrapper = module_0.AnsiTextWrapper(width=20, subsequent_indent='  ')
    wrapped_text = wrapper.fill(text)
    lines = wrapped_text.split('\n')
    assert all((line.startswith('  ') for line in lines[1:]))


def test_example_wenxtzxh():
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras fermentum maximus auctor.'
    wrapper = module_0.AnsiTextWrapper(width=40, max_lines=2)
    wrapped_text = wrapper.fill(text)
    assert len(wrapped_text.split('\n')) <= 2


def test_example_sx4ea8jc():
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    wrapper = module_0.AnsiTextWrapper(width=20, placeholder='[...]')
    wrapped_text = wrapper.fill(text)
    assert '[...]' not in wrapped_text
    wrapper.max_lines = 1
    wrapped_text = wrapper.fill(text)
    assert '[...]' in wrapped_text


