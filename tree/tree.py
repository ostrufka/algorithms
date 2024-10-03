'''
Binary Tree

  A
 _|_ 
|   |
B   C

Complexity: 
    * Execution time: O()
    * Memory: O()
'''

from queue_with_deque import Queue

ROOT = 'root'

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None

    def __str__(self) -> str:
        return str(self.data)
    
class BinaryTree:
    def __init__(self, data=None, node=None) -> None:
        if node:
            self.root = node
        elif data:
            node = Node(data)
        self.root = node

    # Altura (percurso em Pós-Ordem)
    def height(self, node=None):
        if node == ROOT:
            node = self.root
        h_left = h_right = 0
        if node.left:
            h_left = self.height(node.left)
        if node.right:
            h_right = self.height(node.right)
        return h_left + 1 if h_left > h_right else h_right + 1


    # percurso em ordem simétrica
    def inorder_traversal(self, node=ROOT):
        if node == ROOT:
            node = self.root
        if node.left:
            self.inorder_traversal(node.left)
        print(node, end=' ')
        if node.right:
            self.inorder_traversal(node.right)

    # percurso em pós ordem
    def postorder_traversal(self, node=ROOT):
        if node == ROOT:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node, end='')

    # percurso em nível
    def levelorder_traversal(self, node=ROOT):
        if node == ROOT:
            node = self.root
        queue = Queue()
        queue.enqueue(node)
        while len(queue):
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
            print(node, end=' ')


class BinarySearchTree(BinaryTree):
    def __init__(self, data=None) -> None:
        super().__init__(data)

    def insert(self, value: int) -> None:
        parent = None
        x = self.root
        while (x):
            parent = x
            if value < x.data:
                x = x.left
            else:
                x = x.right
        if parent is None:
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)

    def remove(self, value: int) -> None:
        pass
        
    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value: int, node):
        if node is None:
            return node
        if node.data == value:
            return BinarySearchTree(node)
        if value < node.data:
            return self._search(value, node.left)
        else:
            return self._search(value, node.right)
        

# Examples

if __name__ == "__main__":
    tree = BinaryTree(7)
    tree.root.left = Node(18)
    tree.root.right = Node(14)

    print(tree.root)
    print(tree.root.left)
    print(tree.root.right)
