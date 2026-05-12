class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][0] > heights[i]:
                height, index = stack.pop()
                max_area = max(max_area, height*(i-index))
                start = index
            stack.append([heights[i], start])
        for i in range(len(stack)):
            max_area = max(max_area, stack[i][0]*(len(heights)-stack[i][1]))

        return max_area