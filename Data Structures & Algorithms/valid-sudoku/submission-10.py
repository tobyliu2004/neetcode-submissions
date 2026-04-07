class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    row = ("row", i, board[i][j])
                    col = ("col", j, board[i][j])
                    box = ("box", i//3, j//3, board[i][j])
                    if row in seen or col in seen or box in seen:
                        return False
                    else:
                        seen.add(row)
                        seen.add(col)
                        seen.add(box)
        return True