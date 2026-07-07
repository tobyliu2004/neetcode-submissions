class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-st for st in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            y = heapq.heappop(maxHeap) * -1
            x = heapq.heappop(maxHeap) * -1
            if y != x:
                heapq.heappush(maxHeap, -1 * (y-x))
        if maxHeap:
            return maxHeap[0] * -1
        return 0