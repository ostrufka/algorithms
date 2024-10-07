"""
Problem: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

Example:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9

Análise: 
-> Tempo:  O(n)
-> Espaço: O(n)
"""

import doctest
from typing import List

def two_sum(nums: List, target: int):
    """
    >>> two_sum([2,7,11,15], 9)
    [0, 1]
    >>> two_sum([2,7,11,15], 26)
    [2, 3]
    """
    n = len(nums)
    indexes = {}
    for i in range(n):
        if target - nums[i] in indexes.keys():
            return [indexes[target - nums[i] ], i]
        indexes[nums[i]] = i
    

if __name__ == '__main__':
    doctest.testmod()

