class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        target = sum(nums)//2
        seen = set()
        seen.add(0)
        for n in nums:
            temp = set()
            for j in seen:
                temp.add(j)
                temp.add(j+n)
            seen = temp
        return target in seen