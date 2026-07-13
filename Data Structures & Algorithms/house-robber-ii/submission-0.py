class Solution:
    def rob(self, nums: List[int]) -> int:
        one = self.helper(nums[1:])
        two = self.helper(nums[:-1])
        return max(nums[0], one, two)
    
    def helper(self, nums):
        rob1, rob2 = 0,0
        for n in nums:
            temp = max(n+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2