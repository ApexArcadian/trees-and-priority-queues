from stack import Stack

class Node:
    def __init__(self, value=None, left=None, right=None, next=None):
        self.value = value
        self.left = left
        self.right = right
        self.next = next

class ExpressionTree:
    def inorder(self, x):
        if not x:
            return
        self.inorder(x.left)
        print(x.value, end=" ")
        self.inorder(x.right)

