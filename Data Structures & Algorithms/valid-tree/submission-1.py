class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        track = {i:[] for i in range(n)}
        for n1, n2 in edges:
            track[n1].append(n2)
            track[n2].append(n1)
        visit = set()
        def dfs(cur, prev):
            if cur in visit:
                return False
            visit.add(cur)
            for j in track[cur]:
                if j == prev:
                    continue
                if dfs(j, cur) == False:
                    return False
            return True
        if dfs(0,-1) == False or len(visit) != n:
            return False
        return True