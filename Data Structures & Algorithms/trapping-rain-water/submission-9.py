class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = [0] * len(height)
        maxR = [0] * len(height)
        for i in range(len(height)):
            if i == 0:
                maxL[i] = 0
            else:
                maxL[i] = max(height[i-1], maxL[i-1])
        for i in range(len(height)-1,-1,-1):
            if i == len(height)-1:
                maxR[i] = 0
            else:
                maxR[i] = max(height[i+1], maxR[i+1])
        res = 0
        for i in range(len(height)):
            water = min(maxL[i],maxR[i])-height[i]
            if water > 0:
                res += water
        return res