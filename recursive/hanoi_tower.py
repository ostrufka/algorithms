'''
Hanoi Tower (Recursive Algorithm)

 A   B   C
_|_ _|_ _|_

Complexity: 
    * Execution time: O(2^n)
      f(n) = 1 + 2*f(n-1) = 1 + 2 + 4 + ... + 2^(n - 1) = 2^n - 1
    * Memory: O(n)
'''

hanoi_calls = 0

def _hanoi_tower_recursive(discs_num: int, origin='A', destine='B', aux='C'):
    global hanoi_calls
    hanoi_calls += 1
    if discs_num == 1:
        print(f'{origin} -> {destine} : {discs_num}')
        return
    _hanoi_tower_recursive(discs_num - 1, origin, aux, destine)
    print(f'{origin} -> {destine} : {discs_num}')
    _hanoi_tower_recursive(discs_num - 1, aux, destine, origin)

def hanoi_tower(discs_number: int):
    global hanoi_calls
    hanoi_calls = 0
    _hanoi_tower_recursive(discs_number)


if __name__ == '__main__':
    for i in range(1, 5):
        print(f'### Hanoi Tower - {i} discs ###')
        hanoi_tower(i)
        print(f'### {hanoi_calls} chamadas Hanoi!')
        print()
