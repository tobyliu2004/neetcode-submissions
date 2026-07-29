class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        latest = {}
        for i, c in enumerate(s):
            latest[c] = i
        end, size = 0,0
        res = []
        for i, c in enumerate(s):
            size += 1
            end = max(end, latest[c])
            if end == i:
                res.append(size)
                size = 0
        return res