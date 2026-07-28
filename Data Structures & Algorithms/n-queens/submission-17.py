class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        posDiag = set()
        negDiag = set()
        cols = set()
        res = []
        board = [["."]*n for i in range(n)]

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
                board[r][c] = "."
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                cols.remove(c)
        dfs(0)
        return res