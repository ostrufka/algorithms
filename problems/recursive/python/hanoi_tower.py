'''
Hanoi Tower (Recursive Algorithm)

 A   B   C
_|_ _|_ _|_

-> n: number of discs

Execution Stack (all discs from A to B):

Origin | Destine |  Aux  | Disc
-------|---------|-------|-----
   A   |    B    |   C   |  3   
   A   |    C    |   B   |  2  
   A   |    B    |   C   |  1     A -> B
   A   |    C    |   B   |  2     A -> C
   B   |    C    |   A   |  1     B -> C
   A   |    B    |   C   |  3     A -> B
   C   |    B    |   A   |  2  
   C   |    A    |   B   |  1     C -> A
   C   |    B    |   A   |  2     C -> B
   A   |    B    |   C   |  1     A -> B


Complexity: 
    * Time:  O(2^n) 
    * Space: O(n)
'''

import doctest

hanoi_call_count = 0

def _recursive_hanoi_tower(n: int, origin: str = 'A', destine: str = 'B', aux: str = 'C'):
    global hanoi_call_count
    hanoi_call_count += 1
    if n == 1:
        print(f'{origin} -> {destine} : {n}')
    else:
        _recursive_hanoi_tower(n - 1, origin=origin, destine=aux, aux=destine)
        print(f'{origin} -> {destine} : {n}')
        _recursive_hanoi_tower(n - 1, origin=aux, destine=destine, aux=origin)

def hanoi_tower(n: int):
    """
    >>> hanoi_tower(1)
    A -> B : 1
    Hanoi calls count = 1
    >>> hanoi_tower(2)
    A -> C : 1
    A -> B : 2
    C -> B : 1
    Hanoi calls count = 3
    >>> hanoi_tower(3)
    A -> B : 1
    A -> C : 2
    B -> C : 1
    A -> B : 3
    C -> A : 1
    C -> B : 2
    A -> B : 1
    Hanoi calls count = 7
    >>> hanoi_tower(4)
    A -> C : 1
    A -> B : 2
    C -> B : 1
    A -> C : 3
    B -> A : 1
    B -> C : 2
    A -> C : 1
    A -> B : 4
    C -> B : 1
    C -> A : 2
    B -> A : 1
    C -> B : 3
    A -> C : 1
    A -> B : 2
    C -> B : 1
    Hanoi calls count = 15
    """
    global hanoi_call_count
    hanoi_call_count = 0
    _recursive_hanoi_tower(n)
    print(f"Hanoi calls count = {hanoi_call_count}")

if __name__ == '__main__':
    doctest.testmod()