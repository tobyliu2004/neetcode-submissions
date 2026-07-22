class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))
        def addRoom(r,c):
            if r in range(rows) and c in range(cols) and grid[r][c] != -1 and (r,c) not in visit:
                q.append([r,c])
                visit.add((r,c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                addRoom(r+1,c)
                addRoom(r-1,c)
                addRoom(r,c+1)
                addRoom(r,c-1)
            dist += 1