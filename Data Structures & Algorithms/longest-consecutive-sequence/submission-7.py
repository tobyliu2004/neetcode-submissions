class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0
        for i in seen:
            if i-1 not in seen:
                length = 1
                while (i+1) in seen:
                    length += 1
                    i += 1
                longest = max(length,longest)
        return longest
        