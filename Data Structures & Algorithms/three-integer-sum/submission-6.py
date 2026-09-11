class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #[-4, -1, -1, 0, 1, 2] 1 < 4 if too little move left pointer, if larger then move the left

        res = []
        nums.sort()
        res_set = set()

        # (-n[i]) = 4 = n[j] + n[k]

        for i in range(len(nums)):
            target = -nums[i]

            l,r = i+1, len(nums)-1

            while l<r:
                if nums[l]+nums[r] < target:
                    l += 1
                elif nums[l]+nums[r] > target:
                    r -=1
                else:
                    triplet = sorted([nums[i], nums[l], nums[r]])
                    if tuple(triplet) not in res_set:
                        res_set.add(tuple(triplet))
                        res.append([nums[i], nums[l], nums[r]])
                    l += 1
        return res
