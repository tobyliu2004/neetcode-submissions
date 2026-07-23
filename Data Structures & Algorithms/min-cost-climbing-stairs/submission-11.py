class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = 0,0
        for i in range(len(cost)-1,-1,-1):
            cur = cost[i] + min(one, two)
            temp = one
            one = cur
            two = temp
        return min(one, two)