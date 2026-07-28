class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        total = 0
        res = 0
        for i in range(len(gas)):
            diff = gas[i]-cost[i]
            total += diff
            if total < 0:
                res = i + 1
                total = 0
        return res
            