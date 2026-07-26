class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        res = float("-inf")
        for n in nums:
            curSum += n
            res = max(res, curSum)
            if curSum < 0:
                curSum = 0
        return res