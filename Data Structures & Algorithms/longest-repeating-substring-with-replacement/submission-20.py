class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        track = defaultdict(int)
        for r in range(len(s)):
            track[s[r]] += 1
            top = max(track.values())
            while r-l+1-top > k:
                track[s[l]] -= 1
                if track[s[l]] == 0:
                    del(track[s[l]])
                l += 1
            res = max(res, r-l+1)
        return res