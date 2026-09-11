class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #formula: r-l * min(heights[l], heights[r])

        l,r = 0, len(heights)-1
        max_volume = 0
        while l<r:
            # increment max_volume if possible
            curr = (r-l) * min(heights[l], heights[r])
            max_volume = max(max_volume, curr)

            print(l,r, curr)

            #if left is taller than right then move right
            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1

        return max_volume

        