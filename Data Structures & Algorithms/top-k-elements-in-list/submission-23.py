class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #count
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1

        #place all into heap
        heap = []

        for key, value in counter.items():
            print(value, key)
            heap.append((value,key))

        #turn into heap and drop until k
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)

        #clean output:
        res = []
        for tup in heap:
            res.append(tup[1])

        return res

        