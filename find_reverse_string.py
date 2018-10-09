#  sample = '#abc#de#eg#'

def rev(s):
    """concatenates inside out"""
    return len(s) != 0 and rev(s[1:]) + s[0] or s

def test_rev():
    s = '#abc#de#eg#'
    assert rev(s) == '#ge#ed#cba#'


def reverse_and_filter(s):
    """reverse only alnums filtering special characters"""
    if len(s) == 0:
        return s
    return reverse_and_filter(s[1:]) + (s[0].isalnum() and s[0] or '')

def test_reverse_and_filter():
    s = '#abc#de#eg#'
    assert reverse_and_filter(s) == 'geedcba'


def reverse_only_alnum(s):
    """reverse only alnums leaving special charactes in place"""
    return len(s) != 0 and reverse_only_alnum(s[1:]) + s[0] or s

def test_reverse_only_alnum():
    s = '#abc#de#eg#'
    assert reverse_only_alnum(s) == '#gee#dc#ba#'

def reverse_str2(s):
    return ''.join([x[::-1] for x in s[::-1] if x.isalnum()])
