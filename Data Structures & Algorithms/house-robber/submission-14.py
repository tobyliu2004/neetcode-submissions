class Solution:
    def rob(self, nums: List[int]) -> int:
        nums.append(0)
        one = nums[-2]
        two = nums[-1]
        for i in range(len(nums)-3, -1, -1):
            temp = one
            one = max(nums[i]+two, one)
            two = temp
        return one