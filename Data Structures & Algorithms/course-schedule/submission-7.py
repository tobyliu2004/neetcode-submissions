class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        track = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            track[crs].append(pre)
        visit = set()
        def dfs(crs):
            if crs in visit:
                return False
            if track[crs] == []:
                return True
            visit.add(crs)
            for j in track[crs]:
                if not dfs(j):
                    return False
            visit.remove(crs)
            track[crs] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True