class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        res = [intervals[0]]
        for start, end in intervals[1:]:
            if res[-1][1] >= start:
                tempS, tempE = res.pop()
                res.append([min(start, tempS), max(tempE, end)])
                continue
            res.append([start, end])
        return res