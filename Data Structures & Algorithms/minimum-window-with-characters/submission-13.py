class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        trackT = defaultdict(int)
        for i in t:
            trackT[i] += 1
        have = 0
        need = len(trackT)
        res = [-1,-1]
        reslen = float("infinity")
        window = defaultdict(int)
        l = 0
        for r in range(len(s)):
            window[s[r]] += 1
            if s[r] in trackT and trackT[s[r]] == window[s[r]]:
                have += 1
            while have == need:
                if r-l+1 < reslen:
                    reslen = r-l+1
                    res = [l,r]
                window[s[l]] -= 1
                if s[l] in trackT and window[s[l]]<trackT[s[l]]:
                    have -= 1          
                l += 1
        l, r = res
        return s[l:r+1] if reslen < float("infinity") else ""