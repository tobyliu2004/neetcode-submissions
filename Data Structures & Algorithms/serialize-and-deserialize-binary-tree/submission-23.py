# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(root):
            if not root:
                res.append("N")
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(res)

    # Decodes your encode data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        def dfs(val):
            if val[0] == "N":
                return None, val[1:]
            root = TreeNode(int(val[0]))
            root.left, val = dfs(val[1:])
            root.right, val = dfs(val)
            return root, val
        root, vals = dfs(vals)
        return root