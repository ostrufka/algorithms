from collections import deque
from distutils.command.build_scripts import first_line_re
from queue_with_deque import Queue


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

class LexicalError(Exception):
    pass

class SyntaxError(Exception):
    pass


def lexical_analysis(expression: str) -> Queue:
    '''
    Executes lexical analysis transforming the expression into a queue of objects (tokens):
    > check valid characters -> + - * / ( ) [ ] { } . integers
    '''
    number = ''
    valid_symbols = ['+','-','*','/','.','(','[','{',')',']','}']
    queue = Queue()
    for _char in expression:
        try:
            int(_char)
            number += _char
        except ValueError:
            if _char in valid_symbols:
                if number:
                    queue.enqueue(number)
                    number = ''
                queue.enqueue(_char)
            else:
                raise LexicalError('Invalid character in the expression.')
    if number:
        queue.enqueue(number)
    return queue

def syntax_analisis(token_queue: Queue) -> Queue:
    '''
    Executes syntax analysis on tokens produced by lexical analysis.
    Transform chars into:
    > integers -> int
    > floating point numbers -> float
    Return syntax queue with numeric tokens to be evaluated if no error occours.
    '''
    if token_queue.is_empty():
        raise SyntaxError('No tokens to be analysed.')
    special_chars = {')': '(', ']': '[', '}': '{'}
    integer, float_val = '', ''
    stack = Pile()
    queue = Queue()
    while not token_queue.is_empty():
        token = token_queue.dequeue()
        if token in '([{':
            stack.push(token)
        elif token in ')]}':
            if stack.is_empty() or stack.top() != \
                    special_chars[token]:
                raise SyntaxError('Unbalanced Expression.')
            stack.pop()
        try:
            int(token)
            integer = token
            if float_val:
                float_val += integer
                queue.enqueue(float(float_val))
                integer, float_val = '', ''
        except ValueError:
            if integer:
                if token == '.':
                    float_val = integer+token
                    continue
                else:
                    queue.enqueue(int(integer))
                    integer = ''
            queue.enqueue(token)
    if integer:
        queue.enqueue(int(integer))
    if not stack.is_empty():
        raise SyntaxError('Unbalanced Expression.')
    return queue

def evaluate(expression: str):
    '''
    Evaluates arithmetic expression.
    Return numeric value with result if no error occours.
    '''
    result = 0
    stack = Pile()
    queue = Queue()
    lexical_queue = lexical_analysis(expression)
    syntatic_queue = syntax_analisis(lexical_queue)
    first_elem = syntatic_queue.first()
    if first_elem != '(' or first_elem != '[' or first_elem != '{':
        syntatic_queue.enqueue(')')
    while not syntatic_queue.is_empty():
        token = syntatic_queue.dequeue()
        if isinstance(token, str):
            if token in '([{':
                if not queue.is_empty():
                    stack.push(queue)
                queue = Queue()
                continue
            elif token in ')]}':
                temp_result, operation = 0, ''
                while not queue.is_empty():
                    element = queue.dequeue()
                    if isinstance(element, int) or isinstance(element, float):
                        if operation == '':
                            temp_result = element
                        else:
                            if operation == '+':
                                temp_result += element
                            elif operation == '-':
                                temp_result -= element
                            elif operation == '*':
                                temp_result *= element
                            else:
                                try:
                                    temp_result = temp_result / float(element)
                                except ZeroDivisionError as e:
                                    raise e
                        operation = ''
                    else:
                        operation = element
                if stack.is_empty():
                    result = temp_result
                    break
                queue = stack.pop()
                queue.enqueue(temp_result)
                continue
        queue.enqueue(token)
    return result


######### Unit Tests #########

import unittest

class TestLexicalAnalysis(unittest.TestCase):
    def test_empty_expression(self):
        queue = lexical_analysis('')
        self.assertTrue(queue.is_empty())

    def test_invalid_character(self):
        self.assertRaises(LexicalError, lexical_analysis, 'a')
        self.assertRaises(LexicalError, lexical_analysis, 'ab')

    def test_one_integer_character(self):
        queue = lexical_analysis('1')
        self.assertEqual('1', queue.dequeue())
        self.assertTrue(queue.is_empty())

    def test_many_integer_characters(self):
        queue = lexical_analysis('1234567890')
        self.assertEqual('1234567890', queue.dequeue())
        self.assertTrue(queue.is_empty())

    def test_float(self):
        queue = lexical_analysis('1234567890.34')
        self.assertEqual('1234567890', queue.dequeue())
        self.assertEqual('.', queue.dequeue())
        self.assertEqual('34', queue.dequeue())
        self.assertTrue(queue.is_empty())

    def test_parentheses(self):
        queue = lexical_analysis('(1)')
        self.assertEqual('(', queue.dequeue())
        self.assertEqual('1', queue.dequeue())
        self.assertEqual(')', queue.dequeue())
        self.assertTrue(queue.is_empty())

    def test_chaves(self):
        queue = lexical_analysis('{(1)}')
        self.assertEqual('{', queue.dequeue())
        self.assertEqual('(', queue.dequeue())
        self.assertEqual('1', queue.dequeue())
        self.assertEqual(')', queue.dequeue())
        self.assertEqual('}', queue.dequeue())
        self.assertTrue(queue.is_empty())

    def test_brackets(self):
        queue = lexical_analysis('[{(1.0)}]')
        self.assertEqual('[', queue.dequeue())
        self.assertEqual('{', queue.dequeue())
        self.assertEqual('(', queue.dequeue())
        self.assertEqual('1', queue.dequeue())
        self.assertEqual('.', queue.dequeue())
        self.assertEqual('0', queue.dequeue())
        self.assertEqual(')', queue.dequeue())
        self.assertEqual('}', queue.dequeue())
        self.assertEqual(']', queue.dequeue())
        self.assertTrue(queue.is_empty())

    def test_adition(self):
        queue = lexical_analysis('1+2.0')
        self.assertEqual('1', queue.dequeue())
        self.assertEqual('+', queue.dequeue())
        self.assertEqual('2', queue.dequeue())
        self.assertEqual('.', queue.dequeue())
        self.assertEqual('0', queue.dequeue())
        self.assertTrue(queue.is_empty())

    def test_subtraction(self):
        queue = lexical_analysis('1-2.0')
        self.assertEqual('1', queue.dequeue())
        self.assertEqual('-', queue.dequeue())
        self.assertEqual('2', queue.dequeue())
        self.assertEqual('.', queue.dequeue())
        self.assertEqual('0', queue.dequeue())
        self.assertTrue(queue.is_empty())

    def test_multiplication(self):
        queue = lexical_analysis('1*2.0')
        self.assertEqual('1', queue.dequeue())
        self.assertEqual('*', queue.dequeue())
        self.assertEqual('2', queue.dequeue())
        self.assertEqual('.', queue.dequeue())
        self.assertEqual('0', queue.dequeue())
        self.assertTrue(queue.is_empty())

    def test_division(self):
        queue = lexical_analysis('1/2.0')
        self.assertEqual('1', queue.dequeue())
        self.assertEqual('/', queue.dequeue())
        self.assertEqual('2', queue.dequeue())
        self.assertEqual('.', queue.dequeue())
        self.assertEqual('0', queue.dequeue())
        self.assertTrue(queue.is_empty())

    def test_expression_with_all_symbols(self):
        expression = '1/{2.0+3*[7-(5-3)]}'
        queue = lexical_analysis(expression)
        self.assertListEqual(list(expression), [e for e in queue])
        self.assertTrue(queue.is_empty())


class TestSyntaxAnalysis(unittest.TestCase):
    def test_queue_is_empty(self):
        queue = Queue()
        self.assertRaises(SyntaxError, syntax_analisis, queue)

    def test_int(self):
        queue = Queue()
        queue.enqueue('1234567890')
        syntax_queue = syntax_analisis(queue)
        self.assertEqual(1234567890, syntax_queue.dequeue())
        self.assertTrue(syntax_queue.is_empty())

    def test_float(self):
        queue = Queue()
        queue.enqueue('1234567890')
        queue.enqueue('.')
        queue.enqueue('4')
        syntax_queue = syntax_analisis(queue)
        self.assertEqual(1234567890.4, syntax_queue.dequeue())
        self.assertTrue(syntax_queue.is_empty())

    def test_expression_with_all_elements(self):
        queue = lexical_analysis('1000/{222.125+3*[7-(5-3)]}')
        syntax_queue = syntax_analisis(queue)
        self.assertListEqual([1000, '/', '{', 222.125, '+', 3, '*', '[', 7, '-', '(', 5, '-', 3, ')', ']', '}'], [e for e in syntax_queue])

    def test_unbalanced_expression(self):
        expressions = [
            '1000/{222.125+3*[7-(5-3)]',
            '1000/{222.125+3*[7-(5-3)]}(',
            '1000/{222.125+3*[7-(5-3)])'
        ]
        for expression in expressions:
            queue = lexical_analysis(expression)
            self.assertRaises(SyntaxError, syntax_analisis, queue)


class TestEvaluation(unittest.TestCase):
    def test_is_empty_expression(self):
        self.assertRaises(SyntaxError, evaluate, '')

    def test_integer(self):
        self.assert_evaluate('1')

    def test_float(self):
        self.assert_evaluate('2.1')

    def test_sum(self):
        self.assert_evaluate('2+1')

    def test_subtraction_and_parentheses(self):
        self.assert_evaluate('(2-1)')

    def test_expressions_with_all_elements(self):
        self.assertEqual(1.0, evaluate('2.0/[4*3+1-{15-(1+3)}]'))
        self.assertEqual(5.0, evaluate('(25-5/[5-3*{1+9}]+4)'))
        self.assertEqual(15.0, evaluate('{20-[100*2/20-(40+5)*2]/6}'))

    def assert_evaluate(self, expression):
        self.assertEqual(eval(expression), evaluate(expression))

if __name__ == '__main__':
    unittest.main()