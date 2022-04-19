'''
Bubble Sort

Complexity: 
    * Execution time: O()
    * Memory: O()
'''

def slice_without_extensive_memory_consumption(sequence, current_idx):
    # return sequence[idx:] -> this way consume more memory
    for idx in range(current_idx, len(sequence)):
        yield sequence[idx]

def order(sequence: list) -> list:
    
    return sequence


######### Unit Tests #########

import unittest

class OrderTests(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual([], order([]))

    def test_unitary_list(self):
        self.assertListEqual([1], order([1]))

    def test_binary_list(self):
        self.assertListEqual([1, 2], order([2, 1]))

    def test_unsorted_list(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], order([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()