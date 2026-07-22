class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges)+1)

        def find(n1):
            if n1 != par[n1]:
                par[n1] = find(par[n1])
            return par[n1]
        def union(n1,n2):
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
        
        for n1, n2 in edges:
            if union(n1,n2) == 0:
                return [n1,n2]
        
        