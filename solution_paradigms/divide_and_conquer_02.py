'''
Divide and Conquer Paradigm - cash change example (less number of bills for any bills set)
    -> Divide a bigger problem into smaller problems and solve each one to solve the global
    -> Normally used: recursion

Complexity: 
    * Execution time: O(n^n)
    * Memory: O()

Solution developed by Renzo
'''

from cmath import inf
from typing import Dict
from collections import defaultdict

def zero_factory():
    return 0

impossible_solution = defaultdict(zero_factory)
impossible_solution[-1] = inf

def calculate_better_solution(solution: dict, other_solution: dict) -> dict:
    if sum(solution.values()) < sum(other_solution.values()):
        return solution
    return other_solution

def calculate_change_recursively(value: int, bills: set, partial_solution: Dict[int, int]) -> dict:
    if value == 0:
        return partial_solution
    elif value < 0 or len(bills) == 0:
        return impossible_solution

    bills_without_chosen_bill = set(bills)
    chosen_bill = bills_without_chosen_bill.pop()

    possible_solution = defaultdict(zero_factory)
    possible_solution.update(partial_solution)
    possible_solution[chosen_bill] += 1

    # divide
    solution_with_chosen_bill = calculate_change_recursively(value - chosen_bill, bills, possible_solution)
    solution_without_chosen_bill = calculate_change_recursively(value, bills_without_chosen_bill, partial_solution)

    # conquer
    return calculate_better_solution(solution_with_chosen_bill, solution_without_chosen_bill)


def calc_change(value: int, bills: set) -> dict:
    initial_solution = defaultdict(zero_factory)
    return calculate_change_recursively(value, bills, initial_solution)


######### Unit Tests #########

import unittest

class ChangeTests(unittest.TestCase):
    def test_no_bills(self):
        self.assertDictEqual(impossible_solution, calc_change(9, {}))

    def test_10_dollar_bills(self):
        self.assertDictEqual(impossible_solution, calc_change(9, {10}))
        self.assertDictEqual({10: 1}, calc_change(10, {10}))
        self.assertDictEqual({10: 10}, calc_change(100, {10}))
        
    def test_multiple_bills(self):
        self.assertDictEqual({10: 2, 5: 1, 1: 4}, calc_change(29, {10, 5, 1}))
        self.assertDictEqual({10: 10, 5: 1, 2: 1}, calc_change(107, {10, 5, 2}))

    def test_non_multiple_bills(self):
        self.assertDictEqual({7: 2}, calc_change(14, {10, 7, 1}))
        self.assertDictEqual({30: 1, 2: 1, 1: 1}, calc_change(33, {30, 10, 2, 1}))
        self.assertDictEqual({50: 1, 10: 1, 7: 1}, calc_change(67, {50, 20, 10, 7, 1}))

if __name__ == '__main__':
    unittest.main()