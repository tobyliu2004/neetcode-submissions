class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        track = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for i in s:
                count[ord(i)-ord("a")] += 1
            track[tuple(count)].append(s)
        return list(track.values())