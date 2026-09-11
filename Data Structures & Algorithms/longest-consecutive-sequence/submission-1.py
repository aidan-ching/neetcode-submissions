class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        lookup = set(nums)
        ans = 1

        for n in nums:
            curr = n
            while curr+1 in lookup:
                curr = curr+1
                ans = max(ans, curr-n+1)
                
        return ans
                
        