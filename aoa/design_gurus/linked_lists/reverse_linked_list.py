"""
Problem: Given the head of a singly linked list, reverse the list, and return the reversed list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Análise: 
-> Tempo:  O(n)
-> Espaço: O(1)
"""

# import doctest

class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value: int) -> None:
        self.root = Node(value)

    def reverseList(head):
        prev = None
        current = head

        while current:
            nextNode = current.next
            current.next = prev  
            prev = current
            current = nextNode

        return prev

    def reverse(self, node: Node = None) -> bool:
        if node is None:
            node = self.root

        if node.next is None:
            self.root = node
            return node      
        
        node.next = self.reverse(node.next)

        if node.next.next is None:
            node.next.next = node
            node.next = None

        return node
    

if __name__ == '__main__':
    # doctest.testmod()
    linked_list = LinkedList(1)
    linked_list.root.next = Node(2)
    linked_list.root.next.next = Node(3)
    linked_list.root.next.next.next = Node(4)
    linked_list.root.next.next.next.next = Node(5)

    print(f"{linked_list.root.value} -> ", end=' ')
    print(f"{linked_list.root.next.value} -> ", end=' ')
    print(f"{linked_list.root.next.next.value} -> ", end=' ')
    print(f"{linked_list.root.next.next.next.value} -> ", end=' ')
    print(f"{linked_list.root.next.next.next.next.value} -> ", end=' ')
    print(f"{linked_list.root.next.next.next.next.next}")

    linked_list.reverse()

    print(f"{linked_list.root.value} -> ", end=' ')
    print(f"{linked_list.root.next.value} -> ", end=' ')
    print(f"{linked_list.root.next.next.value} -> ", end=' ')
    print(f"{linked_list.root.next.next.next.value} -> ", end=' ')
    print(f"{linked_list.root.next.next.next.next.value} -> ", end=' ')
    print(f"{linked_list.root.next.next.next.next.next}")