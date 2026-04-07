class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        string_s = {}
        string_t = {}
        for i in range(len(s)):
            string_s[s[i]] = 1 + string_s.get(s[i], 0)
            string_t[t[i]] = 1 + string_t.get(t[i], 0)
        return string_s == string_t
