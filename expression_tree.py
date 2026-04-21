from linked_binary_tree import LinkedBinaryTree
from stack import Stack

class BinaryExpressionTree(LinkedBinaryTree):
    """An expression tree represents an arithmetic expression.
    Each internal node corresponds to an operator, and each leaf
    corresponds to an operand.
    """
    def __init__(self):
        """Creates an empty expression tree."""
        super().__init__()
        # Root is None (inherited from LinkedBinaryTree)
    
    def is_empty(self):
        """Return True if tree is empty, else False."""
        return len(self) == 0
    
    def clear_tree(self):
        """Clear the tree (remove all nodes)."""
        self._root = None
        self._size = 0
    
    def build_from_postfix(self, postfix):
        """
        Build expression tree from a postfix expression string.
        
        Pre: postfix is a valid whitespace-separated postfix expression
        Post: Builds an expression tree representing the postfix expression
        
        Raises:
            ValueError: If invalid token, too few operands, or extra operands
        """
        if not postfix or not postfix.strip():
            raise ValueError("Postfix expression cannot be empty")
        
        tokens = postfix.split()
        stack = Stack()
        operators = {'+', '-', '*', '/'}
        
        for token in tokens:
            if token not in operators:
                # It's an operand (number)
                # Create a single-node tree and push to stack
                operand_tree = BinaryExpressionTree()
                operand_tree.add_root(token)
                stack.push(operand_tree)
            else:
                # It's an operator
                if stack.is_empty():
                    raise ValueError(f"Invalid postfix expression: insufficient operands for operator '{token}'")
                
                right_tree = stack.pop()
                
                if stack.is_empty():
                    raise ValueError(f"Invalid postfix expression: insufficient operands for operator '{token}'")
                
                left_tree = stack.pop()
                
                # Create operator node and merge trees
                merged_tree = BinaryExpressionTree()
                merged_tree.add_root(token)
                merged_tree._attach(merged_tree.root(), left_tree, right_tree)
                stack.push(merged_tree)
        
        # Should have exactly one tree left
        if stack.is_empty():
            raise ValueError("Invalid postfix expression: no expression tree constructed")
        
        result_tree = stack.pop()
        
        if not stack.is_empty():
            raise ValueError("Invalid postfix expression: extra operands/operators left on stack")
        
        # Copy result_tree into self
        self._root = result_tree._root
        self._size = result_tree._size
    def __str__(self):
        pieces = []
        self._parenthesize_recur(self.root(), pieces)
        return ''.join(pieces)
    def _parenthesize_recur(self, p, result):
        if self.is_leaf(p):
            result.append(str(p.element()))
        else:
            result.append('(')
            self._parenthesize_recur(self.left(p), result)
            result.append(str(p.element()))
            self._parenthesize_recur(self.right(p), result)
            result.append(')')
            
    def _evaluate(self, p):
        if self.is_leaf(p):
            return float(p.element())
        else:
            op = p.element()
            left_val = self._evaluate_recur(self.left(p))
            right_val = self._evaluate_recur(self.right(p))
            if op == '+':
                return left_val + right_val
            elif op == '-':
                return left_val - right_val
            # i like this better than allowing x as multiplication
            #if i want to let algebreic expressions be evaluated, i can just use the * operator
            elif op == '*':
                return left_val * right_val
            elif op == '/':
                return left_val / right_val
            else:
                raise ValueError('Unknown operator: ' + str(op))
    