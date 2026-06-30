class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            y = heapq.heappop(maxHeap) * -1
            x = heapq.heappop(maxHeap) * -1
            if x < y:
                dif = y-x
                heapq.heappush(maxHeap, -1 * dif)
        maxHeap.append(0)
        return abs(maxHeap[0])