class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rows
        for i in board:
            repeats = defaultdict(int)
            for j in i:
                repeats[j] += 1
            for m in repeats:
                if repeats[m] > 1 and m != ".":
                    return False
        #columns
        for j in range(9):
            repeats = defaultdict(int)
            for i in board:
                repeats[i[j]] += 1
            for m in repeats:
                if repeats[m] > 1 and m != ".":
                    return False
        #boxes
        boxes = defaultdict(lambda: defaultdict(int)) 
        for i in range(9):
            for j in range(9):
                row = i//3
                col = j//3
                boxes[(row,col)][board[i][j]] += 1
        for m in boxes:
            for n in boxes[m]:
                if boxes[m][n] > 1 and n != ".":
                    return False
        return True