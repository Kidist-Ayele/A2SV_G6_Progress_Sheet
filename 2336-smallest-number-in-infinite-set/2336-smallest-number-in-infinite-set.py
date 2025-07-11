class SmallestInfiniteSet:

    def __init__(self):
        self.next_num = 1                     
        self.heap = []                         
        self.in_heap = set()   
                       
    def popSmallest(self) -> int:
        if self.heap:
            smallest = heappop(self.heap)
            self.in_heap.remove(smallest)
            return smallest
        else:
            self.next_num += 1
            return self.next_num - 1

    def addBack(self, num: int) -> None:
        if num < self.next_num and num not in self.in_heap:
            heappush(self.heap, num)
            self.in_heap.add(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)