import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first lets count
        count = defaultdict(int)
        for n in nums:
            count[n] += 1

        #lets put it into a heap
        heap = []

        for n in count.keys():
            heapq.heappush(heap,(count[n], n))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for t in heap:
            res.append(t[1])

        return res

        


        