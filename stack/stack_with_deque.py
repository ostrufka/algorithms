from collections import deque # python double linked list

class Pile:
    def __init__(self):
        self.__deque = deque()

    def __repr__(self):
        return repr(self.__deque)

    def is_empty(self):
        return len(self.__deque) == 0

    def top(self):
        try:
            return self.__deque[-1]
        except IndexError as e:
            raise EmptyListException('Empty pile!') from e

    def push(self, obj):
        self.__deque.append(obj)

    def pop(self):
        try:
            return self.__deque.pop()
        except IndexError as e:
            raise EmptyListException('Empty pile!') from e

class EmptyListException(Exception):
    pass

######### Unit Tests #########

import unittest

class TestPile(unittest.TestCase):
    def test_creation(self):
        Pile()

    def test_is_empty_with_empty_pile(self):
        pile = Pile()
        self.assertTrue(pile.is_empty())

    def test_is_empty_with_not_empty_pile(self):
        pile = Pile()
        pile.push('A')
        self.assertFalse(pile.is_empty())

    def test_top_with_empty_pile(self):
        pile = Pile()
        with self.assertRaises(EmptyListException):
            pile.top()

    def test_top_with_not_empty_pile(self):
        pile = Pile()
        pile.push('A')
        self.assertEqual('A', pile.top())
        self.assertFalse(pile.is_empty())

    def test_pop_with_empty_pile(self):
        pile = Pile()
        with self.assertRaises(EmptyListException):
            pile.pop()

    def test_pop_with_not_empty_pile(self):
        pile = Pile()
        pile.push('A')
        self.assertFalse(pile.is_empty())
        self.assertEqual('A', pile.pop())
        self.assertTrue(pile.is_empty())

    def test_FILO(self):
        pile = Pile()
        letters = 'ABCD'
        for letter in letters:
            pile.push(letter)
        for letter in reversed(letters):
            self.assertEqual(letter, pile.pop())
        self.assertTrue(pile.is_empty())

if __name__ == '__main__':
    unittest.main()

