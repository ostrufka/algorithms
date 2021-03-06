'''
Quick Sort (random pivot)

Complexity: 
    * Execution time: O(n.log(n)) | O(n^2)
    * Memory: O()
'''

from random import randint

def order(sequence: list) -> list:
    sequence_size = len(sequence)
    if sequence_size <= 1:
        return sequence
    
    greaters, lowers = [], []
    # pivot = sequence.pop() # pivot as last element
    pivot_idx = randint(0, sequence_size-1)
    pivot = sequence[pivot_idx]
    sequence.remove(pivot)

    # divide
    lowers = [n for n in sequence if n < pivot]
    sorted_lowers = order(lowers)
    greaters = [n for n in sequence if n >= pivot]
    sorted_greaters = order(greaters)

    # conquer
    sorted_list = sorted_lowers + [pivot] + sorted_greaters
    return sorted_list


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