class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l = 0
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)
        for i in s1:
            dict1[i] += 1
        for r in range(len(s2)):
            dict2[s2[r]] += 1
            if r-l+1 == len(s1):
                if dict1 == dict2:
                    return True
                dict2[s2[l]] -= 1
                if dict2[s2[l]] == 0:
                    del dict2[s2[l]]
                l += 1
        return False