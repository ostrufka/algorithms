"""
Problem: Given the root of a binary tree, return its maximum depth.

Example:

    3
   / \
  9  20
    /  \
   15   7

Max depth = 3

Análise: 
-> Tempo:  O(n)
-> Espaço: O(n)
"""

import doctest

ROOT = 'ROOT'

class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, value: int) -> None:
        self.root = Node(value)
        

    def height(self, node=ROOT) -> int:
        if node == 'ROOT':
            node = self.root
        h = h_left = h_right = 0
        if node.left:
            h_left = self.height(node.left)
        if node.right:
            h_right = self.height(node.right)
        h = h_left if h_left > h_right else h_right
        return h + 1
        
    

if __name__ == '__main__':
    # doctest.testmod()
    tree = BinaryTree(3)
    tree.root.left = Node(9)
    tree.root.right = Node(20)
    tree.root.right.left = Node(15)
    tree.root.right.right = Node(7)
    tree.root.right.right.left = Node(1)
    tree.root.left.right = Node(3)
    print(tree.height())

