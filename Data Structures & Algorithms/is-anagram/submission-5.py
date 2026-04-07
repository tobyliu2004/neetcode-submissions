class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        for i in s:
            s_dict[i] += 1
        t_dict = defaultdict(int)
        for i in t:
            t_dict[i] += 1
        return t_dict == s_dict