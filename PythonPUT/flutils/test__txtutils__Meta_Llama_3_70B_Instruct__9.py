from functools import cached_property
from itertools import chain
from sys import hexversion
from __decorators import cached_property
from textwrap import TextWrapper
from typing import Sequence
from typing import List
import re
import txtutils as module_0
from typing import cast
from typing import Optional
import pytest
def test_example_kylxnlfd():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert module_0.len_without_ansi(text) == 6











def test_example_in5ubr6l():
    text = '\x1b[31m\x1b[1m\x1b[4mLorem ipsum dolor sit amet, consectetur adipiscing elit. Cras fermentum maximus auctor. Cras a varius ligula. Phasellus ut ipsum eu erat consequat posuere.\x1b[0m Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas ultricies lacus id massa interdum dignissim. Curabitur \x1b[38;2;55;172;230m efficitur ante sit amet nibh consectetur, consequat rutrum nunc\x1b[0m egestas. Duis mattis arcu eget orci euismod, sit amet vulputate ante scelerisque. Aliquam ultrices, turpis id gravida vestibulum, tortor ipsum consequat mauris, eu cursus nisi felis at felis. Quisque blandit lacus nec mattis suscipit. Proin sed tortor ante.  Praesent fermentum orci id dolor euismod, quis auctor nisl sodales.\x1b[0m'
    wrapper = module_0.AnsiTextWrapper(width=40)
    wrapped_text = wrapper.fill(text)
    lines = wrapped_text.split('\n')
    for line in lines:
        assert module_0.len_without_ansi(line) <= 40








def test_example_0wg0sqnt():
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras fermentum maximus auctor.'
    wrapper = module_0.AnsiTextWrapper(width=60)
    wrapped_text = wrapper.fill(text)
    lines = wrapped_text.split('\n')
    assert len(lines) == 2
    assert module_0.len_without_ansi(lines[0]) <= 60
    assert module_0.len_without_ansi(lines[1]) <= 60








def test_example_6r2l2zi6():
    text = '\x1b[31m\x1b[1m\x1b[4mLorem ipsum dolor sit amet, consectetur adipiscing elit. Cras fermentum maximus auctor. Cras a varius ligula. Phasellus ut ipsum eu erat consequat posuere.\x1b[0m Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas ultricies lacus id massa interdum dignissim. Curabitur \x1b[38;2;55;172;230m efficitur ante sit amet nibh consectetur, consequat rutrum nunc\x1b[0m egestas. Duis mattis arcu eget orci euismod, sit amet vulputate ante scelerisque. Aliquam ultrices, turpis id gravida vestibulum, tortor ipsum consequat mauris, eu cursus nisi felis at felis. Quisque blandit lacus nec mattis suscipit. Proin sed tortor ante.  Praesent fermentum orci id dolor euismod, quis auctor nisl sodales.\x1b[0m'
    wrapper = module_0.AnsiTextWrapper(width=40)
    wrapped_text = wrapper.fill(text)
    assert isinstance(wrapped_text, str)





def test_len_without_ansi_dws91s6l():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert module_0.len_without_ansi(text) == 6





def test_AnsiTextWrapper_initial_indent_84ilf84a():
    text = '\x1b[31mLorem ipsum dolor sit amet, consectetur adipiscing elit.\x1b[0m'
    wrapper = module_0.AnsiTextWrapper(width=40, initial_indent='    ')
    wrapped_text = wrapper.fill(text)
    assert wrapped_text.startswith('    ')





def test_AnsiTextWrapper_subsequent_indent_mpci1zwc():
    text = '\x1b[31mLorem ipsum dolor sit amet, consectetur adipiscing elit.\x1b[0m'
    wrapper = module_0.AnsiTextWrapper(width=40, subsequent_indent='  ')
    wrapped_text = wrapper.fill(text)
    lines = wrapped_text.split('\n')
    assert all((line.startswith('  ') for line in lines[1:]))





def test_example_g444s4n5():
    text = '\x1b[31m\x1b[1m\x1b[4mLorem ipsum dolor sit amet, consectetur adipiscing elit. Cras fermentum maximus auctor. Cras a varius ligula. Phasellus ut ipsum eu erat consequat posuere.\x1b[0m Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas ultricies lacus id massa interdum dignissim. Curabitur \x1b[38;2;55;172;230m efficitur ante sit amet nibh consectetur, consequat rutrum nunc\x1b[0m egestas. Duis mattis arcu eget orci euismod, sit amet vulputate ante scelerisque. Aliquam ultrices, turpis id gravida vestibulum, tortor ipsum consequat mauris, eu cursus nisi felis at felis. Quisque blandit lacus nec mattis suscipit. Proin sed tortor ante.  Praesent fermentum orci id dolor euismod, quis auctor nisl sodales.\x1b[0m'
    wrapper = module_0.AnsiTextWrapper(width=80)
    wrapped_text = wrapper.fill(text)
    lines = wrapped_text.split('\n')
    for line in lines:
        assert module_0.len_without_ansi(line) <= 80


