class Solution:
    def trap(self, height: List[int]) -> int:
        minL = [0] * len(height)
        minR = [0] * len(height)

        for i in range(1, len(height)):
            minL[i] = max(minL[i-1], height[i-1])

        for i in range(len(height)-2,-1,-1):
            minR[i] = max(minR[i+1], height[i+1])
        
        res = 0
        for i in range(len(height)):
            if (min(minL[i], minR[i]) - height[i])>0:
                res += min(minL[i], minR[i]) - height[i]
        return res

