class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #use heap
        count = defaultdict(int)
        for n in nums: #O(N)
            count[n] += 1

        #put all into the heap
        heap = []
        for key, val in count.items():
            heapq.heappush(heap, (val, key))

        while len(heap) > k:
            heapq.heappop(heap)
        res = []
        for val, key in heap:
            res.append(key)

        return res
        