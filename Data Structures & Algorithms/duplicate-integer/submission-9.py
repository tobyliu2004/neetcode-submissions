class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = set()
        for i in nums:
            if i in dict:
                return True
            dict.add(i)
        return False