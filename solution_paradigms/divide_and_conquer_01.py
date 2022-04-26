'''
Divide and Conquer Paradigm - cash change example (less number of bills for any bills set)
    -> Divide a bigger problem into smaller problems and solve each one to solve the global
    -> Normally used: recursion

Complexity: 
    * Execution time: O(n^n)
    * Memory: O()

Solution developed by myself
'''

from cmath import inf
from typing import Tuple

def calc_change_for_specific_bill(value: int, bill: int) -> Tuple[int, int]:
    number_of_bills = 0
    while value > 0:
        value = value - bill
        if value < 0:
            value = value + bill
            break
        number_of_bills += 1
    return value, number_of_bills

def calc_change_possibilities(value: int, bills: set) -> list:
    current_change, all_change_possibilities, other_possible_changes = {}, [], []
    inverse_ordered_bills = sorted(bills, reverse=True) # O(d.log(d)) d = number of different bills
    for idx, bill in enumerate(inverse_ordered_bills):
        if idx == 0 and len(inverse_ordered_bills) > 1: 
            bills.remove(bill)
            other_possible_changes = calc_change_possibilities(value, bills)
        value, number_of_bills = calc_change_for_specific_bill(value, bill)
        if number_of_bills > 0: current_change[bill] = number_of_bills
    if current_change: all_change_possibilities.append(current_change)
    if isinstance(other_possible_changes, list): all_change_possibilities.extend(other_possible_changes)
    return all_change_possibilities

def calc_minimum_change(possible_changes: list) -> dict:
    min_sum_of_bills, min_change = inf, {}
    for change in possible_changes:
        sum_of_bills = sum(change.values())
        if sum_of_bills < min_sum_of_bills:
            min_sum_of_bills = sum_of_bills
            min_change = change
    return min_change

def calc_change(value: int, bills: set) -> dict:
    possible_changes = calc_change_possibilities(value, bills) # divide
    min_change = calc_minimum_change(possible_changes) # conquer
    return min_change


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
        self.assertDictEqual({10: 10, 5: 1, 2: 1}, calc_change(107, {10, 5, 2}))
        self.assertDictEqual({100: 12, 20: 1, 10: 1, 2: 2}, calc_change(1234, {100, 50, 20, 10, 5, 2}))

    def test_non_multiple_bills(self):
        self.assertDictEqual({7: 2}, calc_change(14, {10, 7, 1}))
        self.assertDictEqual({30: 1, 2: 1, 1: 1}, calc_change(33, {30, 10, 2, 1}))
        self.assertDictEqual({50: 1, 10: 1, 7: 1}, calc_change(67, {50, 20, 10, 7, 1}))

if __name__ == '__main__':
    unittest.main()