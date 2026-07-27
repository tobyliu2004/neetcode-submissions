class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        posDiag = set()
        negDiag = set()
        cols = set()
        res = []
        board = [["."]*n for i in range(n)]
        def dfs(r):
            for c in range(n):
                if r == n:
                    copy = ["".join(board[i]) for i in range(n)]
                    res.append(copy)
                    return
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