"""Reduce and accumulate module"""

from typing import TypeVar, Callable
A = TypeVar('A')
B = TypeVar('B')


def reduce(f: Callable[[A], B], x: list[A]) -> B:
    """
    Reduce f over list x.x

    >>> reduce(lambda x,y: x+y, [1, 2, 3])
    6
    >>> reduce(lambda x,y: x*y, [1, 2, 3, 4])
    24
    """
    assert len(x) >= 2
    
    # Initialize the first element
    item = x[0]

    # Iterate the operation until the last element
    for i in range(1, len(x)):
        item = f(item, x[i])
    
    return item

def accumulate(f: Callable[[A], A], x: list[A]) -> list[A]:
    """
    Accumulate f over list x.x

    >>> accumulate(lambda x,y: x+y, [1, 2, 3])
    [1, 3, 6]
    >>> accumulate(lambda x,y: x*y, [1, 2, 3, 4])
    [1, 2, 6, 24]
    """
    assert len(x) >= 2

    # Create a list for the output
    out_list = [0] * len(x)

    # Initialize first element of the output list
    out_list[0] = x[0]

    # Iterate the operation
    # from second element to the last element
    # of the input list
    for i in range(1, len(x)):
        out_list[i] = f(out_list[i-1], x[i])

    return out_list