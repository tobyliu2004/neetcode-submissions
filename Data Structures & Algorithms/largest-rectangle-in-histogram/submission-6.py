class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][0] > heights[i]:
                prev_height, prev_index = stack.pop()
                max_area = max(max_area, prev_height*(i-prev_index))
                start = prev_index
            stack.append([heights[i], start])
        for height, start_index in stack:
            max_area = max(max_area, height * (len(heights) - start_index))
        return max_area