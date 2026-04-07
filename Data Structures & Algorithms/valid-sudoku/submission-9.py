class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != ".":
                    if (board[i][j], "row", i) in seen or (board[i][j], "col", j) in seen or (board[i][j], i//3, j//3) in seen:
                        return False
                    else:
                        seen.add((board[i][j], "row", i))
                        seen.add((board[i][j], "col", j))
                        seen.add((board[i][j], i//3, j//3))

        return True