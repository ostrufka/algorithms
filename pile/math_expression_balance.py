from pile_with_deque import Pile

class Balance:
    ''' 
    Function that calculates if an math expression has parenthesis '()', brakets '[]' and curly brakets (braces) '{}' in a balanced way.
    '''
    def __init__(self):
        self.__pile = Pile()
        self.__special_chars = {')': '(', ']': '[', '}': '{'}

    def is_balanced(self, expr: str):
        '''
        Complexity:
          * Time: O(n)
          * Space: O(n)
        '''
        if not expr:
            return True
        for _char in expr:
            if _char in '([{': 
                self.__pile.push(_char)
            elif _char in ')]}':
                if self.__pile.is_empty() or self.__pile.top() != \
                        self.__special_chars[_char]:
                    return False
                self.__pile.pop()
        return self.__pile.is_empty()


######### Unit Tests #########

import unittest

class TestBalance(unittest.TestCase):
    def test_empty_expression(self):
        balance = Balance()
        self.assertTrue(balance.is_balanced(''))

    def test_parentheses(self):
        balance = Balance()
        self.assertTrue(balance.is_balanced('()'))

    def test_curly_brakets(self):
        balance = Balance()
        self.assertTrue(balance.is_balanced('{}'))

    def test_brakets(self):
        balance = Balance()
        self.assertTrue(balance.is_balanced('[]'))

    def test_all_characters(self):
        balance = Balance()
        self.assertTrue(balance.is_balanced('({[]})'))
        self.assertTrue(balance.is_balanced('[({})]'))
        self.assertTrue(balance.is_balanced('{[()]}'))

    def test_curly_brakets_not_closed(self):
        balance = Balance()
        self.assertFalse(balance.is_balanced('{'))

    def test_brakets_not_closed(self):
        balance = Balance()
        self.assertFalse(balance.is_balanced('['))

    def test_parentheses_not_closed(self):
        balance = Balance()
        self.assertFalse(balance.is_balanced('('))

    def test_curly_brakets_not_opened(self):
        balance = Balance()
        self.assertFalse(balance.is_balanced('}{'))

    def test_brakets_not_opened(self):
        balance = Balance()
        self.assertFalse(balance.is_balanced(']['))

    def test_parentheses_not_opened(self):
        balance = Balance()
        self.assertFalse(balance.is_balanced(')('))

    def test_lack_of_close_character(self):
        balance = Balance()
        self.assertFalse(balance.is_balanced('({[]}'))

    def test_lack_of_open_character(self):
        balance = Balance()
        self.assertFalse(balance.is_balanced('({]})'))

    def test_valid_math_expression(self):
        balance = Balance()
        self.assertTrue(balance.is_balanced('({[1+3]*5}/7)+9'))

    def test_error_close_charactere(self):
        balance = Balance()
        self.assertFalse(balance.is_balanced('[)'))

    def test_charactere_wrong_order(self):
        balance = Balance()
        self.assertFalse(balance.is_balanced('[(])'))

if __name__ == '__main__':
    unittest.main()

