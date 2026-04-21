from linked_binary_tree import LinkedBinaryTree
class ExpressionTree(LinkedBinaryTree):
    """An expression tree represents an arithmetic expression.
    Each internal node corresponds to an operator, and each leaf
    corresponds to an operand.
    """
    def __init__(self, token, left=None, right=None):
        super().__init__()
        if not isinstance(token, str):
            raise ValueError('Token must be a string')
        self._add_root(token)
        if left is not None:
            self._attach(self.root(), left, right)
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
            
    def evaluate(self):
        """Return the numeric result of the expression."""
        return self._evaluate_recur(self.root())
    def _evaluate_recur(self, p):
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