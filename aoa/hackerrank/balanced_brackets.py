"""
Problem description: https://www.hackerrank.com/challenges/balanced-brackets/problem

Análise Assintótica:
-> Tempo: O(n)
-> Memória: O(n/2) -> O(n)
"""

#!/bin/python3

import os

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

class ExceptionStringTooBig(Exception):
    pass
    
class ExceptionInvalidBracket(Exception):
    pass
    
class ExceptionTooManyInputs(Exception):
    pass
    
class ExceptionEmptyString(Exception):
    pass

def isBalanced(s: str) -> str:
    valid_brackets = {
        "}": "{",
        "]": "[",
        ")": "("
    }
    close_brackets = valid_brackets.keys()
    open_brackets = valid_brackets.values()
    brackets_stack = []
    n = len(s)
    
    if n > 1001:
        raise ExceptionStringTooBig("Input string must be < 1000 characters")
    elif n == 0:
        raise ExceptionEmptyString("Input string is empty")

    for i in range(n):
        if s[i] not in open_brackets and s[i] not in close_brackets:
            raise ExceptionInvalidBracket(f"{s[i]} is not a valid bracket")

        if i == 0 and s[i] not in open_brackets:
            return "NO"

        if not brackets_stack:
            brackets_stack.append(s[i])
        else:
            if s[i] in open_brackets:
                brackets_stack.append(s[i])
            else:
                last_bracket = brackets_stack.pop()
                if last_bracket != valid_brackets[s[i]]:
                    return "NO"
    if brackets_stack:
        return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())
    
    if t > 1001:
        raise ExceptionTooManyInputs("Inputs number must be up to 1000")

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
