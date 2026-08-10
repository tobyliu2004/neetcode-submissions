class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges)+1)
        def find(n1):
            if par[n1] != n1:
                par[n1] = find(par[n1])
            return par[n1]
        
        def union(l1,l2):
            n1, n2 = find(l1), find(l2)
            if n1 != n2:
                if rank[n1]>rank[n2]:
                    par[n2] = n1
                    rank[n1] += rank[n2]
                    return -1
                else:
                    par[n1] = n2
                    rank[n2] += rank[n1]
                    return -1
            return 0
        
        for n1, n2 in edges:
            if union(n1, n2) == 0:
                return [n1,n2]
            