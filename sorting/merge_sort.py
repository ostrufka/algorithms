'''
Merge Sort

Complexity: 
    * Execution time: O(n.log(n))
    * Memory: O()
'''

def divide(sequence: list):
    half = len(sequence) // 2
    left = order(sequence[:half])
    right = order(sequence[half:])
    return left, right

def merge(left: list, right: list) -> list:
    sorted_list, left_len, right_len, i, j = [], len(left), len(right), 0, 0
    while i <= left_len - 1 and j <= right_len - 1:
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list += left[i:]
    sorted_list += right[j:]
    return sorted_list

def order(sequence: list) -> list:
    size = len(sequence)
    if size < 2: 
        return sequence
    left, right = divide(sequence)
    return merge(left, right) # conquer


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