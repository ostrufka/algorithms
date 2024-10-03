"""
Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces and the words are always separated by a single space.

For example,
Given s = “the sky is blue”,
return “blue is sky the”.

Could you do it in-place without allocating extra space?

Análise:
#1 Tempo = O(n) / Memória = O(n)
#2 Tempo = O(n) / Memória = O(1)
"""

import doctest
from typing import List
from collections import deque

def reverse_words_1(words: str):
    """
    >>> reverse_words_1("the sky is blue")
    'blue is sky the'
    """
    sliced_words = words.split(" ")
    sliced_words.reverse()
    return ' '.join(sliced_words)

def reverse_words_2(words: str):
    """
    >>> list(reverse_words_2("the sky is blue"))
    ['blue', 'is', 'sky', 'the']
    """
    word = deque()
    for letter in reversed(words):
        if letter == ' ':
            yield ''.join(word)
            word.clear()
        else:
            word.appendleft(letter)
    yield ''.join(word)

def reverse_words_3(words: List) -> List:
    """
    >>> list(reverse_words_3(['t', 'h', 'e', ' ', 's', 'k', 'y', ' ', 'i', 's', ' ', 'b', 'l', 'u', 'e']))
    ['b', 'l', 'u', 'e', ' ', 'i', 's', ' ', 's', 'k', 'y', ' ', 't', 'h', 'e']
    """
    n = len(words)
    for i in range(n):
        if i < n - 1 - i:
            words[i], words[n-1-i] = words[n-1-i], words[i]

    start = end = 0
    for i in range(n):
        if words[i] == ' ':
            if end != 0:
                start = end + 1
            end = i
            for j in range(end - start):
                if j < end - 1 - start - j:
                    words[start+j], words[end-1-j] = words[end-1-j], words[start+j]
    start = end + 1
    end = n
    for j in range(end - start):
        if j < end - 1 - start - j:
            words[start+j], words[end-1-j] = words[end-1-j], words[start+j]
    return words


if __name__ == '__main__':
    doctest.testmod()