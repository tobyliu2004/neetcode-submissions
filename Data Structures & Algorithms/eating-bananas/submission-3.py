class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        def canFinish(m):
            hours = 0
            for i in piles:
                if i % m == 0:
                    hours += i // m
                else:
                    hours += (i//m) + 1
            if hours > h:
                return False
            return True
        
        while l <= r:
            m = (l + r) // 2
            if canFinish(m):
                min_hours = m
                r = m - 1
            else:
                l = m + 1
        return min_hours