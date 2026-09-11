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

        l, r = 0, offset-1

        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif target > nums[m]:
                l = m+1
            else:
                r = m-1

        l, r = l+1, len(nums)-1

        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif target > nums[m]:
                l = m+1
            else:
                r = m-1

        return -1
            



