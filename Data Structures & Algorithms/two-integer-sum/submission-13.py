class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums[j] = target - nums[i]
        # use hashmap to check
        # for each, store into hashmap with key as nums[i] val as index
        m = {}
        for i, n in enumerate(nums):
            if target - n in m:
                return [m[target-n], i]
            else:
                m[n] = i
        

        