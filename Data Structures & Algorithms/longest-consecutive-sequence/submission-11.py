class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        track = set()
        longest = 0
        for i in nums:
            track.add(i)
        for i in track:
            if i-1 in track:
                continue
            else:
                count = 1
                curr = i
                while curr+1 in track:
                    curr += 1
                    count += 1
                longest = max(longest, count)
        return longest