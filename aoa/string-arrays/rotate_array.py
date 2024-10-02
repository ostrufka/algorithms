"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4]. How many different ways do you know to solve this problem?

REF: https://www.programcreek.com/2015/03/rotate-array-in-java/

### Análise: O(n) em tempo e espaço.
"""

import doctest
from typing import List

def rotate_array(list: List, k: int):
    """
    >>> rotate_array([], 1)
    []
    >>> rotate_array([1], 2)
    []
    >>> rotate_array([1,2], 1)
    [2, 1]
    >>> rotate_array([1,2,3], 1)
    [3, 1, 2]
    >>> rotate_array([1,2,3], 2)
    [2, 3, 1]
    >>> rotate_array([1,2,3,4,5,6,7], 3)
    [5, 6, 7, 1, 2, 3, 4]
    >>> rotate_array([1,2,3,4,5,6,7], 2)
    [6, 7, 1, 2, 3, 4, 5]
    >>> rotate_array([1,2,3,4,5,6,7], 1)
    [7, 1, 2, 3, 4, 5, 6]
    >>> rotate_array([1,2,3,4,5,6,7], 0)
    [1, 2, 3, 4, 5, 6, 7]
    """
    n = len(list)
    if n == 0 or k > n:
        return []
    if k == 0:
        return list
    # first = list[:n-k]
    # last = list[n-k:]

    # return last + first
    rotated = []
    for i in range(n):
        if i < k:
            rotated[i + k] = list[i]
        else:
            rotated[i - k] = list[i]
    return rotated


if __name__ == '__main__':
    doctest.testmod()

