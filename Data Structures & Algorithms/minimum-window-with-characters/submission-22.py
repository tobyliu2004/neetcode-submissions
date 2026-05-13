class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""

        track_t = {}
        for i in t:
            track_t[i] = track_t.get(i, 0) + 1
        need = len(track_t)
        have = 0
        track_s = {}
        shortest = [0, 0]
        shortest_len = float("infinity")
        l = 0
        for r in range(len(s)):
            track_s[s[r]] = track_s.get(s[r], 0) + 1
            if s[r] in track_t and track_t[s[r]] == track_s[s[r]]:
                have += 1
            while have == need:
                if r-l+1 < shortest_len:
                    shortest_len = r-l+1
                    shortest = [l,r]
                track_s[s[l]] -= 1
                if s[l] in track_t and track_s[s[l]] < track_t[s[l]]:
                    have -= 1
                if track_s[s[l]] == 0:
                    del track_s[s[l]]
                l += 1
        return s[shortest[0]:shortest[1]+1] if shortest_len != float("inf") else ""
