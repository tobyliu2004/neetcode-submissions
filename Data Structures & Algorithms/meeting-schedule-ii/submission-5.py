"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [i.start for i in intervals]
        end = [i.end for i in intervals]
        start.sort()
        end.sort()
        start = deque(start)
        end = deque(end)
        res = 0
        count = 0
        while start:
            if start[0] < end[0]:
                count += 1
                start.popleft()
            else:
                count -= 1
                end.popleft()
            res = max(res, count)
        return res
