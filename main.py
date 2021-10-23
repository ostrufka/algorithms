# ---------------------------- #
# Algorithms & Data Structutes #
# ---------------------------- #

'''
Big-O Notation: 
O(1)
O(log(n))
O(n)
O(n.log(n))
O(nˆ2)
O(nˆc)
O(cˆn)
O(n!)
O(nˆn)

Greedy Algorithm: Try to make locally optimal choices at each stage expecting to get the best global result (does not work always).
'''

import time

class SortingAlgoritms:
    def __init__(self):
        pass

    def check_args_and_timing(func):
        def wrapper(*args, **kwargs):
            ul = args[-1]
            ulen = len(ul)
            if ulen < 2:
                print('The list must have at least 2 elements to be sorted.')
                return []
            start = time.time()
            result = func(*args, **kwargs)
            stop = time.time()
            print(f'Time "{func.__name__}": \t{(stop - start) * 1000} ms')
            return result
        return wrapper

    @check_args_and_timing
    def bubble_sort(self, ul: list) -> list:
        ''' O[nˆ2] '''
        ulen = len(ul)
        for i in range(ulen):
            for j in range(ulen - i - 1):
                if ul[j] > ul[j+1]:
                    tmp = ul[j+1]
                    ul[j+1] = ul[j]
                    ul[j] = tmp
        return ul

    @check_args_and_timing
    def selection_sort(self, ul: list) -> list:
        ''' O[nˆ2] '''
        ulen = len(ul)
        for i in range(ulen):
            min_idx = i
            for j in range(i, ulen - 1):
                if ul[j+1] < ul[min_idx]:
                    min_idx = j+1
            tmp = ul[i]
            ul[i] = ul[min_idx]
            ul[min_idx] = tmp
        return ul

    @check_args_and_timing
    def insertion_sort(self, ul: list) -> list:
        ''' O[nˆ2] '''
        ulen = len(ul)
        for i in range(1, ulen):
            j = i
            while j > 0 and ul[j] < ul[j-1]:
                tmp = ul[j]
                ul[j] = ul[j-1]
                ul[j-1] = tmp
                j -= 1
        return ul

    #@check_args_and_timing
    def merge_sort(self, ul: list) -> list:
        ''' O[n.log(n)] '''
        ulen = len(ul)
        if ulen > 1:
            # divide
            right_l = ul[ulen//2:]
            left_l = ul[:ulen//2]
            # recursive
            self.merge_sort(left_l)
            self.merge_sort(right_l)
            # merge
            l_idx, r_idx, m_idx = 0, 0, 0
            while l_idx < len(left_l) and r_idx < len(right_l):
                if left_l[l_idx] < right_l[r_idx]:
                    ul[m_idx] = left_l[l_idx]
                    l_idx += 1
                else:
                    ul[m_idx] = right_l[r_idx]
                    r_idx += 1
                m_idx += 1
            while l_idx < len(left_l):
                ul[m_idx] = left_l[l_idx]
                l_idx += 1
                m_idx += 1
            while r_idx < len(right_l):
                ul[m_idx] = right_l[r_idx]
                r_idx += 1
                m_idx += 1
            return ul

            
unsorted_list = [4, 6, 2, 9, 1, 11, 0, 3, 5, 8, 2, 5, 19]
print(unsorted_list)
sort = SortingAlgoritms()
#sort.bubble_sort(unsorted_list.copy())
#sort.selection_sort(unsorted_list.copy())
#sorted_list = sort.insertion_sort(unsorted_list.copy())
sorted_list = sort.merge_sort(unsorted_list.copy())
print(sorted_list)
