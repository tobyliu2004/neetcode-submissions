import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums)-k
        l, r = 0, len(nums)-1
        while True:
            rand_idx = random.randint(l, r)
            nums[r], nums[rand_idx] = nums[rand_idx], nums[r]
            p = l
            pivot = nums[r]

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if p < k:
                l = p+1
            elif p>k:
                r = p - 1
            else:
                return nums[p]