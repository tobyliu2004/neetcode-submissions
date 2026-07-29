class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        seen = set()

        def bfs(r,c):
            if (r,c) not in seen and r in range(rows) and c in range(cols) and grid[r][c] == "1":
                seen.add((r,c))
                bfs(r+1,c)
                bfs(r-1,c)
                bfs(r,c+1)
                bfs(r,c-1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in seen:
                    bfs(r,c)
                    islands += 1
        return islands