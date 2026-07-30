# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        def height(root):
            if not root:
                return 0
            left = max(height(root.left), 0)
            right = max(height(root.right), 0)
            self.res = max(self.res, left+right+root.val)
            return root.val + max(left, right)
        height(root)
        return self.res