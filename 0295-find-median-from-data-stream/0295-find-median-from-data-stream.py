class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: int) -> None:
        heappush(self.max_heap, -num)

        x = heappop(self.max_heap)
        heappush(self.min_heap, -x)

        if len(self.min_heap) > len(self.max_heap):
            poped = heappop(self.min_heap)
            heappush(self.max_heap, -poped)
            
        

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            left, right = -self.max_heap[0], self.min_heap[0]
            return (left + right)/2
        return -self.max_heap[0]
         
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()