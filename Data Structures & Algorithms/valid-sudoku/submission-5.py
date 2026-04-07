class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                row_check = ('row', i, board[i][j])
                col_check = ('col', j, board[i][j])
                box_check = ('box', i//3, j//3, board[i][j])

                if row_check in seen or col_check in seen or box_check in seen:
                    return False
                
                seen.add(row_check)
                seen.add(col_check)
                seen.add(box_check)

        return True