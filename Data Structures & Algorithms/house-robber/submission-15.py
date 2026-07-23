class Solution:
    def rob(self, nums: List[int]) -> int:
        one = 0
        two = 0
        for i in range(len(nums)-1, -1, -1):
            temp = one
            one = max(nums[i]+two, one)
            two = temp
        return one