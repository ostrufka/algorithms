"""
Problem: Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example:

Input: s = "anagram", t = "nagaram"
Output: true

Análise: 
-> Tempo:  O(n)
-> Espaço: O(n)
"""

import doctest
from typing import Dict

def count_letters(word: str) -> Dict:
    letter_count = {}
    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

def valid_anagram(s: str, t: str) -> bool:
    """
    >>> valid_anagram("anagram", "nagaram")
    True
    >>> valid_anagram("anagram", "nagarim")
    False
    >>> valid_anagram("ovo", "voo")
    True
    >>> valid_anagram("arara", "arraia")
    False
    """
    s_len = len(s)
    t_len = len(t)
    if s_len != t_len:
        return False
    s_count = count_letters(s)
    t_count = count_letters(t)
    if s_count == t_count:
        return True
    return False
    

if __name__ == '__main__':
    doctest.testmod()

