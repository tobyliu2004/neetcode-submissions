class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = float("-inf")
        for n in nums:
            if curSum < 0:
                curSum = n
            else:
                curSum += n
            maxSum = max(maxSum, curSum)
        return maxSum