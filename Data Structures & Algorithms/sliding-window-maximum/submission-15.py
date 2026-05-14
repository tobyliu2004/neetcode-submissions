class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        res = []
        for r in range(len(nums)):
            while d and d[0]<r-k+1:
                d.popleft()
            while d and nums[d[-1]] < nums[r]:
                d.pop()
            d.append(r)
            if r < k-1:
                continue
            res.append(nums[d[0]])
        return res