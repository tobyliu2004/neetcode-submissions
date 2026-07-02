class MedianFinder:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        heapq.heapify(self.minHeap)
        heapq.heapify(self.maxHeap)

    def addNum(self, num: int) -> None:
        if self.minHeap and self.minHeap[0]<num:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -1*num)
        
        if abs(len(self.minHeap)-len(self.maxHeap)) > 1:
            if len(self.minHeap) > len(self.maxHeap):
                num = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, num*-1)
            else:
                num = heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, num*-1)

    def findMedian(self) -> float:
        if (len(self.maxHeap)+len(self.minHeap)) % 2 == 0:
            return ((-1*self.maxHeap[0]) + self.minHeap[0]) / 2
        else:
            if len(self.maxHeap)>len(self.minHeap):
                return -1 * self.maxHeap[0]
            else:
                return self.minHeap[0]