class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #hashmap
        #O(m*n) , m=number of strings, n=average length of each string
        res = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))  # "eat" → "aet", "tea" → "aet"
            res[sorted_s].append(s)
        return list(res.values())
