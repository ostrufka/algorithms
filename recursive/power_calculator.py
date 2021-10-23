'''
Power Calculator (Recursive Algorithm)
'''

def power_iterative(base: int, exp: int):
    '''
    Complexity: 
        * Execution time: O(n)
        * Memory: O(1)
    '''
    result = 1
    for _ in range(exp):
        result *= base
    return result


def _power_recursive_linear(base, exp, result=1):
    '''
    Complexity: 
        * Execution time: O(n)
        f(n) = 4 + f(n-1) = 4*n
        * Memory: O(n)
        > if it were optimized for python: O(1)
    '''
    if exp == 0:
        return result
    return _power_recursive_linear(base, exp - 1, result * base)

def power_recursive_linear(base: int, exp: int):
    return _power_recursive_linear(base, exp - 1, base)


def _power_recursive_logarithmic(base, exp, result=1):
    '''
    if exp = even: base^(2*n) = (base*base)^n, where n = exp//2
    if exp = odd: base^(2*n + 1) = base*[(base*base)^n], where n = (exp-1)//2

    Complexity: 
        * Execution time: O(log(n))
        * Memory: O(?)
    '''
    if exp == 0:
        return result
    if exp % 2 == 0:
        return _power_recursive_logarithmic(base*base, exp//2, result)
    else:
        return _power_recursive_logarithmic(base*base, (exp-1)//2, result*base)

def power_recursive_logarithmic(base: int, exp: int):
    return _power_recursive_logarithmic(base, exp)

if __name__ == '__main__':
    base, exp = 5, 10
    print(f'Power: {power_iterative(base, exp)} (Interactive)')
    print(f'Power: {power_recursive_linear(base, exp)} (Recursive Linear)')
    print(f'Power: {power_recursive_logarithmic(base, exp)} (Recursive Logarithmic)')