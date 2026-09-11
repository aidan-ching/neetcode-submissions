class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort, fix i and run 2sum 2 on the list next to it

        nums.sort()
        #[-4,-1,-1,0,1,2]

        res = []

        for i in range(len(nums)):
            #init 2 pointers
            l, r, target = i+1, len(nums)-1, -1*nums[i]
            #check if i is the same as the previous one
            if i > 0 and nums[i] == nums[i-1]:
                continue

            #-nums[i] = nums[j] + nums[k]
            while l < r:
                s = nums[l] + nums[r]
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    if (len(res) > 0 and res[-1] != [nums[i], nums[l], nums[r]]) or len(res) == 0:
                        res.append([nums[i], nums[l], nums[r]])
                    
                    l += 1

        return res


                


        