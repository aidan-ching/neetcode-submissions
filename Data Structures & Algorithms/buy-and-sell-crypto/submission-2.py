class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1

        profit = 0

        while r < len(prices):
            profit = max(prices[r]-prices[l], profit)
            while prices[l] > prices[r]:
                l += 1

            r += 1

        return profit

            
        