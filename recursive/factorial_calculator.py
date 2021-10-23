'''
Factorial Calculator (Recursive Algorithm)
'''

def factorial_iteractive(factor: int, factorial=1):
    '''
    Complexity: O(n)
    '''
    if factor <= 1:
        return factorial
    for i in range(factor, 1, -1):
        factorial *= i
    return factorial

def _factorial_recursive(factor, factorial=1):
    '''
    Complexity: O(n)
    '''
    if factor <= 1:
        return factorial
    return _factorial_recursive(factor - 1, factorial * factor)

def factorial_recursive(factor: int):
    return _factorial_recursive(factor)


if __name__ == '__main__':
    factor = 5
    print(f'Factorial of {factor}: {factorial_iteractive(factor)} (Interactive)')
    print(f'Factorial of {factor}: {factorial_recursive(factor)} (Recursive)')