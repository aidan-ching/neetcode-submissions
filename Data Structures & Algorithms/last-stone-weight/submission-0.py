class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #x is heaviest
        #y is second heaviest

        #max heap.
        #while len(heap) > 1
        #pop top and second top(pop twice)
        #do our compairisons
        #insert back abs(x-y) if theyre not equal else just pop them

        heap = []
        for n in stones:
            heapq.heappush(heap, -1*n)

        while len(heap) > 1:
            x = heapq.heappop(heap)*-1
            y = heapq.heappop(heap)*-1

            if x!=y:
                heapq.heappush(heap, -1*(abs(x-y)))
        
        return 0 if len(heap) == 0 else heap[0]*-1


