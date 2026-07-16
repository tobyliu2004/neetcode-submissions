class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        visit = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))

        def addRooms(r,c):
            if r in range(rows) and c in range(cols) and grid[r][c] != -1 and (r,c) not in visit:
                visit.add((r,c))
                q.append([r,c])
        
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                addRooms(r+1,c)
                addRooms(r-1,c)
                addRooms(r,c+1)
                addRooms(r,c-1)
            dist += 1