from collections import deque

class Queue:
    def __init__(self):
        self.__queue = deque()
        self.__size = 0

    def __len__(self):
        return self.__size

    def __iter__(self):
        try:
            while not self.is_empty():
                yield self.dequeue()
        except EmptyQueueError:
            pass

    def is_empty(self):
        return self.__size == 0

    def first(self):
        try:
            return self.__queue[0]
        except IndexError as e:
            raise EmptyQueueError('Empty queue!') from e

    def enqueue(self, element):
        self.__queue.append(element)
        self.__size += 1

    def dequeue(self):
        try:
            dequeued_element = self.__queue.popleft()
            self.__size -= 1
            return dequeued_element
        except IndexError as e:
            raise EmptyQueueError('Empty queue!') from e

class EmptyQueueError(Exception):
    pass


######### Unit Tests #########

import unittest

class TestQueue(unittest.TestCase):
    def test_empty_queue(self):
        queue = Queue()
        self.assertTrue(queue.is_empty())
        self.assertEqual(0, len(queue))
        with self.assertRaises(EmptyQueueError):
            queue.first()

    def test_enqueue_one_element(self):
        queue = Queue()
        queue.enqueue('A')
        self.assertFalse(queue.is_empty())
        self.assertEqual('A', queue.first())

    def test_enqueue_two_element(self):
        queue = Queue()
        queue.enqueue('A')
        queue.enqueue('B')
        self.assertFalse(queue.is_empty())
        self.assertEqual('A', queue.first())

    def test_dequeue_empty_queue(self):
        queue = Queue()
        with self.assertRaises(EmptyQueueError):
            queue.dequeue()

    def test_dequeue(self):
        queue = Queue()
        letters = 'ABCDE'
        for letter in letters:
            queue.enqueue(letter)
        for letter in letters:
            letter_dequeued = queue.dequeue()
            self.assertEqual(letter, letter_dequeued)

    def test_size(self):
        queue = Queue()
        letters = 'ABCDE'
        for size, letter in enumerate(letters, start=1):
            queue.enqueue(letter)
            self.assertEqual(size, len(queue))

    def test_iterate(self):
        queue = Queue()
        letters = 'ABCDE'
        for letter in letters:
            queue.enqueue(letter)
        for letter, letter_dequeued in zip(letters, queue):
            self.assertEqual(letter, letter_dequeued)
        self.assertTrue(queue.is_empty())

if __name__ == '__main__':
    unittest.main()