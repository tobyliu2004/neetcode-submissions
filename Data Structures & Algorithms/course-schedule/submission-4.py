class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pres = {i:[] for i in range(numCourses)}
        visit = set()
        for crs, pre in prerequisites:
            pres[crs].append(pre)
        def dfs(crs):
            if crs in visit:
                return False
            if pres[crs] == []:
                return True
            visit.add(crs)
            for j in pres[crs]:
                if not dfs(j):
                    return False
            visit.remove(crs)
            pres[crs] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True