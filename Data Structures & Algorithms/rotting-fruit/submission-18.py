class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r,c])
        time = 0
        while q:
            qLen = len(q)
            for i in range(qLen):
                row,col = q.popleft()
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1:
                        grid[r][c] = 2
                        q.append([r,c])
            if q:
                time += 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return time