class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        visit = set()
        q = deque()
        visit.add(0)
        q.append(0)
        adj = [[] for i in range(n)]
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        while q:
            node = q.popleft()
            for nei in adj[node]:
                if nei not in visit:
                    visit.add(nei)
                    q.append(nei)
        return len(visit) == n