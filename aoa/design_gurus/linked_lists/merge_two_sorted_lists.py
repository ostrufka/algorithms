"""
Problem: Merge two sorted linked lists into one sorted list.

Example:

List 1: 1->2->4
List 2: 1->3->4
Merged: 1->1->2->3->4->4

Análise: 
-> Tempo:  O(m+n)
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

def merge_linked_lists(list1: Node, list2: Node) -> Node:   
    merged_list_original = Node(0)
    merged_list = merged_list_original

    while list1 and list2:
        if list1.value < list2.value:
            merged_list.next = list1
            list1 = list1.next
        else:
            merged_list.next = list2
            list2 = list2.next

        merged_list = merged_list.next

    if list1:
        merged_list.next = list1
    elif list2:
        merged_list.next = list2

    return merged_list_original.next
    

if __name__ == '__main__':
    # doctest.testmod()
    linked_list1 = LinkedList(1)
    linked_list1.root.next = Node(2)
    linked_list1.root.next.next = Node(4)
    linked_list2 = LinkedList(1)
    linked_list2.root.next = Node(3)
    linked_list2.root.next.next = Node(4)

    merged_list = merge_linked_lists(linked_list1.root, linked_list2.root)

    print(f"{linked_list1.root.value} -> ", end=' ')
    print(f"{linked_list1.root.next.value} -> ", end=' ')
    print(f"{linked_list1.root.next.next.value} -> ", end=' ')
    print(f"{linked_list1.root.next.next.next}")

    print(f"{linked_list2.root.value} -> ", end=' ')
    print(f"{linked_list2.root.next.value} -> ", end=' ')
    print(f"{linked_list2.root.next.next.value} -> ", end=' ')
    print(f"{linked_list2.root.next.next.next}")

    print(f"{merged_list.value} -> ", end=' ')
    print(f"{merged_list.next.value} -> ", end=' ')
    print(f"{merged_list.next.next.value} -> ", end=' ')
    print(f"{merged_list.next.next.next.value} -> ", end=' ')
    print(f"{merged_list.next.next.next.next.value} -> ", end=' ')
    print(f"{merged_list.next.next.next.next.value} -> ", end=' ')
    print(f"{merged_list.next.next.next.next.next}")



    # linked_list.reverse()

    # print(f"{linked_list.root.value} -> ", end=' ')
    # print(f"{linked_list.root.next.value} -> ", end=' ')
    # print(f"{linked_list.root.next.next.value} -> ", end=' ')
    # print(f"{linked_list.root.next.next.next.value} -> ", end=' ')
    # print(f"{linked_list.root.next.next.next.next.value} -> ", end=' ')
    # print(f"{linked_list.root.next.next.next.next.next}")