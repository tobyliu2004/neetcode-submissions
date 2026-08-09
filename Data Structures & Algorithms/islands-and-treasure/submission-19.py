class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        inf = 2147483647
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
        while q:
            row, col = q.popleft()
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            for dr, dc in directions:
                r = row + dr
                c = col + dc
                if r in range(rows) and c in range(cols) and grid[r][c] == inf:
                    grid[r][c] = 1 + grid[row][col]
                    q.append([r,c])
            