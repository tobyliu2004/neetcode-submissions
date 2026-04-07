class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        perm = defaultdict(int)
        for i in range(len(s1)):
            perm[s1[i]] += 1
        temp = defaultdict(int)
        for r in range(len(s2)):
            temp[s2[r]] += 1
            while r-l+1 > len(s1):
                temp[s2[l]] -= 1
                if temp[s2[l]] == 0:
                    del temp[s2[l]]
                l += 1
            if temp == perm:
                return True
        return False