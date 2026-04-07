class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        def possible(k):
            hours = 0
            for i in range(len(piles)):
                if piles[i]%k == 0:
                    hours += piles[i]//k
                else:
                    hours += piles[i]//k + 1
            if hours <= h:
                return True
            return False
        
        while l <= r:
            m = (l + r) // 2
            if possible(m):
                min_hours = m
                r = m-1
            elif not possible(m):
                l = m + 1

        return min_hours