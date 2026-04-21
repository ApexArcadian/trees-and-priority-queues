#this needs to build the binary expression tree and evaluate it
from binary_expression_tree import Node, ExpressionTree
from stack import Stack
def main():
    s = "ABC*+D/"
    stack = Stack()
    tree = ExpressionTree()
    for c in s:
        if c in "+-*/^":
            z = Node(c)
            x = stack.pop()
            y = stack.pop()
            z.left = y
            z.right = x
            stack.push(z)
        else:
            stack.push(Node(c))
    print("The Inorder Traversal of Expression Tree: ", end="")
    tree.inorder(stack.pop())

if __name__ == "__main__":
    main()