class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in comp:
                return [comp[diff], i]
            comp[val] = i
        return
