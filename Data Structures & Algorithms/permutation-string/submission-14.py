class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        comp = defaultdict(int)
        track = defaultdict(int)
        for i in range(len(s1)):
            comp[s1[i]] += 1
        for r in range(len(s2)):
            track[s2[r]] += 1
            if r-l+1>len(s1):
                track[s2[l]] -= 1
                if track[s2[l]] == 0:
                    del track[s2[l]]
                l += 1
            if comp == track:
                return True
            
        return False