class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic1 = defaultdict(int)
        for i in s1:
            dic1[i] += 1
        l = 0
        r = len(s1)-1
        while r < len(s2):
            dic2 = defaultdict(int)
            for i in range(l, r+1):
                dic2[s2[i]] += 1
            if dic1 == dic2:
                return True
            r += 1
            l += 1
        return False