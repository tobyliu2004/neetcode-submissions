class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sdict = defaultdict(int)
        tdict = defaultdict(int)

        for i in range(len(s)):
            sdict[s[i]] += 1
            tdict[t[i]] += 1
        return sdict == tdict