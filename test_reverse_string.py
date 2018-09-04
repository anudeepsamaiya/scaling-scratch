from reverse_string import *

def test_rev():
    s = '#abc#de#eg#'
    assert rev(s) == '#ge#ed#cba#'

def test_reverse_and_filter():
    s = '#abc#de#eg#'
    assert reverse_and_filter(s) == 'geedcba'
