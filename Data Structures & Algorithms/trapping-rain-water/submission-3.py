class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = []
        for i in range(len(height)):
            if i == 0:
                maxLeft.append(0)
            else:
                maxLeft.append(max(maxLeft[i-1], height[i-1]))
        maxRight = [0] * len(height)
        for i in range(len(height)-1, -1, -1):
            if i == len(height)-1:
                maxRight[i] = 0
            else:
                maxRight[i] = max(maxRight[i+1], height[i+1])
        mins = []
        for i in range(len(height)):
            mins.append(min(maxRight[i], maxLeft[i]))
        res_list = []
        for i in range(len(height)):
            if mins[i]-height[i] > 0:
                res_list.append(mins[i]-height[i])
            else:
                res_list.append(0)
        res = 0
        for i in range(len(height)):
            res += res_list[i]
        return res