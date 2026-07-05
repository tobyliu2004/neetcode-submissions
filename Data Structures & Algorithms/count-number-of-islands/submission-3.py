class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        islands = 0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        def bfs(r,c):
            q = collections.deque()
            q.append([r,c])
            visited.add((r,c))
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0,1], [0,-1]]
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in visited:
                        q.append([r,c])
                        visited.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1
        return islands