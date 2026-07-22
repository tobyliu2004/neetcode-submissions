class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) %2 == 1:
            return False
        target = sum(nums)//2
        visit = set()
        visit.add(0)
        for i in range(len(nums)):
            temp = set()
            for t in visit:
                temp.add(t)
                temp.add(t+nums[i])
            visit = temp
        return True if target in visit else False