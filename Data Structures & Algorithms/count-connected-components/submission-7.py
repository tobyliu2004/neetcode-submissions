class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            if n1 != par[n1]:
                par[n1] = find(par[n1])
            return par[n1]

        def union(n1, n2):
            one, two = find(n1), find(n2)
            if one == two:
                return 0
            if rank[one] > rank[two]:
                par[two] = par[one]
                rank[one] += rank[two]
            else:
                par[one] = par[two]
                rank[two] += rank[one]
            return 1
        
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res