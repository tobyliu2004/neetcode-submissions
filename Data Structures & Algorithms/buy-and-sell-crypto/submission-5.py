class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l + 1
        res = 0
        for r in range(len(prices)):
            res = max(res, prices[r]-prices[l])
            if prices[r]-prices[l] < 0:
                l = r
        return res