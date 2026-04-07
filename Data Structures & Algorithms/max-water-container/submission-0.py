class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_amt = 0
        L = 0
        R = len(heights) - 1
        while R>L:
            amt = min(heights[L], heights[R]) * (R-L)
            max_amt = max(amt, max_amt)
            if heights[L] < heights[R]:
                L += 1
            elif heights[R] < heights[L]:
                R -= 1
            else:
                L += 1
                R -= 1
        return max_amt