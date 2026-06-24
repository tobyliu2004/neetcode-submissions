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
            rightSide = None
            qLen = len(q)
            for i in range(qLen):
                curr = q.popleft()
                if curr:
                    rightSide = curr.val
                    q.append(curr.left)
                    q.append(curr.right)
            if rightSide:
                res.append(rightSide)
        return res