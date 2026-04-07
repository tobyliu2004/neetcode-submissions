class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in nums_map:
                return[nums_map[diff], i]
            nums_map[n] = i
        return