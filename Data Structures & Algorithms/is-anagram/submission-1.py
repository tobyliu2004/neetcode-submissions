class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        
        map_t = {}
        map_s = {}
        for i in range(len(s)):
            map_t[t[i]] = 1 + map_t.get(t[i], 0)
            map_s[s[i]] = 1 + map_s.get(s[i], 0)
        return map_t == map_s