class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for i in nums:
            counts[i] += 1
        buckets = [[] for i in range(len(nums)+1)]
        for n, count in counts.items():
            buckets[count].append(n)
        res = []
        for i in range(len(buckets)-1,-1,-1):
            for j in buckets[i]:
                res.append(j)
                if (len(res) == k):
                    return res
        return