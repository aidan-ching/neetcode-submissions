class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #lets count first
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

        # lets throw all the counts into a tuple (count, number) so we can heap it

        heap = []
        for key, value in count.items():
            heap.append((value,key))

        heapq.heapify(heap)
        
        while len(heap) > k:
            heapq.heappop(heap)

        

        
        #lets loop through heap and only grab the values 

        res = []

        for key, value in heap:
            res.append(value)

        return res