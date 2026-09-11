class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #we want buy low sell high
        #if our right pointer is lower than left, then we can just move it

        l, r = 0, 1
        m = 0

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r = l+1

            else:
                m = max(m, prices[r]-prices[l])
                r += 1

        return m

