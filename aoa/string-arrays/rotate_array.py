"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4]. How many different ways do you know to solve this problem?

REF: https://www.programcreek.com/2015/03/rotate-array-in-java/
"""

import doctest
from typing import List

### Análise: O(n) em tempo e espaço.
def rotate_array(list: List, k: int):
    """
    >>> rotate_array([], 1)
    []
    >>> rotate_array([1], 2)
    [1]
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
        return list
    if k == 0:
        return list
    first = list[:n-k]
    last = list[n-k:]

    return last + first

### Análise: O(n) em tempo e O(1) espaço - rotação in-place.
def rotate_array_inplace(arr: List[int], k: int) -> List[int]:
    """
    >>> rotate_array_inplace([], 1)
    []
    >>> rotate_array_inplace([1], 2)
    [1]
    >>> rotate_array_inplace([1,2], 1)
    [2, 1]
    >>> rotate_array_inplace([1,2,3], 1)
    [3, 1, 2]
    >>> rotate_array_inplace([1,2,3], 2)
    [2, 3, 1]
    >>> rotate_array_inplace([1,2,3,4,5,6,7], 3)
    [5, 6, 7, 1, 2, 3, 4]
    >>> rotate_array_inplace([1,2,3,4,5,6,7], 2)
    [6, 7, 1, 2, 3, 4, 5]
    >>> rotate_array_inplace([1,2,3,4,5,6,7], 1)
    [7, 1, 2, 3, 4, 5, 6]
    >>> rotate_array_inplace([1,2,3,4,5,6,7], 0)
    [1, 2, 3, 4, 5, 6, 7]
    """
    n = len(arr)
    if n == 0 or k % n == 0:
        return arr

    k %= n  # In case k is greater than n
    # Step 1: Reverse the entire array
    arr.reverse()
    # Step 2: Reverse the first k elements
    arr[:k] = arr[:k][::-1]
    # arr[:k] = reversed(arr[:k])
    # Step 3: Reverse the remaining n-k elements
    # arr[k:] = reversed(arr[k:])
    arr[k:] = arr[k:][::-1]
    
    return arr



if __name__ == '__main__':
    doctest.testmod()

