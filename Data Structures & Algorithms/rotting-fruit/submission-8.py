class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r,c])
        def addRot(r,c):
            if r in range(rows) and c in range(cols) and grid[r][c] == 1:
                q.append([r,c])
                grid[r][c] = 2
        
        time = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                addRot(r+1,c)
                addRot(r-1,c)
                addRot(r,c+1)
                addRot(r,c-1)
            if q:
                time += 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1     
        return time