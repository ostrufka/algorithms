'''
Greed Paradigm ("ganacioso") - cash change example (less number of bills considering multiple bill values - ex: 1, 5, 10)
    -> Make a locally optimal choice at each stage to solve the global problem
    -> Sometimes the locally optimal step does not result in a global optimal solution
    -> Change example: this algorithm is not good for non-multiple dollar bills

Complexity: 
    * Execution time: O()
    * Memory: O()
'''

from collections import defaultdict

def zero_factory():
    return 0

def calc_change(value: int, bills: set) -> dict:
    change_result = defaultdict(zero_factory)
    ordered_bills = sorted(bills) # O(d.log(d)) d = number of different bills
    while value > 0 and ordered_bills:
        bill = ordered_bills.pop()
        number_of_bills, value = divmod(value, bill)
        if number_of_bills > 0:
            change_result[bill] = number_of_bills
    return change_result


######### Unit Tests #########

import unittest

class ChangeTests(unittest.TestCase):
    def test_no_bills(self):
        self.assertDictEqual({}, calc_change(9, {}))

    def test_10_dollar_bills(self):
        self.assertDictEqual({}, calc_change(9, {10}))
        self.assertDictEqual({10: 1}, calc_change(10, {10}))
        self.assertDictEqual({10: 10}, calc_change(100, {10}))
        
    def test_multiple_bills(self):
        self.assertDictEqual({10: 2, 5: 1, 1: 4}, calc_change(29, {10, 5, 1}))
        self.assertDictEqual({10: 10, 5: 1, 1: 2}, calc_change(107, {10, 5, 1}))
        self.assertDictEqual({100: 12, 50: 1, 10: 3, 5: 1, 1: 4}, calc_change(1289, {100, 50, 10, 5, 1}))

    def test_non_multiple_bills(self):
        self.assertDictEqual({10: 1, 1: 4}, calc_change(14, {10, 7, 1})) # not minimal number o bills (2x7)


if __name__ == '__main__':
    unittest.main()