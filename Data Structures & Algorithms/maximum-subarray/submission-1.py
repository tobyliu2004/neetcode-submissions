class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curMax = 0
        resMax = float("-inf")
        for i in range(len(nums)):
            curMax += nums[i]
            resMax = max(resMax, curMax)
            if curMax < 0:
                curMax = 0
            
        return resMax
