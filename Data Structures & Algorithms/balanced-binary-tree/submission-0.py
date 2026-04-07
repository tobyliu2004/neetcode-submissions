# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def height(node):
            if node is None:
                return 0
            
            # 1. Ask children for their heights
            left_height = height(node.left)
            right_height = height(node.right)
            
            # 2. Check if THIS node is balanced
            if abs(left_height - right_height) > 1:
                self.balanced = False
            
            # 3. Return height to parent
            return 1 + max(left_height, right_height)
        
        height(root)
        return self.balanced