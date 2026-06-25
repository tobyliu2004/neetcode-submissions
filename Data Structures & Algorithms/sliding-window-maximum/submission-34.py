class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = collections.deque()
        l = 0
        res = []
        for r in range(len(nums)):
            while d and nums[r] > nums[d[-1]]:
                d.pop()
            d.append(r)
            if r >= k-1:
                res.append(nums[d[0]])
                if d[0] < l+1:
                    d.popleft()
                l += 1
        return res