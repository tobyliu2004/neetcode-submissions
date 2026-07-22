class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1,1
        res = max(nums)
        for n in nums:
            tmp = curMax*n
            curMax = max(curMax*n, curMin*n, n)
            curMin = min(tmp, curMin*n, n)
            res = max(res, curMax)
        return res