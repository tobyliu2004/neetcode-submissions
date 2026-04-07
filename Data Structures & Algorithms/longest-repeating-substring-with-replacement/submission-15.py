class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        track = defaultdict(int)
        res = 0
        for r in range(len(s)):
            track[s[r]] += 1
            cur_max = max(track.values())
            if (r-l+1)-cur_max > k:
                track[s[l]] -= 1
                if track[s[l]] == 0:
                    del track[s[l]]
                l += 1
            res = max(res, r-l+1)
        return res
