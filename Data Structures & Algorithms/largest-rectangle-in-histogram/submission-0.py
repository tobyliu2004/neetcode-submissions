class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                res = max(res, height * (i-index))
                start = index
            stack.append([start, heights[i]])
        for index, height in stack:
            res = max(res, height * (len(heights) - index))
        return res