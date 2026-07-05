# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            qLen = len(q)
            rightSide = None
            for i in range(qLen):
                cur = q.popleft()
                if cur:
                    rightSide = cur.val
                    q.append(cur.left)
                    q.append(cur.right)
            if rightSide:
                res.append(rightSide)
        return res
