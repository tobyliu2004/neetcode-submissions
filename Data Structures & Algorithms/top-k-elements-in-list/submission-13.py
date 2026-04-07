class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        buckets = [[] for i in range(len(nums)+1)] 
        for key, value in count.items():
            buckets[value].append(key)
        res = []
        for i in range(len(buckets)-1,-1,-1):
            for j in buckets[i]:
                if len(res) != k:
                    res.append(j)
        return res
