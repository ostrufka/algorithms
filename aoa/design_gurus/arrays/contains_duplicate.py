"""
Problem: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example:

Input: nums = [1,2,3,1]
Output: true

Análise: 
-> Tempo:  O(n)
-> Espaço: O(n)
"""

import doctest
from typing import List

def contains_duplicate(nums: List[int]) -> bool:
    """
    >>> contains_duplicate([1,2,3,1])
    True
    >>> contains_duplicate([1,2,3,4])
    False
    >>> contains_duplicate([1,2,3,4,5,2,7,8])
    True
    """
    seen = []
    for num in nums:
        if num in seen:
            return True
        seen.append(num)
    return False

if __name__ == '__main__':
    doctest.testmod()

