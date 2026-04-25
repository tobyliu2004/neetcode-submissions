class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        t_dict = defaultdict(int)
        s_dict = defaultdict(int)
        track = 0
        res_len = float('inf')
        res = [0,0]
        for i in range(len(t)):
            t_dict[t[i]] += 1
        need = len(t_dict)
        l = 0
        for r in range(len(s)):
            s_dict[s[r]] += 1
            if s_dict[s[r]] == t_dict[s[r]]:
                track += 1
            while track == need:
                if r-l+1 < res_len:
                    res_len = r-l+1
                    res = [l, r]
                s_dict[s[l]] -= 1
                if s_dict[s[l]] == t_dict[s[l]]-1:
                    track -= 1
                if s_dict[s[l]] == 0:
                    del(s_dict[s[l]])
                l += 1
        if res_len == float('inf'):
            return ""
        return s[res[0]:res[1]+1]