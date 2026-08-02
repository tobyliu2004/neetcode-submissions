class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        track = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            track[crs].append(pre)
        res = []
        visit = set()
        def dfs(crs):
            if crs in visit:
                return False
            if track[crs] == []:
                if crs not in res:
                    res.append(crs)
                return True
            visit.add(crs)
            for pre in track[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            track[crs] = []
            res.append(crs)
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res