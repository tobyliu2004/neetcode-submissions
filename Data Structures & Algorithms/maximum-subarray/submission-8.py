class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = max(nums)
        cur = 0
        for i in nums:
            cur += i
            res = max(res, cur)
            if cur <= 0:
                cur = 0
        return res