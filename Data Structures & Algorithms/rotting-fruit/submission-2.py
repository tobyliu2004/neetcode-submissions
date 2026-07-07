class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh, time = 0, 0
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
        while q and fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()
                directions = [[0,1], [0,-1], [1,0], [-1,0]]
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if r <0 or r == rows or c<0 or c == cols or grid[r][c] != 1:
                        continue
                    fresh -= 1
                    grid[r][c] = 2
                    q.append([r,c])
            time += 1
        return time if fresh == 0 else -1