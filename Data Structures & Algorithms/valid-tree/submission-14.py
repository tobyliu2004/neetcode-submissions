class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = [[] for i in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = {0}
        q = deque([0])
        while q:
            node = q.popleft()
            for nei in adj[node]:
                if nei not in visit:
                    visit.add(nei)
                    q.append(nei)

        return len(visit) == n