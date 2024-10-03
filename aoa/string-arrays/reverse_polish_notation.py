"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, /. Each operand may be an integer or another expression. For example:

  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

Análise:
#1 Tempo = O(n) / Memória = O(n)
"""

import doctest
from typing import List

class InvalidException(Exception):
    pass
    
def calculate(operand1, operand2, operator):
    try:
        if operator == "+":
            return int(operand1) + int(operand2)
        elif operator == "-":
            return int(operand1) - int(operand2)
        elif operator == "*":
            return int(operand1) * int(operand2)
        elif operator == "/":
            return int(operand1) // int(operand2)
    except (ValueError, TypeError) as e:
        return e

def reverse_polish_notation(equation: List[str]) -> int:
    """
    >>> reverse_polish_notation(["2", "1", "+", "3", "*"])
    9
    >>> reverse_polish_notation(["4", "13", "5", "/", "+"])
    6
    >>> reverse_polish_notation(["4", "a", "5", "/", "+"])
    TypeError("int() argument must be a string, a bytes-like object or a number, not 'ValueError'")
    >>> reverse_polish_notation(["4", "2"])
    <class 'ValueError'>
    """
    operators = ["+", "-", "*", "/"]
    n = len(equation)
    if n < 3:
        return ValueError

    exp = []
    exp.append(equation[0])
    exp.append(equation[1])
    for i in range(2, n):
        if equation[i] in operators:
            op2 = exp.pop()
            op1 = exp.pop()
            exp.append(calculate(op1, op2, equation[i]))
        else:
            exp.append(equation[i])

    return exp[0]


if __name__ == '__main__':
    doctest.testmod()