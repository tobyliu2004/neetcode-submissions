# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append(root)
        res = []
        while q:
            right = None
            qLen = len(q)
            for i in range(qLen):
                cur = q.popleft()
                if cur:
                    right = cur.val
                    q.append(cur.left)
                    q.append(cur.right)
            if right:
                res.append(right)
        return res