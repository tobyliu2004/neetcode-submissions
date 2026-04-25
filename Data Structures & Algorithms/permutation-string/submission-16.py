class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        substring_dict = defaultdict(int)
        for i in range(len(s1)):
            substring_dict[s1[i]] += 1
        l = 0
        main_string_dict = defaultdict(int)
        for r in range(len(s2)):
            if r < len(s1)-1:
                main_string_dict[s2[r]] += 1
                continue
            main_string_dict[s2[r]] += 1
            if substring_dict == main_string_dict:
                return True
            main_string_dict[s2[l]] -= 1
            if main_string_dict[s2[l]] == 0:
                del(main_string_dict[s2[l]])
            l += 1
        return False