from heapq import *

class MedianFinder:

    def __init__(self):
        self.heap_low = []
        self.heap_high = []

    def addNum(self, num: int) -> None:
        heappush(self.heap_high, -heappushpop(self.heap_low, -num))
        if len(self.heap_high) > len(self.heap_low):
            heappush(self.heap_low, -heappop(self.heap_high))

    def findMedian(self) -> float:
        if len(self.heap_high) == len(self.heap_low):
            return (self.heap_high[0] - self.heap_low[0]) / 2
        return -self.heap_low[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()