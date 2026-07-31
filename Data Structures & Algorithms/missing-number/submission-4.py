class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #res = len(nums)
        #for i in range(len(nums)):
        #    res += (i-nums[i])
        #return res

        xorr = len(nums)
        for i in range(len(nums)):
            xorr ^= i ^ nums[i]
        return xorr