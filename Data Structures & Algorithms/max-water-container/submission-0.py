class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #height = r-l * min(heights[l], heights[r])
        maximum = 0

        l, r = 0, len(heights)-1

        while l < r:
            maximum = max(maximum, (r-l) * min(heights[l], heights[r]))

            #we want to keep the longer part 
            if heights[l] > heights[r]:
                #move shorter
                r -= 1
            else:
                l += 1

        return maximum


        