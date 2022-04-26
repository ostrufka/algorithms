'''
Selection Sort

Complexity: 
    * Execution time: O(n^2)
    * Memory: O(1)
'''

def slice_without_extensive_memory_consumption(sequence, current_idx):
    # return sequence[idx:] -> this way consume more memory
    for idx in range(current_idx, len(sequence)):
        yield sequence[idx]

def order(sequence: list) -> list:
    for current_idx, _ in enumerate(sequence):
        minimal_idx = current_idx
        # find minimal value between elements after the current
        for idx, elem in enumerate(slice_without_extensive_memory_consumption(sequence, current_idx)):
            if elem < sequence[minimal_idx]:
                minimal_idx = idx+current_idx
        # swipe current element and minimal element if current element is not the minimal element
        # python swap syntax without aux variable (using tuple)
        sequence[current_idx], sequence[minimal_idx] = sequence[minimal_idx], sequence[current_idx]
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
        self.assertListEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 9], order([9, 7, 1, 8, 5, 3, 6, 4, 2, 9]))

    def test_sorted_list(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], order([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

if __name__ == '__main__':
    unittest.main()