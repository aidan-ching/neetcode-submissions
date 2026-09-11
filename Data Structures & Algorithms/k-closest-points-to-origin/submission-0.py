class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #we can use a min heap for this problem
        #append the calculations going through the list

        heap = []

        for p in points:
            x = p[0]
            y = p[1]

            heapq.heappush(heap, (math.sqrt(x**2 + y**2), [x,y]))
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res
