class Solution:
    def jump(self, nums: List[int]) -> int:
        l,r = 0,0
        res = 0
        track = 0
        while r < len(nums)-1:
            for i in range(l,r+1):
                track = max(track,nums[i]+i)
            l = r+1
            r = track
            res += 1
        return res