class MedianFinder:

    def __init__(self):
        self.heap = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap, num)
        

    def findMedian(self) -> float:
        r = len(self.heap)//2 + 1


        res = heapq.nsmallest(r, self.heap)
        print(res)

        return res[-1] if len(self.heap) % 2 == 1 else (res[-1]+res[-2])/2


        
        