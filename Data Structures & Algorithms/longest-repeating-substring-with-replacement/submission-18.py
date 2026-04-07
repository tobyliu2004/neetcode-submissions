class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        l = 0
        longest = 0
        for r in range(len(s)):
            window[s[r]] += 1
            max_val = max(window.values())
            while r-l+1-max_val > k:
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del(window[s[l]])
                l += 1
                max_val = max(window.values())
            longest = max(longest, r-l+1)
        return longest