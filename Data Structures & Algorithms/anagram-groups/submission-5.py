class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        track = defaultdict(list)
        for i in strs:
            letters = [0] * 26
            for j in i:
                letters[ord(j)-ord("a")] += 1
            track[tuple(letters)].append(i)
        res = []
        for i, lists in track.items():
            res.append(lists)
        return res