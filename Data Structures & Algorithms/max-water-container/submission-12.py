class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1

        m = 0

        while l < r:
            #calcualte current weight of wata
            curr = (min(heights[l], heights[r])) * (r-l)
            print(curr, l, r)
            m = max(curr, m)

            #move l/r depending on which is shorter
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return m
        