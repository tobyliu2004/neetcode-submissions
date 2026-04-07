class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = max_freq = 0
        count = {}
        for R in range(len(s)):
            count[s[R]] = count.get(s[R], 0) + 1
            max_freq = max(max_freq, count[s[R]])
            if R - L + 1 - max_freq > k:
                count[s[L]] -= 1
                L += 1
        return R-L+1