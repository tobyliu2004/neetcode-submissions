class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        l = 0
        res = []
        for r in range(len(nums)):
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)
            if r >= k-1:
                res.append(nums[dq[0]])
                l += 1
                if dq[0] < l:
                    dq.popleft()
        return res