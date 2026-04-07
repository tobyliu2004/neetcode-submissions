class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        track = defaultdict(int)
        for i in nums:
            track[i] += 1

        buckets = [[] for i in range(len(nums)+1)]
        for num, freq in track.items():
            buckets[freq].append(num)
        res = []
        for freq in range(len(buckets)-1,0,-1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res