class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 == 1:
            return False
        target = sum(nums)//2
        dp = set()
        dp.add(0)
        for i in range(len(nums)):
            temp = set()
            for t in dp:
                temp.add(t)
                temp.add(nums[i]+t)
            dp = temp
        return True if target in dp else False