class MedianFinder:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        heapq.heapify(self.minHeap)
        heapq.heapify(self.maxHeap)

    def addNum(self, num: int) -> None:
        if self.minHeap and num < self.minHeap[0]:
            heapq.heappush(self.maxHeap, -1*num)
        else:
            heapq.heappush(self.minHeap, num)
        if abs(len(self.minHeap)-len(self.maxHeap)) > 1:
            if len(self.minHeap) > len(self.maxHeap):
                heapq.heappush(self.maxHeap, -1*heapq.heappop(self.minHeap))
            else:
                heapq.heappush(self.minHeap, -1*heapq.heappop(self.maxHeap))
    def findMedian(self) -> float:
        if (len(self.minHeap) + len(self.maxHeap)) % 2 == 0:
            return (self.minHeap[0] + (self.maxHeap[0]*-1))/2
        else:
            if len(self.minHeap) > len(self.maxHeap):
                return self.minHeap[0]
            else:
                return self.maxHeap[0]*-1