class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        visit = set()

        def dfs(r,c):
            q = deque()
            q.append([r,c])
            visit.add((r,c))
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            cur = 1
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if row in range(rows) and col in range(cols) and grid[row][col] == 1 and (row, col) not in visit:
                        q.append([row,col])
                        visit.add((row,col))
                        cur += 1
            return cur

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit and grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
        return max_area