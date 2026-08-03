class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        posDiag = set()
        negDiag = set()
        cols = set()
        board = [["."]*n for i in range(n)]
        res = []
        def dfs(r):
            if r == n:
                copy = ["".join(board[i]) for i in range(n)]
                res.append(copy)
                return
            for c in range(n):
                if c in cols or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                posDiag.add(r+c)
                negDiag.add(r-c)
                cols.add(c)
                board[r][c] = "Q"
                dfs(r+1)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                cols.remove(c)
                board[r][c] = "."
        dfs(0)
        return res