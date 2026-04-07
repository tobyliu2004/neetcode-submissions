class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            #SKIP DUPLICATE LOGIC
            if i > 0 and nums[i] == nums[i-1]:
                continue # skips this loop iteration and goes to the next, skips duplicate
            target = -nums[i]
            L = i+1
            R = len(nums)-1
            while R > L:
                if nums[R] + nums[L] == target:
                    res.append([nums[i], nums[L], nums[R]])
                    #SKIP DUPLICATE LOGIC
                    while L < R and nums[L] == nums[L+1]:
                        L += 1
                    while L < R and nums[R] == nums[R-1]:
                        R -= 1
                    L += 1
                    R -= 1
                elif nums[R] + nums[L] < target:
                    L += 1
                elif nums[R] + nums[L] > target:
                    R -= 1
        return res