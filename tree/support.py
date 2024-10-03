from tree import BinaryTree, Node

# Leitura em percurso de ordem simétrica
#
#      '+'
#    /     \
#  'a'      '*'
#          /   \
#        'b'    '-'
#              /    \
#            '/'    'e' 
#           /   \
#         'c'   'd'
#
# (a + (b * ((c/d) - e)))

def inorder_example_tree() -> BinaryTree:
    tree = BinaryTree()
    n1 = Node('a')
    n2 = Node('+')
    n3 = Node('*')
    n4 = Node('b')
    n5 = Node('-')
    n6 = Node('/')
    n7 = Node('c')
    n8 = Node('d')
    n9 = Node('e')

    n6.left = n7
    n6.right = n8
    n5.left = n6
    n5.right = n9
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3
    
    tree.root = n2
    return tree


# Leitura em percurso em Pós-Ordem
#
#           '3'
#         /     \
#       'E'      '5'
#       / \      /
#     'I' 'R'   'A' 
#         / \     \
#       'N' 'C'   'V' 
#             \  
#             'S'  
#
# INSCREVA53

def postorder_example_tree():
    tree = BinaryTree()
    n1 = Node('I')
    n2 = Node('N')
    n3 = Node('S')
    n4 = Node('C')
    n5 = Node('R')
    n6 = Node('E')
    n7 = Node('V')
    n8 = Node('A')
    n9 = Node('-')
    n10 = Node('5')
    n0 = Node('3')

    n0.left = n6
    n0.right = n10
    n6.left = n1
    n6.right = n5
    n5.left = n2
    n5.right = n4
    n4.right = n3
    n10.left = n8
    n10.right = n9
    n8.right = n7

    tree.root = n0
    return tree

if __name__ == "__main__":
    tree1 = inorder_example_tree()
    print("InOrder Transversal: ", end='')
    tree1.inorder_traversal()
    print(f" ->  Altura = {tree1.height()}")
    tree2 = postorder_example_tree()
    print("PostOrder Transversal: ", end='')
    tree2.postorder_traversal()
    print(f" -> Altura = {tree2.height()}")