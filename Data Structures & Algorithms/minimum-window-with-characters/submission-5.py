class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(s) < len(t):
            return ""
        target = defaultdict(int)
        for i in t:
            target[i] += 1
        have = 0
        need = len(target)
        window = {}
        l = 0
        res = [-1, -1]
        resLen = float("infinity")

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in target and window[c] == target[c]:
                have += 1
            while need == have:
                if (r-l+1) < resLen:
                    resLen = r-l+1
                    res = [l, r]
                window[s[l]] -= 1
                if s[l] in target and window[s[l]] < target[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""
                    