class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        max_area = 0

        def dfs(r,c):
            q = deque()
            q.append([r,c])
            visit.add((r,c))
            cur = 1
            while q:
                r,c = q.popleft()
                directions = [[0,1], [0,-1], [1,0], [-1,0]]
                for dr, dc in directions:
                    row = r+dr
                    col = c+dc
                    if row in range(rows) and col in range(cols) and grid[row][col] == 1 and (row,col) not in visit:
                        q.append([row,col])
                        visit.add((row,col))
                        cur += 1
            return cur
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    max_area = max(max_area, dfs(r,c))
        return max_area