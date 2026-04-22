from linked_binary_tree import LinkedBinaryTree

tree_visual = """
       8
      /  \
    3     10
   / \      \
  1   6      14
     / \     /
    4   7   13
"""

  

tree = LinkedBinaryTree()
# Construct the tree according to the visual representation
root = tree._Node(8)
tree._root = root
node3 = tree._Node(3, parent=root)
node10 = tree._Node(10, parent=root)
root._left = node3
root._right = node10
node1 = tree._Node(1, parent=node3)
node6 = tree._Node(6, parent=node3)
node3._left = node1
node3._right = node6
node4 = tree._Node(4, parent=node6)
node7 = tree._Node(7, parent=node6)
node6._left = node4
node6._right = node7
node14 = tree._Node(14, parent=node10)
node10._right = node14
node13 = tree._Node(13, parent=node14)
node14._left = node13

#this is hideous but it works

print("PREORDER:")
for node in tree.positions('preorder'):
    print(node.element())

print("INORDER:")
for node in tree.positions('inorder'):
    print(node.element())

print("POSTORDER:")
for node in tree.positions('postorder'):
    print(node.element())
