class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #two pointers, look one ahead, and iterate the one that is longer
        #keep track of max with variable
        #(r - l) * min(height[l], height[r]) 

        maximum = float('-inf')

        l, r = 0, len(heights)-1

        while l < r:
            maximum = max(maximum, (r-l)*min(heights[l], heights[r]))
            if heights[l] > heights[r]:
                r-= 1
            else:
                l += 1
        return maximum
