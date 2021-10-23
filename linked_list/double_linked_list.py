
# Double linked list in python: from collections import deque

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __iter__(self):
        current_node = self
        while current_node is not None:
            yield current_node
            current_node = current_node.right

    def __reversed__(self):
        current_node = self
        while current_node is not None:
            yield current_node
            current_node = current_node.left

class DoubleLinkedList:
    '''
    Complexity:
      * Execution Time:
        - Index Access: O(idx)
        - Insertion: End -> O(1), Middle -> O(idx), Begin -> O(1)
        - Remove: End -> O(1), Middle -> O(idx), Begin -> O(1)
        - Iteration: O(n)
        - Size: O(1)
      * Memory: O(n)
    '''
    def __init__(self):
        self._first = None
        self._last = None
        self._size = 0

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        if self._first is None:
            raise IndexError(f'Empty List.')
        if index <= len(self)//2:
            for cur_index, cur_node in enumerate(self._first):
                if index == cur_index:
                    return cur_node.value
        else:
            for inverted_index, cur_node in enumerate(reversed(self._last)):
                if index == self._size - 1 - inverted_index:
                    return cur_node.value
        raise IndexError(f'Index {index} out of range.')

    def __iter__(self):
        for node in self._first:
            yield node.value

    def __reversed__(self):
        for node in self._last:
            yield node.value

    def add(self, value, index=None):
        node = Node(value)
        if self._first is None and self._last is None:
            self._first = self._last = node
        else:
            if index == 0: # add to begin - O(1)
                node.right = self._first # old first
                self._first.left = node
                self._first = node
            elif index is None: # add to end - O(1)
                node.left = self._last # old last
                self._last.right = node
                self._last = node
            else: # add to middle - O(index)
                for cur_index, cur_node in enumerate(self._first):
                    if index == cur_index:
                        node.left = cur_node.left
                        node.right = cur_node
                        cur_node.left = node
                        node.left.right = node
        self._size += 1

    def remove(self, index=None):
        if self._first is None:
            raise IndexError('List is already empty.')
        elif self._first is self._last:
            node = self._first
            self._first = self._last = None
        else:
            if index == 0: # remove from begin - O(1)
                node = self._first
                self._first.right.left = None
                self._first = self._first.right
            elif index is None: # remove from end - O(1)
                node = self._last
                self._last.left.right = None
                self._last = self._last.left
            else: # remove from middle - O(index)
                for cur_index, cur_node in enumerate(self._first):
                    if index == cur_index:
                        node = cur_node
                        cur_node.left.right = cur_node.right
                        cur_node.right.left = cur_node.left
        self._size -= 1
        return node



######### Unit Tests #########

import unittest

class TestDoubleLinkedListNode(unittest.TestCase):
    def test_create_node_with_different_objects(self):
        for object in (1, 'Andre', 1.1):
            with self.subTest(object):
                node = Node(object)
                self.assertEqual(object, node.value)
                self.assertIsNone(node.left)
                self.assertIsNone(node.right)

    def test_create_node_specifying_left(self):
        left = Node(1)
        node = Node(2, left)
        self.assertEqual(left, node.left)
        self.assertIsNone(node.right)
        new_node = Node(3, left=left)
        self.assertEqual(left, new_node.left)
        self.assertIsNone(new_node.right)

    def test_create_node_specifying_right(self):
        right = Node(1)
        node = Node(2, right=right)
        self.assertEqual(right, node.right)
        self.assertIsNone(node.left)

    def test_create_node_specifying_left_and_right(self):
        left = Node(1)
        right = Node(2)
        node = Node(3, left, right)
        self.assertEqual(left, node.left)
        self.assertEqual(right, node.right)


class TestDoubleLinkedList(unittest.TestCase):
    def test_create_list(self):
        double_linked_list = DoubleLinkedList()
        self.assertEqual(0, len(double_linked_list))
        self.assertIsNone(double_linked_list._first)
        self.assertIsNone(double_linked_list._last)

    def test_add_first_element(self):
        double_linked_list = DoubleLinkedList()
        double_linked_list.add(0)
        self.assertEqual(1, len(double_linked_list))
        first = double_linked_list._first
        self.assertEqual(0, first.value)
        self.assertEqual(first, double_linked_list._last)
        self.assertIsNone(first.left)
        self.assertIsNone(first.right)

    def test_add_second_element(self):
        double_linked_list = DoubleLinkedList()
        double_linked_list.add(0)
        double_linked_list.add(1)
        self.assertEqual(2, len(double_linked_list))
        first = double_linked_list._first
        self.assertEqual(0, first.value)
        last = double_linked_list._last
        self.assertEqual(1, last.value)
        self.assertEqual(first, last.left)
        self.assertEqual(last, first.right)
        self.assertIsNone(first.left)
        self.assertIsNone(last.right)

    def test_add_third_element(self):
        double_linked_list = DoubleLinkedList()
        double_linked_list.add(0)
        double_linked_list.add(1)
        double_linked_list.add(2)
        self.assertEqual(3, len(double_linked_list))
        first = double_linked_list._first
        self.assertEqual(0, first.value)
        last = double_linked_list._last
        second = first.right
        self.assertEqual(1, second.value)
        self.assertEqual(2, last.value)
        self.assertEqual(first, second.left)
        self.assertEqual(second, last.left)
        self.assertEqual(last, second.right)
        self.assertIsNone(first.left)
        self.assertIsNone(last.right)

    def test_add_second_element_from_left(self):
        double_linked_list = DoubleLinkedList()
        double_linked_list.add(0)
        double_linked_list.add(1, index=0)
        self.assertEqual(2, len(double_linked_list))
        first = double_linked_list._first
        self.assertEqual(1, first.value)
        last = double_linked_list._last
        self.assertEqual(0, last.value)
        self.assertEqual(first, last.left)
        self.assertEqual(last, first.right)
        self.assertIsNone(first.left)
        self.assertIsNone(last.right)

    def test_add_third_element_from_left(self):
        double_linked_list = DoubleLinkedList()
        double_linked_list.add(0)
        double_linked_list.add(1)
        double_linked_list.add(2, index=0)
        self.assertEqual(3, len(double_linked_list))
        first = double_linked_list._first
        self.assertEqual(2, first.value)
        last = double_linked_list._last
        second = first.right
        self.assertEqual(0, second.value)
        self.assertEqual(1, last.value)
        self.assertEqual(first, second.left)
        self.assertEqual(second, last.left)
        self.assertEqual(last, second.right)
        self.assertIsNone(first.left)
        self.assertIsNone(last.right)

    def test_add_element_in_middle_from_begin(self):
        double_linked_list = DoubleLinkedList()
        double_linked_list.add(0)
        double_linked_list.add(1)
        double_linked_list.add(2)
        double_linked_list.add(3)
        double_linked_list.add(4)
        double_linked_list.add(5, index=2)
        self.assertEqual(6, len(double_linked_list))
        first = double_linked_list._first
        self.assertEqual(0, first.value)
        last = double_linked_list._last
        self.assertEqual(5, double_linked_list[2])
        self.assertListEqual([0, 1, 5, 2, 3, 4], list(double_linked_list))

    def test_add_element_in_middle_from_end(self):
        double_linked_list = DoubleLinkedList()
        double_linked_list.add(0)
        double_linked_list.add(1)
        double_linked_list.add(2)
        double_linked_list.add(3)
        double_linked_list.add(4)
        double_linked_list.add(5, index=3)
        self.assertEqual(6, len(double_linked_list))
        first = double_linked_list._first
        self.assertEqual(0, first.value)
        last = double_linked_list._last
        self.assertEqual(5, double_linked_list[3])
        self.assertListEqual([0, 1, 2, 5, 3, 4], list(double_linked_list))

    def test_remove_empty_list(self):
        double_linked_list = DoubleLinkedList()
        with self.assertRaises(IndexError):
            double_linked_list.remove()

    def test_remove_element_from_left(self):
        double_linked_list = DoubleLinkedList()
        double_linked_list.add(0)
        double_linked_list.add(1)
        double_linked_list.add(2)
        double_linked_list.add(3)
        double_linked_list.remove(index=0)
        self.assertEqual(3, len(double_linked_list))
        first = double_linked_list._first
        self.assertEqual(1, first.value)
        last = double_linked_list._last
        second = first.right
        self.assertEqual(2, second.value)
        self.assertEqual(3, last.value)
        self.assertEqual(first, second.left)
        self.assertEqual(second, last.left)
        self.assertEqual(last, second.right)
        self.assertIsNone(first.left)
        self.assertIsNone(last.right)
        self.assertListEqual([1, 2, 3], list(double_linked_list))

    def test_remove_element_from_right(self):
        double_linked_list = DoubleLinkedList()
        double_linked_list.add(0)
        double_linked_list.add(1)
        double_linked_list.add(2)
        double_linked_list.add(3)
        double_linked_list.remove()
        self.assertEqual(3, len(double_linked_list))
        first = double_linked_list._first
        self.assertEqual(0, first.value)
        last = double_linked_list._last
        second = first.right
        self.assertEqual(1, second.value)
        self.assertEqual(2, last.value)
        self.assertEqual(first, second.left)
        self.assertEqual(second, last.left)
        self.assertEqual(last, second.right)
        self.assertIsNone(first.left)
        self.assertIsNone(last.right)
        self.assertListEqual([0, 1, 2], list(double_linked_list))

    def test_remove_element_from_middle(self):
        double_linked_list = DoubleLinkedList()
        double_linked_list.add(0)
        double_linked_list.add(1)
        double_linked_list.add(2)
        double_linked_list.add(3)
        double_linked_list.remove(index=1)
        self.assertEqual(3, len(double_linked_list))
        first = double_linked_list._first
        self.assertEqual(0, first.value)
        last = double_linked_list._last
        second = first.right
        self.assertEqual(2, second.value)
        self.assertEqual(3, last.value)
        self.assertEqual(first, second.left)
        self.assertEqual(second, last.left)
        self.assertEqual(last, second.right)
        self.assertIsNone(first.left)
        self.assertIsNone(last.right)
        self.assertListEqual([0, 2, 3], list(double_linked_list))


if __name__ == '__main__':
    unittest.main()