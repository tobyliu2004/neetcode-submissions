class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        visit = set()
        def dfs(r,c):
            cur = 1
            q = deque()
            q.append([r,c])
            visit.add((r,c))
            while q:
                row, col = q.popleft()
                directions = [[0,1], [0,-1], [1,0], [-1,0]]
                for dr, dc in directions:
                    ro, co = row + dr, col + dc
                    if ro in range(rows) and co in range(cols) and (ro,co) not in visit and grid[ro][co] == 1:
                        cur += 1
                        q.append([ro,co])
                        visit.add((ro,co))
            return cur

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit and grid[r][c] == 1:
                    max_area = max(max_area, dfs(r,c))
        
        return max_area