class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                cur = prices[r]-prices[l]
                profit = max(cur, profit)
            else:
                l = r
            r += 1
        return profit