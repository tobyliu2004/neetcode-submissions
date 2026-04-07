class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for i in nums:
            seen.add(i)
        
        count = 0
        res = 0
        for i in seen:
            if (i - 1) in seen:
                continue
            else:
                count = 1
                res = max(count, res)
                curr = i
                while (curr+1) in seen:
                    curr += 1
                    count += 1
                    res = max(count, res)
        return res