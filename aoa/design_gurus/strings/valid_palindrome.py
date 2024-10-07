"""
Problem: Given a string s, return true if it is a palindrome, and false otherwise.

Example:

Input: s = "A man, a plan, a canal: Panama" 
Output: true

Análise: 
-> Tempo:  O(n)
-> Espaço: O(n)
"""

import doctest
import unicodedata

import re

def isPalindrome(s):
  s = s.lower()
  s = re.sub('[^a-zA-Z0-9]', '', s)

  return s == s[::-1]

def valid_palindrome(s: str) -> bool:
    """
    >>> valid_palindrome("A man, a plan, a canal: Panama")
    True
    >>> valid_palindrome("A woman, a car, a film: Panama")
    False
    >>> valid_palindrome("Rir, o breve verbo rir.")
    True
    >>> valid_palindrome("Socorram-me, subi no ônibus em Marrocos!")
    True
    """
    no_accent_s = unicodedata.normalize("NFD", s)
    no_accent_s = no_accent_s.encode("ascii", "ignore")
    no_accent_s = no_accent_s.decode("utf-8")
    filtered_s = [e.lower() for e in no_accent_s if e.isalnum()]
    n = len(filtered_s)
    original_filtered_s = filtered_s
    for i in range(n//2):
        if filtered_s[i] != filtered_s[n-1-i]:
            return False
    return True


if __name__ == '__main__':
    doctest.testmod()

