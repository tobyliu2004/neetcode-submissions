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
        
        for i in range(len(stack)):
            max_area = max(max_area, stack[i][0]*(len(heights)-stack[i][1]))
        return max_area