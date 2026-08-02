class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        track = {i:[] for i in range(n)}
        for n1, n2 in edges:
            track[n1].append(n2)
            track[n2].append(n1)
        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False
            visit.add(i)
            for j in track[i]:
                if j == prev:
                    continue
                else:
                    if not dfs(j, i):
                        return False
            return True
        if dfs(0,-1)==False or len(visit)!=n:
            return False
        return True