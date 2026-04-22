
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
    
    # In BinaryTree class
    def preorder(self):
        """Generate positions in preorder traversal"""
        return self._preorder_subtree(self.root())

    def inorder(self):
        """Generate positions in inorder traversal"""
        return self._inorder_subtree(self.root())

    def postorder(self):
        """Generate positions in postorder traversal"""
        return self._postorder_subtree(self.root())


    # Helper methods for recursion
    def _preorder_subtree(self, p):
        yield p
        for c in self.children(p):
            yield from self._preorder_subtree(c)

    def _postorder_subtree(self, p):
        for c in self.children(p):
            yield from self._postorder_subtree(c)
        yield p

    def _inorder_subtree(self, p):
        if self.left(p) is not None:
            yield from self._inorder_subtree(self.left(p))
        yield p
        if self.right(p) is not None:
            yield from self._inorder_subtree(self.right(p))
        
            
    def positions(self, traversal='preorder'):
        """Generate an iteration of the tree's positions."""
        if traversal == 'preorder':
            return self.preorder()
        elif traversal == 'inorder':
            return self.inorder()
        elif traversal == 'postorder':
            return self.postorder()
        else:
            raise ValueError('traversal must be "preorder", "inorder", or "postorder"')

    def __iter__(self):
        """Generate an iteration of the tree's elements."""
        for p in self.positions():
            yield p.element()