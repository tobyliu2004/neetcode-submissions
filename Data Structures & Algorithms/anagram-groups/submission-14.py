class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        track = defaultdict(list)
        for i in strs:
            letters = [0] * 26
            for j in i:
                letters[ord(j)-ord("a")] += 1
            track[tuple(letters)].append(i)
        return list(track.values())