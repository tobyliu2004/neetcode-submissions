class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashish = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in hashish:
                hashish.remove(s[l])
                l += 1
            hashish.add(s[r])
            res = max(res, r-l+1)
        return res