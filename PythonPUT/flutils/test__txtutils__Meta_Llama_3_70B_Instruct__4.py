from textwrap import TextWrapper
from typing import Optional
from typing import List
import pytest
from sys import hexversion
from functools import cached_property
import re
from typing import cast
import txtutils as module_0
from itertools import chain
from __decorators import cached_property
from typing import Sequence
def test_AnsiTextWrapper_56q20jwv():
    wrapper = module_0.AnsiTextWrapper(width=40)
    text = '\x1b[31m\x1b[1m\x1b[4mLorem ipsum dolor sit amet, consectetur adipiscing elit. Cras fermentum maximus auctor. Cras a varius ligula. Phasellus ut ipsum eu erat consequat posuere.\x1b[0m Pellentesque habitant orbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas ultricies lacus id massa interdum dignissim. Curabitur \x1b[38;2;55;172;230m efficitur ante sit amet nibh consectetur, consequat rutrum nunc\x1b[0m egestas. Duis mattis arcu eget orci euismod, sit amet vulputate ante scelerisque. Aliquam ultrices, turpis id gravida vestibulum, tortor ipsum consequat mauris, eu cursus nisi felis at felis. Quisque blandit lacus nec mattis suscipit. Proin sed tortor ante.  Praesent fermentum orci id dolor \x1b[38;5;208meuismod, quis auctor nisl sodales.\x1b[0m'
    wrapped_text = wrapper.fill(text)
    assert len(wrapped_text.splitlines()) > 1





def test_AnsiTextWrapper_initial_indent_kx806df2():
    wrapper = module_0.AnsiTextWrapper(width=40, initial_indent='\x1b[32m  ')
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    wrapped_text = wrapper.fill(text)
    assert wrapped_text.startswith('\x1b[32m  Lorem ipsum')





def test_AnsiTextWrapper_placeholder_ze7ncinf():
    wrapper = module_0.AnsiTextWrapper(width=40, max_lines=2, placeholder='[...]')
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras fermentum maximus auctor. Phasellus ut ipsum eu erat consequat posuere.'
    wrapped_text = wrapper.fill(text)
    lines = wrapped_text.splitlines()
    assert len(lines) == 2
    assert lines[1].endswith('[...]')





def test_AnsiTextWrapper_break_long_words_i3b9buip():
    wrapper = module_0.AnsiTextWrapper(width=20, break_long_words=True)
    text = 'Loremipsumdolorsitametconsecteturadipiscingelit.'
    wrapped_text = wrapper.fill(text)
    lines = wrapped_text.splitlines()
    assert len(lines) > 1
    assert all((len(line) <= 20 for line in lines))





def test_AnsiTextWrapper_break_on_hyphens_m4jhmsqn():
    wrapper = module_0.AnsiTextWrapper(width=40, break_on_hyphens=True)
    text = 'Lorem-ipsum-dolor-sit-amet-consectetur-adipiscing-elit.'
    wrapped_text = wrapper.fill(text)
    lines = wrapped_text.splitlines()
    assert len(lines) > 1
    assert '-' in lines[0]
    assert '-' in lines[1]





def test_len_without_ansi_12xazpng():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert module_0.len_without_ansi(text) == 6


def test_AnsiTextWrapper_g1gykfjq():
    wrapper = module_0.AnsiTextWrapper(width=40)
    text = '\x1b[31m\x1b[1m\x1b[4mLorem ipsum dolor sit amet, consectetur adipiscing elit.\x1b[0m'
    wrapped_text = wrapper.fill(text)
    assert len(wrapped_text.split('\n')[0]) <= 40


