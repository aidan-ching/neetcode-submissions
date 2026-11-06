class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,4,6]
        # [1,1,2,8]
        # [48,24,6,1]

        #[1,1,1,1]

        left = [1]*len(nums)
        right = [1]*len(nums)
        res = []

        #calculate left first
        total = 1
        for i in range(1, len(nums)):
            total = total*nums[i-1]
            left[i] = total
        # print(left)

        total = 1
        for i in range(len(nums)-2, -1, -1):
            total = total*nums[i+1]
            right[i] = total

        # print(right)

        for i in range(len(nums)):
            res.append(left[i]*right[i])

        return res