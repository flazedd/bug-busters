from typing import List
import pytest
from typing import Optional
import txtutils as module_0
from functools import cached_property
from __decorators import cached_property
from typing import Sequence
from typing import cast
import re
from textwrap import TextWrapper
from itertools import chain
from sys import hexversion
def test_example_5fujj6of():
    text = '\x1b[31m\x1b[1m\x1b[4mLorem ipsum dolor sit amet, consectetur adipiscing elit. Cras fermentum maximus auctor. Cras a varius ligula. Phasellus ut ipsum eu erat consequat posuere.\x1b[0m Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas ultricies lacus id massa interdum dignissim. Curabitur \x1b[38;2;55;172;230m efficitur ante sit amet nibh consectetur, consequat rutrum nunc\x1b[0m egestas. Duis mattis arcu eget orci euismod, sit amet vulputate ante scelerisque. Aliquam ultrices, turpis id gravida vestibulum, tortor ipsum consequat mauris, eu cursus nisi felis at felis. Quisque blandit lacus nec mattis suscipit. Proin sed tortor ante.  Praesent fermentum orci id dolor euismod, quis auctor nisl sodales.\x1b[0m'
    wrapper = module_0.AnsiTextWrapper(width=80)
    wrapped_text = wrapper.fill(text)
    for line in wrapped_text.split('\n'):
        assert module_0.len_without_ansi(line) <= 80


def test_example_iuu8fuf5():
    text = '\x1b[31mHello\x1b[0m, \x1b[32mworld\x1b[0m!'
    wrapper = module_0.AnsiTextWrapper(width=20)
    wrapped_text = wrapper.fill(text)
    assert module_0.len_without_ansi(wrapped_text) <= 20


def test_example_zevyuy9n():
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    wrapper = module_0.AnsiTextWrapper(width=20)
    wrapped_text = wrapper.fill(text)
    lines = wrapped_text.split('\n')
    assert all((module_0.len_without_ansi(line) <= 20 for line in lines))


def test_example_8xhb6igu():
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    wrapper = module_0.AnsiTextWrapper(width=10)
    wrapped_text = wrapper.fill(text)
    lines = wrapped_text.split('\n')
    assert len(lines) > 1


def test_example_kabxdtqs():
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    wrapper = module_0.AnsiTextWrapper(width=100)
    wrapped_text = wrapper.fill(text)
    assert '\n' not in wrapped_text


def test_example_m0k1rlmb():
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    wrapper = module_0.AnsiTextWrapper(width=40)
    wrapped_text = wrapper.fill(text)
    lines = wrapped_text.split('\n')
    assert all((module_0.len_without_ansi(line) <= 40 for line in lines))
    assert len(lines) > 2


def test_example_rl3pa4ac():
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    wrapper = module_0.AnsiTextWrapper(width=40, initial_indent='    ')
    wrapped_text = wrapper.fill(text)
    lines = wrapped_text.split('\n')
    assert lines[0].startswith('    ')
    assert all((module_0.len_without_ansi(line) <= 40 for line in lines))


def test_example_lfz35sju():
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    wrapper = module_0.AnsiTextWrapper(width=40, subsequent_indent='    ')
    wrapped_text = wrapper.fill(text)
    lines = wrapped_text.split('\n')
    assert all((line.startswith('    ') for line in lines[1:]))
    assert all((module_0.len_without_ansi(line) <= 40 for line in lines))


