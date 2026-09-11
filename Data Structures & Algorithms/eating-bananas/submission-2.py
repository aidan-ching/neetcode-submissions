class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #init array with range 1 -> max(piles)

        #we need a function to see how many hours it would take with k speed
        def hours(k):
            total = 0
            for num in piles:
                total += math.ceil(num/k)

            return total


        #binary search

        l,r = 1, max(piles)

        while l<=r:
            m = l + (r-l)//2
            time = hours(m)
            #if time is longer than hours given, then we have to increase the rate
            if time > h:
                #move l
                l = m+1
            elif time <= h:
                #move r
                r = m-1
        
        return l

