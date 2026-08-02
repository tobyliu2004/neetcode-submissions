class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost)>sum(gas):
            return -1
        res = 0
        cur = 0
        for i in range(len(gas)-1):
            diff = gas[i]-cost[i]
            cur += diff
            if cur < 0:
                cur = 0
                res = i + 1
        return res