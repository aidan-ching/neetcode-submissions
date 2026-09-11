class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        l,r = 0, 1
        #move right until left > right
        # if we hit this condition then we move left to right and right to left+1.

        profit = 0 

        while r < len(prices):
            profit = max(profit, prices[r] - prices[l])
            if prices[l] > prices[r]:
                l = r
            r += 1

        return profit