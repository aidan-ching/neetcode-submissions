class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            target = -nums[i]
            while l < r:
                total = nums[l] + nums[r]
                if total < target:
                    l += 1 
                elif total > target:
                    r -= 1
                else:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1

        ans = []

        for a in list(res):
            ans.append(list(a))
        return ans
                

        
        