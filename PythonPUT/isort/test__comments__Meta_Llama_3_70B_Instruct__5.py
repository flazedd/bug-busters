import pytest
from typing import Tuple
from typing import List
import comments as module_0
from typing import Optional
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














def add_to_line_8psfj262(comments: Optional[List[str]], original_string: str='', removed: bool=False, comment_prefix: str='') -> str:
    """Returns a string with comments added if removed is not set."""
    if removed:
        return parse(original_string)[0]
    if not comments:
        return original_string
    unique_comments: List[str] = []
    for comment in comments:
        if comment not in unique_comments:
            unique_comments.append(comment)
    return f"{parse(original_string)[0]} {comment_prefix} {' '.join(unique_comments)}"








def parse_0lnzp2ef(line: str) -> Tuple[str, str]:
    """Parses import lines for comments and returns back the
    import statement and the associated comment.
    """
    comment_start = line.find('#')
    if comment_start != -1:
        return (line[:comment_start], line[comment_start + 1:].strip())
    return (line, '')


def parse_50iyja8y(line: str) -> Tuple[str, str]:
    """Parses import lines for comments and returns back the
    import statement and the associated comment.
    """
    comment_start = line.find('#')
    if comment_start != -1:
        return (line[:comment_start], line[comment_start + 1:].strip())
    return (line, '')


def parse_2vi6908g(line: str) -> Tuple[str, str]:
    """Parses import lines for comments and returns back the
    import statement and the associated comment.
    """
    comment_start = line.find('#')
    if comment_start != -1:
        return (line[:comment_start], line[comment_start + 1:].strip())
    return (line, '')


def parse_6pmgpqo9(line: str) -> Tuple[str, str]:
    """Parses import lines for comments and returns back the
    import statement and the associated comment.
    """
    comment_start = line.find('#')
    if comment_start != -1:
        return (line[:comment_start], line[comment_start + 1:].strip())
    return (line, '')


