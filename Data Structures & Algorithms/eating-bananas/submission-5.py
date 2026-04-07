class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFit(k):
            total = 0
            for i in range(len(piles)):
                if piles[i] % k == 0:
                    total += piles[i] / k
                else:
                    total += (piles[i] // k) + 1
            return total <= h
        
        l = 1
        r = max(piles)
        minSpeed = max(piles)
        while l <= r:
            m = (l+r) // 2
            if canFit(m):
                minSpeed = min(minSpeed, m)
                r = m - 1
            else:
                l = m + 1
        return minSpeed