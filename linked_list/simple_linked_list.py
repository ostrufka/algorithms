
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __iter__(self):
        current_node = self
        while current_node is not None:
            yield current_node
            current_node = current_node.next

class SimpleLinkedList:
    '''
    Complexity:
      * Execution Time:
        - Index Access: O(n)
        - Insertion: End -> O(n), Middle -> O(idx), Begin -> O(1)
        - Remove: End -> O(n), Middle -> O(idx), Begin -> O(1)
        - Iteration: O(n)
        - Size: O(1)
      * Memory: O(n)
    '''
    def __init__(self):
        self._initial_node: Node = None
        self._size: int = 0

    def __len__(self):
        return self._size

    def __iter__(self):
        for node in self._initial_node:
            yield node.value

    def __getitem__(self, index):
        if self._initial_node is None:
            raise IndexError(f'Empty List.')
        for cur_index, cur_node in enumerate(self._initial_node):
            if index == cur_index:
                return cur_node.value
        raise IndexError(f'Index {index} out of range.')

    def __repr__(self):
        list = ''
        for node in self._initial_node:
            list += f'{node.value}, '
        return f'[{list[:-2]}]'


    def add(self, value, index=None):
        node = Node(value)
        if self._initial_node is None:
            self._initial_node = node
        else:
            if index == 0: # add to begin - O(1)
                node.next = self._initial_node
                self._initial_node = node
            elif index is None: # add to end - O(n)
                cur_node = self._initial_node
                while cur_node.next is not None:
                    cur_node = cur_node.next
                cur_node.next = node
            else: # add to middle - O(index) 
                for cur_index, cur_node in enumerate(self._initial_node, start=1):
                    if index == cur_index:
                        node.next = cur_node.next
                        cur_node.next = node
                        break
        self._size += 1

    def remove(self, index=None):
        if self._initial_node is None:
            raise IndexError('List is already empty.')
        if index == 0: # remove from begin - O(1)
            self._initial_node = self._initial_node.next
        elif index is None: # remove from end - O(n)
            node = self._initial_node
            while node.next is not None:
                last_node = node
                node = node.next
            last_node.next = None
        else:
            for cur_index, cur_node in enumerate(self._initial_node, start=1):
                if index == cur_index:
                    cur_node.next = cur_node.next.next
                    break
        self._size -= 1


    



######### Unit Tests #########

import unittest

class TestSimpleLinkedListNode(unittest.TestCase):
    def test_create_node_with_different_objects(self):
        for object in (1, 'Andre', 1.1):
            with self.subTest(object):
                node = Node(object)
                self.assertEqual(object, node.value)
                self.assertIsNone(node.next)

    def test_create_node_specifying_next(self):
        next = Node(2)
        node = Node(1, next=next)
        self.assertIs(next, node.next)

class TestSimpleLinkedList(unittest.TestCase):
    def test_create_list(self):
        simple_linked_list = SimpleLinkedList()
        self.assertEqual(0, len(simple_linked_list))
        self.assertIsNone(simple_linked_list._initial_node)

    def test_add_element_to_end_of_list(self):
        simple_linked_list = SimpleLinkedList()
        simple_linked_list.add(5)
        self.assertEqual(5, simple_linked_list._initial_node.value)
        self.assertIsNone(simple_linked_list._initial_node.next)
        self.assertEqual(5, simple_linked_list[0])
        self.assertEqual(1, len(simple_linked_list))
        self.assertListEqual([5], list(simple_linked_list))

    def test_add_element_to_begin_of_list(self):
        simple_linked_list = SimpleLinkedList()
        simple_linked_list.add(5)
        simple_linked_list.add(10)
        simple_linked_list.add(3, index=0)
        self.assertEqual(3, simple_linked_list[0])
        self.assertEqual(5, simple_linked_list[1])
        self.assertEqual(10, simple_linked_list[2])
        self.assertEqual(3, len(simple_linked_list))
        self.assertListEqual([3, 5, 10], list(simple_linked_list))

    def test_add_element_to_middle_of_list(self):
        simple_linked_list = SimpleLinkedList()
        simple_linked_list.add(5)
        simple_linked_list.add(10)
        simple_linked_list.add(7)
        simple_linked_list.add(3, index=2)
        self.assertEqual(5, simple_linked_list[0])
        self.assertEqual(10, simple_linked_list[1])
        self.assertEqual(3, simple_linked_list[2])
        self.assertEqual(7, simple_linked_list[3])
        self.assertEqual(4, len(simple_linked_list))
        self.assertListEqual([5, 10, 3, 7], list(simple_linked_list))

    def test_remove_element_to_end_of_list(self):
        simple_linked_list = SimpleLinkedList()
        simple_linked_list.add(5)
        simple_linked_list.add(10)
        simple_linked_list.add(7)
        simple_linked_list.add(11)
        simple_linked_list.remove()
        self.assertEqual(5, simple_linked_list[0])
        self.assertEqual(10, simple_linked_list[1])
        self.assertEqual(7, simple_linked_list[2])
        self.assertEqual(3, len(simple_linked_list))
        self.assertListEqual([5, 10, 7], list(simple_linked_list))

    def test_remove_element_to_begin_of_list(self):
        simple_linked_list = SimpleLinkedList()
        simple_linked_list.add(5)
        simple_linked_list.add(10)
        simple_linked_list.add(7)
        simple_linked_list.add(11)
        simple_linked_list.remove(index=0)
        self.assertEqual(10, simple_linked_list[0])
        self.assertEqual(7, simple_linked_list[1])
        self.assertEqual(11, simple_linked_list[2])
        self.assertEqual(3, len(simple_linked_list))
        self.assertListEqual([10, 7, 11], list(simple_linked_list))

    def test_remove_element_to_middle_of_list(self):
        simple_linked_list = SimpleLinkedList()
        simple_linked_list.add(5)
        simple_linked_list.add(10)
        simple_linked_list.add(7)
        simple_linked_list.add(11)
        simple_linked_list.remove(index=2)
        self.assertEqual(5, simple_linked_list[0])
        self.assertEqual(10, simple_linked_list[1])
        self.assertEqual(11, simple_linked_list[2])
        self.assertEqual(3, len(simple_linked_list))
        self.assertListEqual([5, 10, 11], list(simple_linked_list))

    def test_access_element_empty_list(self):
        simple_linked_list = SimpleLinkedList()
        with self.assertRaises(IndexError):
            simple_linked_list[0]

    def test_access_first_element(self):
        simple_linked_list = SimpleLinkedList()
        simple_linked_list.add(5)
        self.assertEqual(5, simple_linked_list._initial_node.value)
        self.assertEqual(5, simple_linked_list[0])

    def test_access_n_element(self):
        simple_linked_list = SimpleLinkedList()
        simple_linked_list.add(5)
        simple_linked_list.add(10)
        simple_linked_list.add(20)
        self.assertEqual(5, simple_linked_list[0])
        self.assertEqual(10, simple_linked_list[1])
        self.assertEqual(20, simple_linked_list[2])
        self.assertEqual(3, len(simple_linked_list))
        self.assertListEqual([5, 10, 20], list(simple_linked_list))
        with self.assertRaises(IndexError):
            simple_linked_list[3]


if __name__ == '__main__':
    unittest.main()