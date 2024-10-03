"""
Given two strings s and t, determine if they are isomorphic. Two strings are isomorphic if the characters in s can be replaced to get t.

For example,”egg” and “add” are isomorphic, “foo” and “bar” are not.

Analise: O(n) para tempo e memoria
"""

import doctest

def isomorphic1(s: str, t: str) -> bool:
    """
    >>> isomorphic1("egg", "add")
    True
    >>> isomorphic1("foo", "bar")
    False
    >>> isomorphic1("banana", "arara")
    False
    >>> isomorphic1("tool", "cool")
    True
    >>> isomorphic1("ama", "ora")
    False
    >>> isomorphic1("ama", "ooo")
    True
    """
    s_len = len(s)
    t_len = len(t)
    if s_len != t_len:
        return False
    correspondence = {}
    for i in range(s_len):
        if correspondence.get(s[i]) is None:
            correspondence.update({s[i]: t[i]})
    replaced = ""
    for i in range(s_len):
        replaced += correspondence.get(s[i])
    return replaced == t
    
def isomorphic2(s: str, t: str) -> bool:
    """
    >>> isomorphic2("egg", "add")
    True
    >>> isomorphic2("foo", "bar")
    False
    >>> isomorphic2("banana", "arara")
    False
    >>> isomorphic2("tool", "cool")
    True
    >>> isomorphic2("ama", "ora")
    False
    >>> isomorphic2("ama", "ooo")
    True
    """
    if len(s) != len(t):
        return False
    correspondence = {}

    for s_char, t_char in zip(s, t):
        try:
            char_match = (correspondence[s_char] == t_char)
        except KeyError:
            correspondence[s_char] = t_char
        else:
            if not char_match:
                return False
    return True

if __name__ == '__main__':
    doctest.testmod()