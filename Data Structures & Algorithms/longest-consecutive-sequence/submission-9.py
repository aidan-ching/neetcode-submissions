class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #lets have an array with a length of the max value of nums
        #count consecutive numbers there 0 for does not exist, 1 for does exist
        #we would have to handle negative numbers as well

        #length of maximum - minimum + 1
        #[0,0,0,0,0,0,0,0]
        #5 -> -2
        #-2 would map to arr[0] and 5 would map to arr[7]
        #n is -2 -(-2) = 0
        # n - minimum would grant the appropriate spot
        #1 -> 5

        if not nums:
            return 0
        elif len(nums) == 1:
            return 1


        numsMax = max(nums)
        numsMin = min(nums)



        arr = [0] * (numsMax-numsMin+1)

        #we would need to figure out a way to place these values in arr in the correct place

        for n in nums:
            arr[n-numsMin] = 1

        #now we count the consequctive ones
        maximum = 0
        if len(arr) == 1:
            return 1

        for i in range(1, len(arr)):
            if arr[i] != 0 and arr[i-1] != 0 :
                #add to arr
                arr[i] = arr[i-1]+1
            maximum = max(maximum, arr[i])

        print(arr)

        return maximum









        