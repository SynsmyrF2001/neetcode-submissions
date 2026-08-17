class MedianFinder:

    def __init__(self):
        # max_heap stores the smaller half of the numbers (negated)
        # min_heap stores the larger half of the numbers
        self.small = [] # max_heap
        self.large = [] # min_heap 
        

    def addNum(self, num: int) -> None:
        # Add to max_heap first 
        heapq.heappush(self.small, -num)

        # Ensure every number in small is <= every number in large 
        # Move the largest element from small to large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # Balance the heaps
        # If small is larger than large by more than 1, move from small to large 
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        # If large is larger than small, move from large to small
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            # Odd number of elements, medium is top of small heap
            return -self.small[0]
        else:
            # Even number of elements, median is average of tops of both heaps
            return (-self.small[0] + self.large[0]) / 2
        
         