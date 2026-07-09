class MedianFinder:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        heapq.heapify(self.minHeap)
        heapq.heapify(self.maxHeap)

    def addNum(self, num: int) -> None:
        if not self.minHeap or num < self.minHeap[0]:
            heapq.heappush(self.maxHeap, -1*num)
        else:
            heapq.heappush(self.minHeap, num)
        if abs(len(self.minHeap)-len(self.maxHeap)) > 1:
            if len(self.minHeap) > len(self.maxHeap):
                move_num = heapq.heappop(self.minHeap) * -1
                heapq.heappush(self.maxHeap, move_num)
            else:
                move_num = heapq.heappop(self.maxHeap) * -1
                heapq.heappush(self.minHeap, move_num)

    def findMedian(self) -> float:
        if (len(self.minHeap) + len(self.maxHeap)) % 2 == 1:
            if len(self.minHeap) > len(self.maxHeap):
                return self.minHeap[0]
            else:
                return self.maxHeap[0]*-1
        else:
            return (self.minHeap[0]+(-1*self.maxHeap[0]))/2