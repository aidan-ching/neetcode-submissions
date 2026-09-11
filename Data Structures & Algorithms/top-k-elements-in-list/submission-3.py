class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        arr = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] += 1

        #key, value -> value is count, and key is the num

        for key, value in count.items():
            arr[value].append(key)

        print(arr)

        #go backwards
        res = []
        for i in reversed(range(len(arr))):
            for n in arr[i]:
                res.append(n)

        return res[:k]
