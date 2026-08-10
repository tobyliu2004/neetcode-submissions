class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        adj = [[] for i in range(n)]
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visit = set()
        visit.add(0)
        q = deque([0])
        while q:
            node = q.popleft()
            for nei in adj[node]:
                if nei not in visit:
                    visit.add(nei)
                    q.append(nei)
        return len(visit) == n