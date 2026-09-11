class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        print(len(set(nums)), len(nums))
        if len(set(nums)) != len(nums):
            return True
        else:
            return False
         