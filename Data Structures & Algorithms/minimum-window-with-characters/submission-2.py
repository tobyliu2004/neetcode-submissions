class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""
        target = defaultdict(int)
        for i in t:
            target[i] += 1
        window = {}
        res, resLen = [-1, -1], float("infinity")
        l = 0
        have, need = 0, len(target)
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)
            if c in target and window[c] == target[c]:
                have += 1
            while have == need:
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = (r-l+1)
                window[s[l]] -= 1
                if s[l] in target and window[s[l]] < target[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""