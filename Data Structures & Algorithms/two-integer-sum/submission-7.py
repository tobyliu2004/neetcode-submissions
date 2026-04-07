class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        main = defaultdict(int)
        for i, n in enumerate(nums):
            diff = target - n
            if diff in main:
                return [main[diff], i]
            main[n] = i