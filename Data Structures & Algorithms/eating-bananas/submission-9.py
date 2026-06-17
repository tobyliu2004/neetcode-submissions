class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        min_time = 0
        while l <= r:
            mid = (l+r)//2
            total_time = 0
            for i in piles:
                total_time += math.ceil(i/mid)
            if total_time <= h:
                min_time = mid
                r = mid - 1
            else:
                l = mid + 1
        return min_time