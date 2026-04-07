class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l = 0
        r = len(s1) - 1
        first = defaultdict(int)
        for i in s1:
            first[i] += 1
        second = defaultdict(int)
        for i in range(len(s1)):
            second[s2[i]] += 1
        while r < len(s2):
            if first == second:
                return True
            second[s2[l]] -= 1
            if second[s2[l]] == 0:
                del second[s2[l]]
            l += 1
            r += 1
            if r < len(s2):
                second[s2[r]] += 1
        return False