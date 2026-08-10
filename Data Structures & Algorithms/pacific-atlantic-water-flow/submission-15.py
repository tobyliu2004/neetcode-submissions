class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        rows = len(heights)
        cols = len(heights[0])
        def dfs(r,c,ocean,prev):
            if r in range(rows) and c in range(cols) and heights[r][c] >= prev and (r,c) not in ocean:
                ocean.add((r,c))
                dfs(r+1,c,ocean,heights[r][c])
                dfs(r-1,c,ocean,heights[r][c])
                dfs(r,c+1,ocean,heights[r][c])
                dfs(r,c-1,ocean,heights[r][c])
        for r in range(rows):
            dfs(r, 0, pac, 0)
            dfs(r, cols-1, atl, 0)
        for c in range(cols):
            dfs(0, c, pac, 0)
            dfs(rows-1,c,atl,0)
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in atl and (r,c) in pac:
                    res.append([r,c])
        return res