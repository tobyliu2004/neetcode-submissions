class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        longest = 0
        char_count = defaultdict(int)
        maxf = 0

        for R in range(len(s)):
            char_count[s[R]] += 1
            maxf = max(maxf, char_count[s[R]])
            while (R-L+1)-maxf > k:
                char_count[s[L]] -= 1
                L += 1
            longest = max(longest, R-L+1)
            
        return longest
                