class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            if par[n1] != n1:
                par[n1] = find(par[n1])
            return par[n1]

        def union(n1, n2):
            l1 = find(n1)
            l2 = find(n2)
            if l1 == l2:
                return 0
            if rank[l1] > rank[l2]:
                par[l2] = l1
                rank[l1] += rank[l2]
            else:
                par[l1] = l2
                rank[l2] += rank[l1]
            return -1
        for n1, n2 in edges:
            n += union(n1, n2)
        return n