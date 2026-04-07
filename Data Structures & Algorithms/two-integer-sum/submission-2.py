class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        main_map = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in main_map:
                return [main_map[diff], i]
            main_map[nums[i]] = i
        return