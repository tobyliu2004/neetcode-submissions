class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #return len(set(nums))<len(nums)

        hset = set()

        for i in nums:
            if i in hset:
                return True
            hset.add(i)
        return False