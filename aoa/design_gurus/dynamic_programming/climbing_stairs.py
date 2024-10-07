"""
Problem: You are climbing a staircase. It takes n steps to reach the top. Each time you can climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example:

Input: n = 3
Output: 3
Explanations:
1 step + 1 step + 1 step
1 step + 2 steps
2 steps + 1 step

Análise: 
-> Tempo:  O(n)
-> Espaço: O(n)
"""

import doctest
from typing import List

def climbing_stairs_bottom_up(steps:int) -> int:
    if steps < 2:
        return 1
    bottom_up = [0] * (steps + 1)
    bottom_up[1] = 1
    bottom_up[2] = 2
    for i in range(3, steps+1):
        bottom_up[i] = bottom_up[i - 1] + bottom_up[i - 2]
    return bottom_up[steps]

def climbing_stairs_memoize(steps: int, memoize: List) -> int:
    if memoize[steps]:
        return memoize[steps]
    ways = 0
    if steps == 0:
        return ways + 1
    if steps > 1:
        ways += climbing_stairs_memoize(steps - 2, memoize)
    ways += climbing_stairs_memoize(steps - 1, memoize)
    memoize[steps] = ways
    return ways

def climbing_stairs(steps: int):
    """
    >>> climbing_stairs(3)
    3
    >>> climbing_stairs(4)
    5
    >>> climbing_stairs(5)
    8
    >>> climbing_stairs(6)
    13
    >>> climbing_stairs(7)
    21
    >>> climbing_stairs(10)
    89
    """
    # memoize = [None] * (steps + 1)
    # return climbing_stairs_memoize(steps, memoize)
    return climbing_stairs_bottom_up(steps)

if __name__ == '__main__':
    doctest.testmod()
