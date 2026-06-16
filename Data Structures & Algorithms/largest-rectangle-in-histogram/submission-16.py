class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][0] > heights[i]:
                prev_height, prev_index = stack.pop()
                max_area = max(max_area, prev_height*(i-prev_index))
                start = prev_index
            stack.append([h, start])
        for i in range(len(stack)):
            max_area = max(max_area, (len(heights)-stack[i][1]) * stack[i][0])
        return max_area