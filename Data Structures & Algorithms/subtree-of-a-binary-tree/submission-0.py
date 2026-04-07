# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If main tree is empty, can't contain subtree
        if not root:
            return False
        
        # Check if trees match starting at current node
        if self.isSameTree(root, subRoot):
            return True
        
        # If not, check left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both empty
        if not p and not q:
            return True
        
        # One empty, one not
        if not p or not q:
            return False
        
        # Values different
        if p.val != q.val:
            return False
        
        # Check both subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)