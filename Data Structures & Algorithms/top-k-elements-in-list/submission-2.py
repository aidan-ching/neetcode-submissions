class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #hashmap counter
        #insert into array, with indicies being occurances and values being key

        #this array has the same length as nums
        hm = Counter(nums)
        arr = [[] for i in range(len(nums)+1)]

        for key, value in hm.items():
            print(key,value)
            arr[value].append(key)

        res = []

        for i in range(len(arr)-1, 0, -1):
            for j in range(len(arr[i])):
                res.append(arr[i][j])
                if len(res) == k:
                    return res


        