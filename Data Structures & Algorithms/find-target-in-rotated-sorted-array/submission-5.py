class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find minmum 
        l, r = 0, len(nums)-1

        while l < r:
            m = (l+r)//2

            if nums[m] < nums[r]:
                #its on the left side
                r = m
            else:
                l = m+1

        print(nums[l], l)

        if target == nums[l]: return l

        #find out which side that we want to check
        offset = l
        if offset == 0:
            l, r = 0, len(nums)-1
        elif target > nums[0]: #left side
            l, r = 0, l
        elif target < nums[0]: #right side
            l, r = l, len(nums)-1
        elif target == nums[0]:
            return 0

        #run standard binary search on those

        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif target > nums[m]:
                l = m+1
            else:
                r = m-1

        return -1
            



