class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        heapq.heapify(self.minHeap)
        heapq.heapify_max(self.maxHeap)
        
    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.maxHeap, num)

        if self.maxHeap and self.minHeap and self.maxHeap[0] > self.minHeap[0]:
            heapq.heappush(self.minHeap, heapq.heappop_max(self.maxHeap))

        if len(self.maxHeap) > len(self.minHeap) + 1:
            popped = heapq.heappop_max(self.maxHeap)
            heapq.heappush(self.minHeap, popped)
        elif len(self.minHeap) > len(self.maxHeap) + 1:
            popped = heapq.heappop(self.minHeap)
            heapq.heappush_max(self.maxHeap, popped)

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return self.maxHeap[0]
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return (self.minHeap[0] + self.maxHeap[0]) / 2
        