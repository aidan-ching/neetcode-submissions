class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k

        for n in nums:
            heapq.heappush(self.heap, n)
            if len(self.heap) > k:
                heapq.heappop(self.heap)
        #looking for 3rd largest
        #in a min heap, if you pop 1, 2, 3
        #if larger than k, pop

        #max heap. If len(heap) gonna go over k then you pop.

    #  3 3 5
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

        
