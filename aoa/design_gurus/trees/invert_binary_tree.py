"""
Problem: Given the root of a binary tree, invert the tree, and return its root.

Example:

   4
  / \ 
 2   7 
/ \ / \
1 3 6  9

Inverted:
   4
  / \
 7   2
/ \ / \ 
9 6 3  1

Análise: 
-> Tempo:  O(n)
-> Espaço: O(n)
"""

ROOT = 'ROOT'

class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self, value: int) -> None:
        self.root = Node(value)

    def invertTree(self, root):
        if root is None:
            return
        
        right = self.invertTree(root.right) 
        left = self.invertTree(root.left)

        root.left = right
        root.right = left
        
        return root
    

if __name__ == '__main__':
    tree = BinaryTree(3)
    tree.root.left = Node(9)
    tree.root.right = Node(20)
    tree.root.right.left = Node(15)
    tree.root.right.right = Node(7)
    tree.root.right.right.left = Node(1)
    tree.root.left.right = Node(17)
    
    print("*----*")
    print(f'{tree.root.value}', end=' ')
    print(f'{tree.root.left.value}', end=' ')
    print(f'{tree.root.left.right.value}', end=' ')
    print(f'{tree.root.right.value}', end=' ')
    print(f'{tree.root.right.left.value}', end=' ')
    print(f'{tree.root.right.right.value}', end=' ')
    print(f'{tree.root.right.right.left.value}', end=' ')
    print("\n*----*")
    tree.invertTree(tree.root)
    print(f'{tree.root.value}', end=' ')
    print(f'{tree.root.left.value}', end=' ')
    print(f'{tree.root.left.left.value}', end=' ')
    print(f'{tree.root.left.left.right.value}', end=' ')
    print(f'{tree.root.left.right.value}', end=' ')
    print(f'{tree.root.right.value}', end=' ')
    print(f'{tree.root.right.left.value}', end=' ')
    print("\n*----*")

