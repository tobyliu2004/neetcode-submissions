class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        L = 0
        orig_count = defaultdict(int)
        for i in s1:
            orig_count[i] += 1
        count = defaultdict(int)
        for R in range(len(s2)):
            if R-L+1 > len(s1):
                count[s2[L]] -= 1
                if count[s2[L]] == 0:
                    del count[s2[L]]
                L += 1
            count[s2[R]] += 1
            if orig_count == count:
                return True
        return False
