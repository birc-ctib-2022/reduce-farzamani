# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from reduce import (
    reduce, accumulate
)

from random import randint
from itertools import accumulate as py_accumulate
from functools import reduce as py_reduce


def test_reduce():
    def add(x, y): return x+y
    def prod(x, y): return x*y
    for _ in range(10):
        x = [randint(1, 10) for _ in range(10)]
        assert reduce(add, x) == py_reduce(add, x)
        assert reduce(prod, x) == py_reduce(prod, x)


def test_accumulate():
    def add(x, y): return x+y
    def prod(x, y): return x*y
    for _ in range(10):
        x = [randint(1, 10) for _ in range(10)]
        # NB! py_accumulate takes the args in swapped order
        # and returns an iterator we have to translate to a
        # list for comparison
        assert accumulate(add, x) == list(py_accumulate(x, add))
        assert accumulate(prod, x) == list(py_accumulate(x, prod))
