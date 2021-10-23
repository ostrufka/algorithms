import random

def max_min_iteractive(sequence):
    '''
    Complexity:
        * Execution time: O(n)
        * Memory: O(1)
    '''
    if not sequence:
        raise ValueError('Empty Sequence!')
    idx_max = 0
    idx_min = 0
    for value in sequence:
        if value > sequence[idx_max]:
            idx_max = sequence.index(value)
        elif value < sequence[idx_min]:
            idx_min = sequence.index(value)
    return sequence[idx_max], sequence[idx_min]


def _max_min_recursive(sequence, idx_max=0, idx_min=0, checked=0):
    '''
    Complexity:
        * Execution time: O(n)
        * Memory: O(1)
    ''' 
    seq_len = len(sequence) - checked
    if seq_len == 1:
        return sequence[idx_max], sequence[idx_min]
    if sequence[seq_len-1] > sequence[idx_max]:
        idx_max = seq_len-1
    elif sequence[seq_len-1] < sequence[idx_min]:
        idx_min = seq_len-1
    return _max_min_recursive(sequence, idx_max, idx_min, checked+1)

def max_min_recursive(sequence):
    if not sequence:
        raise ValueError('Empty Sequence!')
    return _max_min_recursive(sequence)

if __name__ == '__main__':
    seq = []
    for n in range(9):
        seq.append(random.randint(0, 100))
    
    print(f'Sequence = {seq}')
    max, min = max_min_iteractive(seq)
    print(f'Max value = {max}, Min value = {min} (iterative)')
    max, min = max_min_recursive(seq)
    print(f'Max value = {max}, Min value = {min} (recursive)')
