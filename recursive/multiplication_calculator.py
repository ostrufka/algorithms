'''
Multiplication Calculator (Recursive Algorithm)
'''

def multiply_iterative(multiplicand: int, multiplier: int):
    '''
    Complexity: O(n)
    '''
    product = 0
    for _ in range(multiplier):
        product += multiplicand
    return product


def _multiply_recursive(multiplicand, multiplier, product=0):
    '''
    Complexity: O(n)
    f(n) = 2 + f(n-1) = 2 + 2 + f(n-2) = 2*n
    '''
    if multiplier == 0:
        return product
    product += multiplicand
    return _multiply_recursive(multiplicand, multiplier - 1, product)

def multiply_recursive(multiplicand: int, multiplier: int):
    return _multiply_recursive(multiplicand, multiplier)


if __name__ == '__main__':
    multiplicand, multiplier = 7, 2
    print(f'Multiply: {multiplicand} x {multiplier} = {multiply_iterative(multiplicand, multiplier)} (Interactive)')
    print(f'Multiply: {multiplicand} x {multiplier} = {multiply_recursive(multiplicand, multiplier)} (Recursive)')