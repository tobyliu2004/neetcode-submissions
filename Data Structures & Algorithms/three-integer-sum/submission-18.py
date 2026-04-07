class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-1):
            if i != 0 and nums[i]==nums[i-1]:
                continue
            cur = nums[i]
            l = i + 1
            r = len(nums)-1
            while l < r:
                if nums[r]+nums[l] == -cur:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif nums[r]+nums[l] < -cur:
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                else:
                    r -= 1
                    while nums[r] == nums[r+1] and l < r:
                        r -= 1
                
        return res
