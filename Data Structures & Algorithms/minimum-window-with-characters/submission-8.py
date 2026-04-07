class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        t_dict = defaultdict(int)
        for i in t:
            t_dict[i] += 1
        count = len(t_dict)
        l = 0
        s_dict = defaultdict(int)
        track = 0
        res = ""
        for r in range(len(s)):
            s_dict[s[r]] += 1
            if s_dict[s[r]] == t_dict[s[r]]:
                track += 1
            while track == count:
                if res == "" or ((r-l+1) < len(res)):
                    res = s[l:r+1]
                s_dict[s[l]] -= 1
                if s_dict[s[l]] < t_dict[s[l]]:
                    track -= 1
                l += 1
        return res