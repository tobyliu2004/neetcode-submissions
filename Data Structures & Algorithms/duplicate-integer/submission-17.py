class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m = defaultdict(int)
        for i in nums:
            if m[i] == 1:
                return True
            else:
                m[i] += 1
        return False