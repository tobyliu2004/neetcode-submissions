class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        count_t = {}
        count_s = {}
        for i in t:
            count_t[i] = count_t.get(i, 0) + 1
        need = len(count_t)
        have = 0
        shortest_len = float("infinity")
        shortest = [0,0]
        l = 0
        for r in range(len(s)):
            count_s[s[r]] = count_s.get(s[r], 0) + 1
            if s[r] in count_t and count_t[s[r]] == count_s[s[r]]:
                have += 1
            while have == need:
                if r-l+1 < shortest_len:
                    shortest_len = r-l+1
                    shortest = [l,r]
                count_s[s[l]] -= 1
                if s[l] in count_t and count_s[s[l]]<count_t[s[l]]:
                    have -= 1
                if count_s[s[l]] == 0:
                    del count_s[s[l]]
                l += 1
        return s[shortest[0]:shortest[1]+1] if shortest_len != float("infinity") else ""