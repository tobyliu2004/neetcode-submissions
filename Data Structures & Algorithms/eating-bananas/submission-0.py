class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        def can_finish(k):
            hours = 0
            for i in piles:
                if i % k == 0:
                    hours += i //k
                else:
                    hours += (i//k + 1)
            if hours <= h:
                return True
        
        while l <= r:
            k = (l + r) // 2
            if can_finish(k):
                result = k
                r = k -1
            else:
                l = k + 1
        return result