class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        res = 0
        start = 0
        for i, char in enumerate(s):
            if char in seen:
                start = max(start, seen[char]+1)
            seen[char] = i
            res = max(res, i - start + 1)
        return res