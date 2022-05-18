'''
Quick Sort in-place (random pivot and no sublist creation)

Complexity: 
    * Execution time: O(n.log(n)) | O(n^2)
    * Memory: O(log(n))
'''

from random import randint

def quick_sort_in_place(seq: list, i_idx: int, f_idx: int) -> list:
    initial, final = i_idx, f_idx
    if initial >= final: return seq

    # Select pivot and move it to the end
    p_idx = randint(i_idx, f_idx)
    seq[p_idx], seq[f_idx], p_idx = seq[f_idx], seq[p_idx], f_idx
 
    while i_idx < f_idx:
        # Ascending search
        idx = i_idx
        while seq[idx] < seq[p_idx]:
            idx += 1
        if idx < p_idx:
            seq[p_idx], seq[idx], p_idx = seq[idx], seq[p_idx], idx
            f_idx -= 1
        else:
            f_idx = p_idx
        # Descendind search
        idx = f_idx
        while seq[idx] > seq[p_idx]:
            idx -= 1
        if idx > p_idx:
            seq[p_idx], seq[idx], p_idx = seq[idx], seq[p_idx], idx
            i_idx += 1
        else:
            i_idx = p_idx

    seq = quick_sort_in_place(seq, initial, p_idx - 1)
    seq = quick_sort_in_place(seq, p_idx + 1, final)
    return seq

def order(sequence: list) -> list:
    initial_idx, final_idx = 0, len(sequence) - 1
    return quick_sort_in_place(sequence, initial_idx, final_idx)


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
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], order([1, 7, 3, 8, 5, 9, 6, 4, 0, 2]))
        self.assertListEqual([0, 3, 4, 5, 6, 7, 7, 8, 9, 9], order([6, 9, 3, 8, 5, 9, 7, 4, 0, 7]))
        self.assertListEqual([1, 1, 1, 1, 1, 9, 9, 9, 9, 9], order([9, 1, 9, 1, 9, 1, 9, 1, 9, 1]))

    def test_sorted_list(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], order([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))


if __name__ == '__main__':
    unittest.main()