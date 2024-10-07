"""
Problem: Given an integer array nums, find the contiguous subarray with the largest sum.

Example:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Análise: 
-> Tempo:  O(n)
-> Espaço: O(1)
"""

import doctest
from typing import List

def max_subarray(nums: List) -> int:
    """
    >>> max_subarray([-2,1,-3,4,-1,2,1,-5,4])
    6
    """
    sum = 0
    max_sum = float('-inf')
    n = len(nums)
    for i in range(n):
        sum += nums[i]
        if sum < 0:
            sum = 0
        if sum > max_sum:
            max_sum = sum
    return max_sum


if __name__ == '__main__':
    doctest.testmod()

