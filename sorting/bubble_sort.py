'''
Bubble Sort (with sentinel optimization)

Complexity: 
    * Execution time: best case O(n) / worst case O(n^2)
    * Memory: O(1)
'''

def order(sequence: list) -> list:
    sentinel, n = True, len(sequence)
    while sentinel:
        sentinel = False
        for idx, _ in enumerate(sequence):
            if idx == n-1: break
            if sequence[idx] > sequence[idx+1]:
                sequence[idx], sequence[idx+1] = sequence[idx+1], sequence[idx]
                sentinel = True
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