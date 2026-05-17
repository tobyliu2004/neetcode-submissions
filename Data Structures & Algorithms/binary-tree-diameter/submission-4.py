# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]  # global max, use list so we can modify inside nested function
    
        def height(node):
            if not node:
                return 0
            
            left = height(node.left)
            right = height(node.right)
            
            res[0] = max(res[0], left + right)  # update diameter at this node
            
            return 1 + max(left, right)  # return height to parent
        
        height(root)
        return res[0]