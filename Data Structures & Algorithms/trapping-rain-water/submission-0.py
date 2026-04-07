class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = []
        for i in range(len(height)):
            if i == 0:
                maxLeft.append(0)
            elif i == 1:
                maxLeft.append(height[i-1])
            else:
                maxLeft.append(max(height[i-1], maxLeft[i-1]))
        maxRight = [0] * len(height)
        for i in range(len(height)-1, -1, -1):
            if i == len(height)-1:
                maxRight[i] = 0
            elif i == len(height)-2:
                maxRight[i] = height[i+1]
            else:
                maxRight[i] = max(height[i+1], maxRight[i+1])
        l_r = []
        for i in range(len(maxRight)):
            l_r.append(min(maxLeft[i], maxRight[i]))
        waters = []
        for i in range(len(l_r)):
            if l_r[i]-height[i] < 0:
                waters.append(0)
            else:
                waters.append(l_r[i]-height[i])
        res = 0
        for i in waters:
            res += i
        return res
