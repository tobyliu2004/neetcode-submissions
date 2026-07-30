class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        for i in tasks:
            counts[i] = 1 + counts.get(i,0)
        minHeap = list([-i for i in counts.values()])
        heapq.heapify(minHeap)
        q = deque()
        time = 0
        while minHeap or q:
            time += 1
            if minHeap:
                val = heapq.heappop(minHeap)+1
                if val != 0:
                    q.append([val, time+n])
            if q and q[0][1] == time:
                heapq.heappush(minHeap, q.popleft()[0])
        return time