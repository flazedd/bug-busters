from __decorators import cached_property
import pytest
from typing import Sequence
from functools import cached_property
from textwrap import TextWrapper
import re
from typing import List
from typing import cast
from sys import hexversion
from itertools import chain
from typing import Optional
import txtutils as module_0
def test_example_s3hdif2j():
    wrapper = module_0.AnsiTextWrapper(width=40)
    text = '\x1b[31m\x1b[1m\x1b[4mLorem ipsum dolor sit amet, consectetur adipiscing elit. Cras fermentum maximus auctor. Cras a varius ligula. Phasellus ut ipsum eu erat consequat posuere.\x1b[0m Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas ultricies lacus id massa interdum dignissim. Curabitur \x1b[38;2;55;172;230m efficitur ante sit amet nibh consectetur, consequat rutrum nunc\x1b[0m egestas. Duis mattis arcu eget orci euismod, sit amet vulputate ante scelerisque. Aliquam ultrices, turpis id gravida vestibulum, tortor ipsum consequat mauris, eu cursus nisi felis at felis. Quisque blandit lacus nec mattis suscipit. Proin sed tortor ante.  Praesent fermentum orci id dolor euismod, quis auctor nisl sodales.\x1b[0m'
    wrapped_text = wrapper.fill(text)
    assert wrapped_text is not None








def test_example_hq8b8kmv():
    wrapper = module_0.AnsiTextWrapper(width=20)
    text = '\x1b[32mThis is a very long sentence that needs to be wrapped across multiple lines.\x1b[0m'
    wrapped_text = wrapper.fill(text)
    assert len(wrapped_text.split('\n')) > 1








def test_example_nbm7nbde():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert module_0.len_without_ansi(text) == 6





def test_example_oa70qfz0():
    wrapper = module_0.AnsiTextWrapper(width=40, initial_indent='    ')
    text = '\x1b[31m\x1b[1m\x1b[4mLorem ipsum dolor sit amet, consectetur adipiscing elit. Cras fermentum maximus auctor. Cras a varius ligula. Phasellus ut ipsum eu erat consequat posuere.\x1b[0m Pellentesque habitant orbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas ultricies lacus id massa interdum dignissim. Curabitur \x1b[38;2;55;172;230m efficitur ante sit amet nibh consectetur, consequat rutrum nunc\x1b[0m egestas. Duis mattis arcu eget orci euismod, sit amet vulputate ante scelerisque. Aliquam ultrices, turpis id gravida vestibulum, tortor ipsum consequat mauris, eu cursus nisi felis at felis. Quisque blandit lacus nec mattis suscipit. Proin sed tortor ante.  Praesent fermentum orci id dolor \x1b[38;5;208meuismod, quis auctor nisl sodales.\x1b[0m'
    wrapped_text = wrapper.fill(text)
    assert wrapped_text.startswith('    ')





def test_example_vb1ukbry():
    wrapper = module_0.AnsiTextWrapper(width=40, break_long_words=False)
    text = '\x1b[31m\x1b[1m\x1b[4mLorem ipsum dolor sit amet, consectetur adipiscing elit. Cras fermentum maximus auctor. Cras a varius ligula. Phasellus ut ipsum eu erat consequat posuere.\x1b[0m Pellentesque habitant orbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas ultricies lacus id massa interdum dignissim. Curabitur \x1b[38;2;55;172;230m efficitur ante sit amet nibh consectetur, consequat rutrum nunc\x1b[0m egestas. Duis mattis arcu eget orci euismod, sit amet vulputate ante scelerisque. Aliquam ultrices, turpis id gravida vestibulum, tortor ipsum consequat mauris, eu cursus nisi felis at felis. Quisque blandit lacus nec mattis suscipit. Proin sed tortor ante.  Praesent fermentum orci id dolor \x1b[38;5;208meuismod, quis auctor nisl sodales.\x1b[0m'
    wrapped_text = wrapper.fill(text)
    assert '\x1b[31m\x1b[1m\x1b[4mLorem ipsum dolor sit amet, consectetur' in wrapped_text





def test_AnsiTextWrapper_oroet27c():
    wrapper = module_0.AnsiTextWrapper(width=40)
    text = '\\x1b[31m\\x1b[1m\\x1b[4mLorem ipsum dolor sit amet, consectetur adipiscing elit. Cras fermentum maximus auctor. Cras a varius ligula. Phasellus ut ipsum eu erat consequat posuere.\\x1b[0m Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas ultricies lacus id massa interdum dignissim. Curabitur \\x1b[38;2;55;172;230m efficitur ante sit amet nibh consectetur, consequat rutrum nunc\\x1b[0m egestas. Duis mattis arcu eget orci euismod, sit amet vulputate ante scelerisque. Aliquam ultrices, turpis id gravida vestibulum, tortor ipsum consequat mauris, eu cursus nisi felis at felis. Quisque blandit lacus nec mattis suscipit. Proin sed tortor ante.  Praesent fermentum orci id dolor euismod, quis auctor nisl sodales.\\x1b[0m'
    wrapped_text = wrapper.fill(text)
    assert isinstance(wrapped_text, str)


def test_AnsiTextWrapper_initial_indent_ijyffbh5():
    wrapper = module_0.AnsiTextWrapper(width=40, initial_indent='  ')
    text = '\\x1b[31m\\x1b[1m\\x1b[4mLorem ipsum dolor sit amet, consectetur adipiscing elit.\\x1b[0m'
    wrapped_text = wrapper.fill(text)
    assert wrapped_text.startswith('  ')


def test_AnsiTextWrapper_max_lines_r9yyjo0g():
    wrapper = module_0.AnsiTextWrapper(width=40, max_lines=2)
    text = '\\x1b[31m\\x1b[1m\\x1b[4mLorem ipsum dolor sit amet, consectetur adipiscing elit.\\x1b[0m Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas ultricies lacus id massa interdum dignissim. Curabitur \\x1b[38;2;55;172;230m efficitur ante sit amet nibh consectetur, consequat rutrum nunc\\x1b[0m egestas.'
    wrapped_text = wrapper.fill(text)
    lines = wrapped_text.split('\n')
    assert len(lines) == 2


