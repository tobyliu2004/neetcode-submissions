import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums)-k
        l = 0
        r = len(nums)-1
        while True:
            rand_idx = random.randint(l,r)
            p = l
            nums[r], nums[rand_idx]=nums[rand_idx], nums[r]
            pivot = nums[r]
            for i in range(l,r):
                if nums[i]<=pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if p < k:
                l = p+1
            elif p>k:
                r = p-1
            else:
                return nums[p]