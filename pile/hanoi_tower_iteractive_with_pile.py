'''
Hanoi Tower (Iteractive implementation with Pile)

 A   B   C
_|_ _|_ _|_

Complexity: 
    * Execution time: O(2^n)
    * Memory: O(n)
'''

from pile_with_deque import Pile

REC_CALL = 'CALL'
RETURN_CALL = 'RETURN'

def hanoi_tower(discs_num: int):
    '''
    >>> hanoi_tower(1)
    A -> B : 1

    >>> hanoi_tower(2)
    A -> C : 1
    A -> B : 2
    C -> B : 1

    >>> hanoi_tower(3)
    A -> B : 1
    A -> C : 2
    B -> C : 1
    A -> B : 3
    C -> A : 1
    C -> B : 2
    A -> B : 1

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
    '''
    origin, destine, aux = 'A', 'B', 'C'
    pile = Pile()
    pile.push((REC_CALL, discs_num, origin, destine, aux))
    while not pile.is_empty():
        operation, discs_num, origin, destine, aux  = pile.pop()
        if discs_num == 1:
            print(f'{origin} -> {destine} : {discs_num}')
        elif operation == REC_CALL:
            pile.push((RETURN_CALL, discs_num, origin, destine, aux))
            pile.push((REC_CALL, discs_num-1, origin, aux, destine))
        elif operation == RETURN_CALL:
            print(f'{origin} -> {destine} : {discs_num}')
            pile.push((REC_CALL, discs_num-1, aux, destine, origin))
