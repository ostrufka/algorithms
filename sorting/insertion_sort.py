'''
Insertion Sort

Complexity: 
    * Execution time: best case O(n) / worst case O(n^2)
    * Memory: O(1)
'''

def order(sequence: list) -> list:
    n = len(sequence)
    for current_idx in range(n-1):
        idx = current_idx + 1
        while idx - 1 >= 0:
            if sequence[idx] < sequence[idx-1]:
                sequence[idx], sequence[idx-1] = sequence[idx-1], sequence[idx]
                idx -= 1
            else:
                break
    return sequence

# Not so good implementation
#
# def inverted_slice_without_extensive_memory_consumption(sequence, current_idx):
#     # return sequence[:idx] -> this way consume more memory
#     for idx in range(0, current_idx):
#         yield sequence[idx]
#
# def order(sequence: list) -> list:
#     for current_idx, _ in enumerate(sequence):
#         for idx, elem in enumerate(inverted_slice_without_extensive_memory_consumption(sequence, current_idx)):
#             if sequence[current_idx] < elem:
#                 sequence.insert(idx, sequence[current_idx])
#                 del sequence[current_idx+1]
#                 break
#     return sequence


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