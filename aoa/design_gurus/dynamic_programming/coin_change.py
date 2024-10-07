"""
Problem: Given coins of different denominations and amount, find number of ways to make up the amount.

Example:

Coins: [1, 2, 5]
Amount: 5
Output: 2
Explanations: 5=5, 2+2+1

Análise: 
-> Tempo:  O()
-> Espaço: O()
"""

import doctest
from typing import List   

def count(coins: List, n: int, amount: int, memo: List) -> int:
    if memo[n][amount] != -1:
        return memo[n][amount]
    if amount == 0:
        memo[n][amount] = 1
        return memo[n][amount]
    if n <= 0 or amount < 0:
        return 0
    memo[n][amount] = count(coins, n, amount - coins[n - 1], memo) + count(coins, n - 1, amount, memo)
    return memo[n][amount]
    

def coin_change(coins: List, amount: int):
    """
    >>> coin_change([1, 2, 3], 4)
    4
    >>> coin_change([2, 5, 3, 6], 10)
    5
    >>> coin_change([10], 10)
    1
    >>> coin_change([4], 5)
    0
    """
    n = len(coins)
    memo = [[-1 for i in range(amount + 1)] for j in range(n + 1)]
    return count(coins, n, amount, memo)
    

if __name__ == '__main__':
    doctest.testmod()
