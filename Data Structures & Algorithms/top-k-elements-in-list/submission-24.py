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
        heap.sort()

        res = []
        for i in range(1, k+1):
            res.append(heap[-i][1])

        return res
        