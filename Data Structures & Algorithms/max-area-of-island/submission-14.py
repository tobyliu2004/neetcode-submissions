class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        self.max_area = 0
        seen = set()
        def dfs(r,c):
            area = 1
            q = deque()
            q.append([r,c])
            seen.add((r,c))
            while q:
                row, col = q.pop()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    roww = row + dr
                    coll = col + dc
                    if (roww,coll) not in seen and roww in range(rows) and coll in range(cols) and grid[roww][coll] == 1:
                        area += 1
                        seen.add((roww,coll))
                        q.append([roww, coll])
                    
            self.max_area = max(self.max_area, area)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in seen:
                    dfs(r,c)
        return self.max_area