# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def height(curr):
            if not curr:
                return 0
            leftHeight = height(curr.left)
            rightHeight = height(curr.right)
            curr_diameter = leftHeight + rightHeight
            self.diameter = max(self.diameter, curr_diameter)
            return 1 + max(rightHeight, leftHeight)
        height(root)
        return self.diameter