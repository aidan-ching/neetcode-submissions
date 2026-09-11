class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #min heap
        # heap larger than k then pop

        #      4 5
        heap = []
        if not nums:
            return None

        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]
        