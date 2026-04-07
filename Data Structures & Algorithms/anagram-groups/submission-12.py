class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        comp = defaultdict(list)
        for i in strs:
            sorte = sorted(i)
            comp[tuple(sorte)].append(i)
        return list(comp.values()) 