class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r in [0,rows-1] or c in [0,cols-1]):
                    q.append([r,c])
        
        while q:
            qLen = len(q)
            for i in range(qLen):
                row, col = q.popleft()
                board[row][col] = "T"
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if r in range(rows) and c in range(cols) and board[r][c] == "O":
                        q.append([r,c])
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O"     