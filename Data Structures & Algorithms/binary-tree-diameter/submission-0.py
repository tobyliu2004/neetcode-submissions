# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.diameter = 0
        def height(node):
            if node is None:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)
            
            # Update diameter at this node
            self.diameter = max(self.diameter, left_height + right_height)
            
            # Return height of this subtree
            return 1 + max(left_height, right_height)
        height(root)
        return self.diameter