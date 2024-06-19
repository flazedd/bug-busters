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
def test_example_kmfg6c8v():
    text = '\x1b[31m\x1b[1m\x1b[4mLorem ipsum dolor sit amet, consectetur adipiscing elit. Cras fermentum maximus auctor. Cras a varius ligula. Phasellus ut ipsum eu erat consequat posuere.\x1b[0m Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas ultricies lacus id massa interdum dignissim. Curabitur \x1b[38;2;55;172;230m efficitur ante sit amet nibh consectetur, consequat rutrum nunc\x1b[0m egestas. Duis mattis arcu eget orci euismod, sit amet vulputate ante scelerisque. Aliquam ultrices, turpis id gravida vestibulum, tortor ipsum consequat mauris, eu cursus nisi felis at felis. Quisque blandit lacus nec mattis suscipit. Proin sed tortor ante.  Praesent fermentum orci id dolor euismod, quis auctor nisl sodales.\x1b[0m'
    wrapper = module_0.AnsiTextWrapper(width=40)
    wrapped_text = wrapper.fill(text)
    assert wrapped_text


def test_example_yl7o89ny():
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    wrapper = module_0.AnsiTextWrapper(width=20)
    wrapped_text = wrapper.fill(text)
    assert len(max(wrapped_text.split('\n'), key=len)) <= 20


def test_example_pct3iuw3():
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    wrapper = module_0.AnsiTextWrapper(width=10)
    wrapped_text = wrapper.fill(text)
    assert len(wrapped_text.split('\n')[0]) <= 10


def test_example_ayk4vddr():
    text = '\x1b[31mLorem ipsum dolor\x1b[0m sit amet, consectetur adipiscing elit.'
    wrapper = module_0.AnsiTextWrapper(width=20)
    wrapped_text = wrapper.fill(text)
    assert '\x1b[31m' in wrapped_text
    assert '\x1b[0m' in wrapped_text


def test_example_bioo90j5():
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    wrapper = module_0.AnsiTextWrapper(width=20, initial_indent='    ')
    wrapped_text = wrapper.fill(text)
    assert wrapped_text.startswith('    ')


def test_example_2tzj2kxw():
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    wrapper = module_0.AnsiTextWrapper(width=20, subsequent_indent='    ')
    wrapped_text = wrapper.fill(text)
    lines = wrapped_text.split('\n')
    assert all((line.startswith('    ') for line in lines[1:]))


def test_example_qn0fd95i():
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    wrapper = module_0.AnsiTextWrapper(width=20, max_lines=2)
    wrapped_text = wrapper.fill(text)
    lines = wrapped_text.split('\n')
    assert len(lines) <= 2


def test_example_6dgptybf():
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    wrapper = module_0.AnsiTextWrapper(width=20, break_long_words=False)
    wrapped_text = wrapper.fill(text)
    lines = wrapped_text.split('\n')
    assert all((len(line) <= 20 for line in lines))


