class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        seen = set()

        def bfs(r,c):
            seen.add((r,c))
            q = deque()
            q.append([r,c])
            while q:
                ro, co = q.popleft()
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr, dc in directions:
                    row = ro + dr
                    col = co + dc
                    if (row,col) not in seen and row in range(rows) and col in range(cols) and grid[row][col] == "1":
                        seen.add((row,col))
                        q.append([row,col])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in seen:
                    bfs(r,c)
                    islands += 1
        return islands