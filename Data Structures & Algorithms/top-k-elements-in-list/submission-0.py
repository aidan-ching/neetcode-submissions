class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #top k most frequent can use heap

        #we count first
        count = defaultdict(int)
        for n in nums:
            count[n] += 1

        maxHeap = []

        for key,value in count.items():
            heapq.heappush(maxHeap, (value*-1, key))

        ans = []

        for i in range(k):
            ans.append(heapq.heappop(maxHeap)[1])

        return ans
