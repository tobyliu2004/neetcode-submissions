class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        comp = defaultdict(list)
        for i in strs:
            alpha = [0] * 26
            for j in i:
                alpha[ord(j)-ord("a")] += 2
            comp[tuple(alpha)].append(i)
        return list(comp.values()) 