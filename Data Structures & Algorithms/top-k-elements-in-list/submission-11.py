class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        track = defaultdict(int)
        for i in nums:
            track[i] += 1

        res = [[] for i in range(len(nums)+1)]
        for i in track:
            res[track[i]].append(i)

        final = []
        for i in range(len(res)-1,-1,-1):
            for j in range(len(res[i])-1,-1,-1):
                final.append(res[i][j])
                if len(final) == k:
                    return final