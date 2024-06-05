from typing import List
from typing import Tuple
import pytest
from typing import Optional
import comments as module_0
def test_example_53peyb1q():
    from comments import parse, add_to_line
    original_string = 'import comments as module_0'
    comments = ['This is a comment']
    result = add_to_line(comments, original_string, comment_prefix='#')
    assert result == 'import comments as module_0# This is a comment'








def test_example_1e7daiyr():
    from comments import parse, add_to_line
    original_string = 'import comments as module_0'
    comments = ['This is a comment', 'This is another comment']
    result = add_to_line(comments, original_string, comment_prefix='#')
    assert result == 'import comments as module_0# This is a comment; This is another comment'








def test_example_zj8z45w0():
    from comments import add_to_line, parse
    original_string = 'import comments as module_0'
    comments = ['This is a comment', 'This is another comment']
    comment_prefix = '#'
    result = add_to_line(comments, original_string, removed=False, comment_prefix=comment_prefix)
    assert result == 'import comments as module_0# This is a comment; This is another comment'





def test_example_ib7ze1ay():
    from comments import add_to_line, parse
    comments = ['This is a comment']
    original_string = 'import comments as module_0'
    comment_prefix = '# '
    result = add_to_line(comments, original_string, comment_prefix=comment_prefix)
    assert result == f"{original_string} {comment_prefix}{'; '.join(comments)}"


