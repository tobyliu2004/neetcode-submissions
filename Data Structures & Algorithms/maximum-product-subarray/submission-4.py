class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = 1
        curMin = 1
        res = max(nums)
        for n in nums:
            temp = curMax * n
            curMax = max(curMax*n, curMin*n, n)
            curMin = min(temp, curMin*n, n)
            res = max(res, curMax)
        return res