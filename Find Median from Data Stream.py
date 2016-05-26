import heapq
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.maxLen = 0
        self.maxHeap = []
        self.minLen = 0
        self.minHeap = []
        

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if self.minLen == 0 or num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
            self.minLen += 1
        else:
            heapq.heappush(self.maxHeap, -1 * num)
            self.maxLen += 1
        ## adjust
        if self.minLen > self.maxLen + 1:
            val = heapq.heappop(self.minHeap)
            self.minLen -= 1
            heapq.heappush(self.maxHeap, -1 * val)
            self.maxLen += 1
        if self.minLen < self.maxLen:
            val = heapq.heappop(self.maxHeap)
            self.maxLen -= 1
            heapq.heappush(self.minHeap, -1 * val)
            self.minLen += 1

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if self.maxLen < self.minLen:
            return self.minHeap[0]
        else:
            return (self.minHeap[0] + self.maxHeap[0] * -1) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()
if __name__ == '__main__':
    s = MedianFinder()
    s.addNum(1)
    s.addNum(2)
    print s.findMedian()
    s.addNum(3)
    print s.findMedian()
    print s.minHeap
    print s.maxHeap