

class Pile:
    def __init__(self):
        self.__list = list()

    def __repr__(self):
        return repr(self.__list)

    def is_empty(self):
        return len(self.__list) == 0

    def top(self): # O(1)
        try:
            return self.__list[-1]
        except IndexError as e:
            raise EmptyListException('Empty pile!') from e

    def push(self, obj): # O(1)*
        self.__list.append(obj)

    def pop(self): # O(1)*
        try:
            return self.__list.pop()
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

