class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1, 48, 24, 6] prefix
        #[1, 2,  8,  1] suffix

        prefix = [nums[-1]]
        suffix = [nums[0]]
        ans = []

        for i in range(len(nums)-1):
            prefix.insert(0, prefix[0]*nums[-(i+2)])
            suffix.append(suffix[-1] * nums[i+1])

        for i in range(len(nums)):
            if i == 0:
                ans.append(prefix[1])
            elif i == len(nums)-1:
                ans.append(suffix[-2])
            else:
                ans.append(prefix[i+1]*suffix[i-1])

        return ans
            