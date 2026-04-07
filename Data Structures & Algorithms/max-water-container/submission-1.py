class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        max_amt = 0
        while l < r:
            amt = min(heights[l], heights[r]) * (r-l)
            max_amt = max(max_amt, amt)
            if heights[l]<=heights[r]:
                l += 1
            elif heights[l]>=heights[r]:
                r -= 1
        return max_amt