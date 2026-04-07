class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        r = 0
        track = defaultdict(int)
        while r < len(s):
            track[s[r]] += 1
            while (r-l+1) - max(track.values()) > k:
                track[s[l]] -= 1
                if track[s[l]] == 0:
                    del track[s[l]]
                l += 1
            res = max(res, r-l+1)
            r += 1
        return res