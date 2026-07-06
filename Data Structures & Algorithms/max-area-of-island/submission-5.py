class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        max_area = 0
        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            cur = 1
            while q:
                row, col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for nr, nc in directions:
                    dr = row + nr
                    dc = col + nc
                    if dr in range(rows) and dc in range(cols) and (dr, dc) not in visited and grid[dr][dc] == 1:
                        q.append((dr,dc))
                        visited.add((dr,dc))
                        cur += 1
            return cur
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == 1:
                    max_area = max(max_area, bfs(r,c))
        return max_area