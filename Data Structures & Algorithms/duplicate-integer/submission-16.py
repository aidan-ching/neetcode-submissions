class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #convert to set then compare length
        s_nums = set(nums)
        return len(s_nums) != len(nums)