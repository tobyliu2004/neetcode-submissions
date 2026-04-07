class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        longest = 0
        for i in nums:
            seen.add(i)
        for i in seen:
            if i-1 in seen:
                continue
            else:
                curr = 1
                while i+1 in seen:
                    curr += 1
                    i = i + 1
                longest = max(curr, longest)
        return longest