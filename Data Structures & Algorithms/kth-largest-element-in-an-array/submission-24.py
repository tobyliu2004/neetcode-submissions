import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l,r = 0, len(nums)-1
        k = len(nums)-k
        while True:
            rand_idx = random.randint(l,r)
            nums[r], nums[rand_idx] = nums[rand_idx], nums[r]
            pivot = nums[r]
            p = l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[r], nums[p] = nums[p], nums[r]
            if p < k:
                l = p + 1
            elif p > k:
                r = p - 1
            else:
                return nums[p]
            
