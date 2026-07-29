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
                row, col = q.popleft()
                directions = [[0,1], [0,-1], [1,0], [-1,0]]
                for dr, dc in directions:
                    ro = row + dr
                    co = col + dc
                    if ro in range(rows) and co in range(cols) and (ro,co) not in seen and grid[ro][co] == "1":
                        q.append([ro,co])
                        seen.add((ro,co))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in seen:
                    bfs(r,c)
                    islands += 1
        return islands