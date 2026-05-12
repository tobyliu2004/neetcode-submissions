class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l<r:
            mid = (l+r)//2
            total = 0
            for i in piles:
                total += math.ceil(i/mid)
            if total > h:
                l = mid + 1
            else:
                r = mid

        return r