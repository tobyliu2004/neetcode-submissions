class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        visit = set()
        def dfs(r,c):
            if (r,c) not in visit and r in range(rows) and c in range(cols) and grid[r][c] == "1":
                visit.add((r,c))
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit and grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1
        return islands