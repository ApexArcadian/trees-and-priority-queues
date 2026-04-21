
from tree import Tree



class BinaryTree(Tree):
    """abstract class for binary tree structure"""
    
    #---additional abstract methods---#
    def left(self, p):
        """return a Position representing p's left child (or None if no left child)"""
        raise NotImplementedError('must be implemented by subclass')
    
    def right(self, p):
        """return a Position representing p's right child (or None if no right child)"""
        raise NotImplementedError('must be implemented by subclass')
    
#-- concrete methods implemented in this class --#
    def sibling(self, p):
        """return a Position representing p's sibling (or None if no sibling)"""
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)
    def children(self, p):
        """generate an iteration of Positions representing p's children"""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
            
    #-- binary tree constructor
    def __init__(self):
        """Creates an empty binary tree."""
        super().__init__()
        # Root is None (inherited from Tree)