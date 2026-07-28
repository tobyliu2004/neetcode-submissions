class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        res = [intervals[0]]
        for start, end in intervals[1:]:
            tempS, tempE = res.pop()
            if tempE>=start:
                res.append([min(tempS, start), max(tempE, end)])
                continue
            res.append([tempS, tempE])
            res.append([start, end])
        return res