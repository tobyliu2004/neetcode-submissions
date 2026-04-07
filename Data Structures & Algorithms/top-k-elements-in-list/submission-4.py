class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        track = defaultdict(int)
        for i in nums:
            track[i] += 1
        bucket = [[] for i in range(len(nums)+1)]
        for num, freq in track.items():
            bucket[freq].append(num)
        res = []
        for i in range(len(bucket)-1,-1,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res