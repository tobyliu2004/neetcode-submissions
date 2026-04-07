class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = []
        for i in range(len(height)):
            if i == 0:
                maxLeft.append(0)
            else:
                maxLeft.append(max(height[i-1], maxLeft[i-1]))
        maxRight = [0] * len(height)
        for i in range(len(height)-1, -1, -1):
            if i == len(height)-1:
                maxRight[i] = 0
            else:
                maxRight[i] = max(height[i+1], maxRight[i+1])
        minLR = []
        for i in range(len(height)):
            minLR.append(min(maxLeft[i], maxRight[i]))
        res = []
        for i in range(len(height)):
            if minLR[i] - height[i] > 0:
                res.append(minLR[i] - height[i])
            else:
                res.append(0)
        final = 0
        for i in range(len(res)):
            final += res[i]
        return final