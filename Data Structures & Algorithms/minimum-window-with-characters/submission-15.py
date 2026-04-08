class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        t_count = defaultdict(int)
        window = defaultdict(int)
        shortest = [float('inf'), float('inf'), float('inf')]
        for i in range(len(t)):
            t_count[t[i]] += 1
        goal = len(t_count)
        l = 0
        track = 0
        for r in range(len(s)):
            window[s[r]] += 1
            if s[r] in t_count:
                if window[s[r]] == t_count[s[r]]:
                    track += 1
            while track == goal:
                if r-l+1 < shortest[0]:
                    shortest = [r-l+1, l, r]
                window[s[l]] -= 1
                if s[l] in t_count:
                    if window[s[l]] < t_count[s[l]]:
                        track -= 1
                if window[s[l]] == 0:
                    del(window[s[l]])
                l += 1
        return s[shortest[1]:shortest[2]+1] if shortest[0] < float('inf') else ""