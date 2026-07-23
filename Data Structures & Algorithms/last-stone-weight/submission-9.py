class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-i for i in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            y = heapq.heappop(maxHeap) * -1
            x = heapq.heappop(maxHeap) * -1
            if x != y:
                weight = (y-x) * -1
                heapq.heappush(maxHeap, weight)
        return maxHeap[0]*-1 if maxHeap else 0