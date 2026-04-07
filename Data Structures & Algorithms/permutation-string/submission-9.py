class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        first = defaultdict(int)
        for i in s1:
            first[i] += 1
        second = defaultdict(int)
        for i in range(len(s1)):
            second[s2[i]] += 1
        if first == second:
            return True
        l = 0
        for r in range(len(s1), len(s2)):
            second[s2[r]] += 1
            l_char = s2[r-len(s1)]
            second[l_char] -= 1
            if second[l_char] == 0:
                del second[l_char]
            if first == second:
                return True
        return False