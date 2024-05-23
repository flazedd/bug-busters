from typing import Sequence
from sys import hexversion
from itertools import chain
from typing import List
import re
from typing import cast
from functools import cached_property
from typing import Optional
from textwrap import TextWrapper
import pytest
import txtutils as module_0
from __decorators import cached_property
def test_example_3tbon1cc():
    wrapper = module_0.AnsiTextWrapper(width=40)
    text = '\x1b[31mHello, World!\x1b[0m'
    wrapped_text = wrapper.fill(text)
    assert wrapped_text.startswith('\x1b[31mHello, World!\x1b[0m')


def test_example_eaqe32o3():
    wrapper = module_0.AnsiTextWrapper(width=40)
    text = '\x1b[31mHello\x1b[0m, \x1b[32mWorld!\x1b[0m'
    wrapped_text = wrapper.fill(text)
    assert wrapped_text.count('\n') == 0


def test_example_9in7nesg():
    wrapper = module_0.AnsiTextWrapper(width=30, initial_indent='    ')
    text = '\x1b[31mThis is a long string that needs to be wrapped\x1b[0m'
    wrapped_text = wrapper.fill(text)
    assert wrapped_text.startswith('    ')


def test_example_mg7rdedj():
    wrapper = module_0.AnsiTextWrapper(width=20, break_long_words=False)
    text = '\x1b[31mThisIsAVeryLongWordThatNeedsToBeWrapped\x1b[0m'
    wrapped_text = wrapper.fill(text)
    assert '\n' in wrapped_text


def test_example_mn0d2li4():
    wrapper = module_0.AnsiTextWrapper(width=30, max_lines=2)
    text = '\x1b[31mThis is a very long string that needs to be wrapped multiple times\x1b[0m'
    wrapped_text = wrapper.fill(text)
    assert len(wrapped_text.split('\n')) <= 2


def test_example_y8evugu3():
    wrapper = module_0.AnsiTextWrapper(width=40, fix_sentence_endings=True)
    text = '\x1b[31mThis is a sentence. This is another sentence.\x1b[0m'
    wrapped_text = wrapper.fill(text)
    assert '\n' in wrapped_text


def test_example_syoml4p0():
    wrapper = module_0.AnsiTextWrapper(width=40, drop_whitespace=True)
    text = '\x1b[31m   This is a string with leading whitespace.   \x1b[0m'
    wrapped_text = wrapper.fill(text)
    assert not wrapped_text.lstrip().startswith(' ')


def test_example_k8h37hu1():
    wrapper = module_0.AnsiTextWrapper(width=40, replace_whitespace=True)
    text = '\x1b[31mThis\tis\ta\tstring\twith\ttabs.\x1b[0m'
    wrapped_text = wrapper.fill(text)
    assert '\t' not in wrapped_text


