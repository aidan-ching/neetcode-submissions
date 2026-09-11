class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #change to set then compare lengths
        return len(set(nums)) != len(nums)